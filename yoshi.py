```python
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

from PIL import Image, ExifTags, ImageOps
from tkinterdnd2 import DND_FILES, TkinterDnD


class GhostWasher:
    """
    YOSHI! (Ghost Washer)

    A small bilingual desktop helper that rebuilds image pixels onto a new canvas
    to reduce the risk of sharing common embedded metadata such as Exif and GPS.
    """

    # Metadata keys in Image.info that are worth showing to the user.
    # This is intentionally conservative: some Image.info fields are technical
    # encoder details, while these keys are more likely to contain user-visible
    # or privacy-related metadata.
    INFO_KEYS_OF_INTEREST = {
        "exif",
        "icc_profile",
        "XML:com.adobe.xmp",
        "xmp",
        "comment",
        "description",
        "author",
        "copyright",
        "software",
        "creation_time",
        "date",
    }

    def __init__(self, root, lang="jp"):
        self.root = root
        self.lang = lang
        self.res = self.load_resources(lang)

        self.root.title(f"YOSHI! Ghost Washer v0.1.0 - {'English' if lang == 'en' else '日本語'}")
        self.root.geometry("550x600")

        # Font settings.
        self.jp_font_family = ("Meiryo", "MS UI Gothic", "Yu Gothic", "sans-serif")
        self.normal_font = (self.jp_font_family[0], 10)
        self.log_font = ("Consolas", 10)
        self.yoshi_font = ("MS Gothic", 12, "bold")

        # Main UI.
        self.label = tk.Label(root, text=self.res["label"], pady=10, font=self.normal_font)
        self.label.pack()

        self.info_area = scrolledtext.ScrolledText(root, height=20, width=65, font=self.log_font)
        self.info_area.pack(padx=10, pady=10)

        self.info_area.tag_configure("normal", font=self.normal_font)
        self.info_area.tag_configure("yoshi", foreground="green", font=self.yoshi_font)
        self.info_area.tag_configure("danger", foreground="red", font=(self.jp_font_family[0], 10, "bold"))

        self.clear_info_area(self.res["wait"])

        # Enable drag and drop.
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind("<<Drop>>", self.handle_drop)

    @staticmethod
    def load_resources(lang):
        """Return UI strings for the selected language."""
        resources = {
            "jp": {
                "label": "\n画像をドロップしてください（複数ファイル対応）",
                "wait": "待機中... 😸 (Standby)",
                "scan": "スキャン開始: ",
                "clean": "\n【判定】\n対応しているメタデータは検出されませんでした。\n\nヨシッ！ 👉😸✨",
                "danger": "⚠️ 対応しているメタデータを検出しました：",
                "confirm_title": "現場確認",
                "confirm_msg": (
                    "画像に「{}件」のメタデータが見つかりました。\n"
                    "対応しているメタデータを削減するため、画像を再構成しますか？"
                ),
                "washed_title": "再構成が完了しました！ ✨",
                "washed_info": (
                    "【保存情報】\n"
                    "元のファイル名に「_washed」を付与して保存しました。\n\n"
                    "ファイル名: {}\n"
                    "保存場所: {}\n\n"
                    "必要に応じて、このファイルを再度ドロップして確認してください。\n"
                    "※画像内に写り込んだ情報や投稿文脈までは削除できません。"
                ),
                "unsupported": "この形式では対応メタデータを読み取れない可能性があります。",
                "tags": {
                    "DateTime": "撮影日時",
                    "DateTimeOriginal": "撮影日時",
                    "DateTimeDigitized": "デジタル化日時",
                    "Make": "メーカー",
                    "Model": "カメラ機種名",
                    "Software": "使用ソフト",
                    "GPSInfo": "位置情報(GPS)",
                    "Artist": "作成者",
                    "Copyright": "著作権情報",
                    "ImageDescription": "画像説明",
                    "UserComment": "ユーザーコメント",
                },
                "info_tags": {
                    "exif": "Exifデータ",
                    "icc_profile": "ICCカラープロファイル",
                    "XML:com.adobe.xmp": "XMPメタデータ",
                    "xmp": "XMPメタデータ",
                    "comment": "コメント",
                    "description": "説明",
                    "author": "作成者",
                    "copyright": "著作権情報",
                    "software": "使用ソフト",
                    "creation_time": "作成日時",
                    "date": "日付情報",
                },
            },
            "en": {
                "label": "\nDrop images here (multiple files supported)",
                "wait": "Waiting... 😸 (Standby)",
                "scan": "Scan started: ",
                "clean": "\n[Result]\nNo supported metadata detected.\n\nLGTM! (Looks Good To Me) 👉😸✨",
                "danger": "⚠️ Supported metadata detected:",
                "confirm_title": "Confirmation",
                "confirm_msg": (
                    "Found {} metadata item(s).\n"
                    "Do you want to rebuild the image to reduce supported embedded metadata?"
                ),
                "washed_title": "Rebuild complete! ✨",
                "washed_info": (
                    "[Saved Info]\n"
                    "Appended '_washed' to the original filename.\n\n"
                    "Filename: {}\n"
                    "Path: {}\n\n"
                    "You can drop the new file again to verify supported metadata fields.\n"
                    "Note: visible clues in the image and surrounding post context are not removed."
                ),
                "unsupported": "This format may not expose supported metadata fields.",
                "tags": {},
                "info_tags": {},
            },
        }

        return resources.get(lang, resources["en"])

    def clear_info_area(self, msg):
        """Clear the log area and display a header message."""
        self.info_area.delete("1.0", tk.END)
        self.info_area.insert(tk.END, f"{msg}\n", "normal")
        self.info_area.insert(tk.END, "-" * 60 + "\n", "normal")

    def handle_drop(self, event):
        """Handle one or more files dropped into the window."""
        files = self.root.tk.splitlist(event.data)

        for file_path in files:
            self.process_file(file_path.strip("{}"))

    def process_file(self, file_path):
        """Scan a file, show supported metadata, and ask whether to wash it."""
        self.clear_info_area(f"{self.res['scan']}{os.path.basename(file_path)}")

        try:
            img = Image.open(file_path)
            metadata_items = self.collect_supported_metadata(img)

            if not metadata_items:
                self.info_area.insert(tk.END, self.res["clean"], "yoshi")
                return

            self.info_area.insert(tk.END, f"{self.res['danger']}\n\n", "danger")

            for key, value in metadata_items:
                self.info_area.insert(tk.END, f" ・{key}: {value}\n", "normal")

            should_wash = messagebox.askyesno(
                self.res["confirm_title"],
                self.res["confirm_msg"].format(len(metadata_items)),
            )

            if should_wash:
                self.wash_process(img, file_path)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process the image:\n{e}")

    def collect_supported_metadata(self, img):
        """
        Collect metadata fields supported by this tool.

        Exif is read through Pillow's getexif().
        A small set of Image.info fields is also checked for common metadata blocks.
        """
        items = []

        # Read Exif metadata when Pillow exposes it.
        exif = img.getexif()
        if exif:
            for tag_id, value in exif.items():
                tag_en = ExifTags.TAGS.get(tag_id, str(tag_id))
                tag_display = self.res["tags"].get(tag_en, tag_en) if self.lang == "jp" else tag_en
                items.append((tag_display, self.format_metadata_value(value)))

        # Read selected Image.info metadata keys.
        for key, value in img.info.items():
            key_lower = str(key).lower()

            if key in self.INFO_KEYS_OF_INTEREST or key_lower in self.INFO_KEYS_OF_INTEREST:
                display_key = self.res["info_tags"].get(key, key)
                items.append((display_key, self.format_metadata_value(value)))

        return items

    @staticmethod
    def format_metadata_value(value, max_length=160):
        """Convert metadata values into short, readable text for the UI."""
        if isinstance(value, bytes):
            return f"<binary data: {len(value)} bytes>"

        text = str(value).replace("\n", "\\n")

        if len(text) > max_length:
            return text[:max_length] + "..."

        return text

    def wash_process(self, img, file_path):
        """
        Rebuild the visible image data and save it as a new file.

        This helps avoid carrying over common embedded metadata. It is not a
        complete anonymity guarantee and does not remove visible clues in the image.
        """
        try:
            # Apply Exif orientation first so the rebuilt image keeps the expected view.
            visible_img = ImageOps.exif_transpose(img)

            # Rebuild the visible pixel data on a fresh image canvas.
            clean_img = Image.new(visible_img.mode, visible_img.size)
            clean_img.putdata(visible_img.getdata())

            base, ext = os.path.splitext(file_path)
            ext_lower = ext.lower()
            new_filename = f"{os.path.basename(base)}_washed{ext}"
            new_path = os.path.join(os.path.dirname(file_path), new_filename)

            # JPEG does not support alpha channels, so convert when needed.
            save_img = clean_img
            if ext_lower in {".jpg", ".jpeg"} and save_img.mode not in {"RGB", "L"}:
                save_img = save_img.convert("RGB")

            # Save without intentionally attaching metadata.
            save_kwargs = {}

            if ext_lower in {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}:
                save_kwargs["exif"] = b""

            if ext_lower in {".jpg", ".jpeg", ".png"}:
                save_kwargs["optimize"] = True

            save_img.save(new_path, **save_kwargs)

            # Show the "LGTM / YOSHI!" result after washing.
            self.clear_info_area(self.res["washed_title"])
            self.info_area.insert(tk.END, self.res["clean"], "yoshi")
            self.info_area.insert(
                tk.END,
                "\n\n" + self.res["washed_info"].format(new_filename, os.path.dirname(file_path)),
                "normal",
            )

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save the washed image:\n{e}")


def select_language():
    """Show a small language selection window before launching the app."""
    selected_lang = "en"

    def set_lang(lang):
        nonlocal selected_lang
        selected_lang = lang
        lang_window.destroy()

    lang_window = tk.Tk()
    lang_window.title("Language Selection")

    tk.Label(
        lang_window,
        text="\nChoose Language / 言語を選択してください\n",
        padx=20,
    ).pack()

    tk.Button(
        lang_window,
        text="English (LGTM Mode)",
        width=24,
        command=lambda: set_lang("en"),
    ).pack(pady=5)

    tk.Button(
        lang_window,
        text="日本語 (ヨシッ！モード)",
        width=24,
        command=lambda: set_lang("jp"),
    ).pack(pady=5)

    lang_window.mainloop()
    return selected_lang


if __name__ == "__main__":
    choice = select_language()
    root = TkinterDnD.Tk()
    app = GhostWasher(root, choice)
    root.mainloop()
```
