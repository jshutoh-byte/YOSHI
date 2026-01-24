import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ExifTags
from tkinterdnd2 import DND_FILES, TkinterDnD
import os

class GhostWasher:
    def __init__(self, root, lang='jp'):
        self.root = root
        self.lang = lang
        self.root.title(f"Ghost Washer v2.6 - {'International' if lang=='en' else 'グローバル版'}")
        self.root.geometry("550x600")

        # 言語設定のリソース
        self.res = {
            'jp': {
                'label': "\n画像をドロップしてください（連続対応）",
                'wait': "待機中... 😸 (Standby)",
                'scan': "スキャン開始: ",
                'clean': "\n【判定】\n情報は見つかりませんでした。\n\n何一つ残っていません。ヨシッ！ 👉😸✨",
                'danger': "⚠️ 以下のメタデータ（足跡）を検出しました：",
                'confirm_title': "現場確認",
                'confirm_msg': "画像に「{}件」の情報が埋め込まれています。\nこれらを完全に洗浄しますか？",
                'washed_title': "洗浄完了しました！ ✨",
                'washed_info': "【保存情報】\n元のファイル名に「_washed」を付与して保存しました。\n\nファイル名: {}\n保存場所: {}\n\nこのファイルを再度ドロップして最終確認してください。",
                'tags': {
                    'DateTime': '撮影日時', 'Make': 'メーカー', 'Model': 'カメラ機種名',
                    'Software': '使用ソフト', 'GPSInfo': '位置情報(GPS)'
                }
            },
            'en': {
                'label': "\nDrop images here (Multiple supported)",
                'wait': "Waiting... 😸 (Standby)",
                'scan': "Scan Started: ",
                'clean': "\n[Result]\nNo information found.\n\nTotally clean. LGTM! (Looks Good To Me) 👉😸✨",
                'danger': "⚠️ Metadata (Footprints) Detected:",
                'confirm_title': "Confirmation",
                'confirm_msg': "Found {} items embedded.\nDo you want to wash them completely?",
                'washed_title': "Wash Complete! ✨",
                'washed_info': "[Saved Info]\nAppended '_washed' to the filename.\n\nFilename: {}\nPath: {}\n\nDrop the new file again for final verification.",
                'tags': {} # 英語の場合はそのまま表示
            }
        }[lang]

        # フォント設定
        self.jp_font_family = ("Meiryo", "MS UI Gothic", "Yu Gothic", "sans-serif")
        self.normal_font = (self.jp_font_family[0], 10)
        self.log_font = ("Consolas", 10)
        self.yoshi_font = ("MS Gothic", 12, "bold")

        self.label = tk.Label(root, text=self.res['label'], pady=10, font=self.normal_font)
        self.label.pack()

        self.info_area = scrolledtext.ScrolledText(root, height=20, width=65, font=self.log_font)
        self.info_area.pack(padx=10, pady=10)
        self.info_area.tag_configure("jp_normal", font=self.normal_font)
        self.info_area.tag_configure("yoshi", foreground="green", font=self.yoshi_font)
        self.info_area.tag_configure("danger", foreground="red", font=(self.jp_font_family[0], 10, "bold"))

        self.clear_info_area(self.res['wait'])
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.handle_drop)

    def clear_info_area(self, msg):
        self.info_area.delete('1.0', tk.END)
        self.info_area.insert(tk.END, f"{msg}\n", "jp_normal")
        self.info_area.insert(tk.END, "-"*60 + "\n")

    def handle_drop(self, event):
        files = self.root.tk.splitlist(event.data)
        for file_path in files:
            self.process_file(file_path.strip('{}'))

    def process_file(self, file_path):
        self.clear_info_area(f"{self.res['scan']}{os.path.basename(file_path)}")
        try:
            img = Image.open(file_path)
            exif = img._getexif()
            if not exif:
                self.info_area.insert(tk.END, self.res['clean'], "yoshi")
                return
            
            self.info_area.insert(tk.END, f"{self.res['danger']}\n\n", "danger")
            for tag_id, value in exif.items():
                tag_en = ExifTags.TAGS.get(tag_id, tag_id)
                tag_disp = self.res['tags'].get(tag_en, tag_en) if self.lang == 'jp' else tag_en
                self.info_area.insert(tk.END, f" ・{tag_disp}: {value}\n", "jp_normal")

            if messagebox.askyesno(self.res['confirm_title'], self.res['confirm_msg'].format(len(exif))):
                self.wash_process(img, file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Fail: {e}")

    def wash_process(self, img, file_path):
        clean_img = Image.new(img.mode, img.size)
        clean_img.putdata(list(img.getdata()))
        base, ext = os.path.splitext(file_path)
        new_filename = f"{os.path.basename(base)}_washed{ext}"
        new_path = os.path.join(os.path.dirname(file_path), new_filename)
        clean_img.save(new_path)
        
        self.clear_info_area(self.res['washed_title'])
        self.info_area.insert(tk.END, self.res['washed_info'].format(new_filename, os.path.dirname(file_path)), "jp_normal")

def select_language():
    def set_lang(l):
        nonlocal selected_lang
        selected_lang = l
        lang_window.destroy()

    selected_lang = 'en'
    lang_window = tk.Tk()
    lang_window.title("Language Selection")
    tk.Label(lang_window, text="\nChoose Language / 言語を選択してください\n", padx=20).pack()
    tk.Button(lang_window, text="English (LGTM Mode)", width=20, command=lambda: set_lang('en')).pack(pady=5)
    tk.Button(lang_window, text="日本語 (ヨシッ！モード)", width=20, command=lambda: set_lang('jp')).pack(pady=5)
    lang_window.mainloop()
    return selected_lang

if __name__ == "__main__":
    choice = select_language()
    root = TkinterDnD.Tk()
    app = GhostWasher(root, choice)
    root.mainloop()