# YOSHI! (Ghost Washer) 🐈✨ 👉😸

**Is your photo safe to share? — Wash away hidden image metadata before posting.**
**写真を共有する前に、Exif・GPSなどの見えないメタデータを洗浄するためのツールです。**

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Privacy](https://img.shields.io/badge/Privacy-Metadata%20Cleaning-red.svg)
![Bilingual](https://img.shields.io/badge/Language-English%20%2F%20Japanese-brightgreen.svg)

---

## 📖 Overview

**YOSHI! (Ghost Washer)** is a small bilingual privacy helper for people who share images online and want to reduce the risk of leaking metadata such as Exif, GPS information, embedded thumbnails, and camera-specific MakerNotes.

Unlike simple metadata tag editors, YOSHI rebuilds the visible image data onto a new canvas and saves it as a fresh file. This design helps separate the shared image from common embedded metadata while keeping the workflow simple enough for non-experts.

YOSHI is especially useful for creators, developers, field workers, bloggers, and SNS users who want a quick **“LGTM / ヨシッ!”** check before publishing images.

> **Important:** YOSHI helps remove embedded metadata, but it cannot guarantee anonymity. It cannot remove identifying information that is visibly present in the image itself, such as signs, reflections, backgrounds, uniforms, faces, locations, or other contextual clues.

---

## 📖 概要

**YOSHI! (Ghost Washer)** は、画像をSNSやブログに投稿する前に、Exif・GPS・MakerNotes などのメタデータ漏えいリスクを減らすための、日英対応の軽量プライバシーツールです。

単にメタデータタグを編集するだけではなく、画像の表示ピクセルを新しいキャンバスへ再構成して保存することで、一般的な埋め込みメタデータを切り離すことを目指しています。

非エンジニアでも使いやすいように、ドラッグ＆ドロップ中心のシンプルな確認フローを重視しています。

> **注意:** YOSHI は埋め込みメタデータの削減を支援するツールです。画像内に写り込んだ看板、反射、背景、制服、顔、地形、投稿文脈など、見た目そのものから分かる情報は削除できません。

---

## ✨ Features

### 🌍 Bilingual interface

YOSHI supports both English and Japanese safety messages.

* **English:** `LGTM! 👉😸✨`
* **Japanese:** `ヨシッ！ 👉😸✨`

### 🛡️ Pixel reconstruction wash

YOSHI rebuilds the visible pixel data onto a new canvas and saves it as a fresh image file.

This helps remove common embedded metadata such as:

* Exif
* GPS information
* embedded thumbnails
* camera-specific MakerNotes
* common metadata fields supported by the tool

### 🚀 Simple “YOSHI!” workflow

The workflow is designed to be quick and easy:

1. Drop an image into the tool.
2. Check detected metadata.
3. Wash the image.
4. Save the cleaned file with a `_washed` suffix.
5. Drop the cleaned file again to verify supported metadata fields.

### 👁️ Verification-friendly design

After washing an image, you can drop the output file back into YOSHI to check whether supported metadata fields remain.

When the cat says **“LGTM!”**, it means YOSHI did not detect supported metadata in the output file.

### 🖥️ Local-first tool

YOSHI is designed as a local desktop tool.
Your images do not need to be uploaded to an external web service in order to be washed.

---

## 🖼️ How it works

YOSHI follows a simple four-step process.

### 1. Scan

YOSHI checks the dropped image for supported metadata fields.

### 2. Wash

YOSHI extracts the visible pixel data and reconstructs it onto a new image canvas.

### 3. Save

YOSHI saves the cleaned image as a new file with a `_washed` suffix.

### 4. Verify

You can drop the cleaned file back into YOSHI to confirm whether supported metadata remains.

---

## ✅ What YOSHI can help with

YOSHI can help reduce the risk of accidentally sharing hidden metadata, including:

* location information stored in Exif GPS fields
* camera or device information
* embedded thumbnails
* common metadata blocks
* accidental metadata leakage when sharing field photos or SNS images

---

## ⚠️ What YOSHI cannot guarantee

YOSHI is not a complete anonymity tool.

It cannot remove or protect against:

* signs, buildings, landmarks, license plates, reflections, faces, or other visible clues
* information written in the image itself
* file names or folder names chosen by the user
* metadata added later by another application or platform
* image fingerprinting, watermarking, steganography, or advanced forensic analysis
* privacy risks from the surrounding post text, account history, upload time, or social context

Always review the image visually before sharing.

---

## 🛠️ Installation

Clone or download this repository, then install the required Python packages.

```bash
git clone https://github.com/jshutoh-byte/YOSHI.git
cd YOSHI
```

Install dependencies as needed for your environment.

```bash
pip install pillow
```

If your version uses drag-and-drop support through an additional package, install it as well.

```bash
pip install tkinterdnd2
```

Then run the application script in this repository.

```bash
python yoshi.py
```

> If the script name is different in your local copy, replace `yoshi.py` with the actual file name.

---

## 🚀 Usage

1. Launch YOSHI.
2. Drag and drop an image file into the window.
3. Review the detected metadata.
4. Click the wash button.
5. Save the `_washed` output file.
6. Drop the output file back into YOSHI to verify the result.
7. Share only after visually checking the image itself.

---

## 🧪 Supported formats

YOSHI is built on Python image-processing libraries and is intended for common image formats such as JPEG and PNG.

Metadata behavior may differ depending on file format, encoder, and source application.
For privacy-sensitive use, always verify the generated output file before sharing.

---

## 🗺️ Roadmap

Planned improvements include:

* clearer metadata report view
* packaged Windows release
* improved error messages for non-technical users
* additional verification checks
* English and Japanese documentation improvements
* automated tests for common image formats
* optional command-line mode

---

## 🤝 Contributing

Issues and pull requests are welcome.

Good first contributions include:

* improving documentation
* testing image formats
* reporting metadata that was not detected
* improving Japanese or English wording
* packaging support for Windows
* UI improvements for non-technical users

---

## 🔐 Privacy philosophy

YOSHI is built around a simple idea:

> Before sharing an image, users should have an easy way to ask:
> **“Is this safe enough to post?”**

YOSHI does not replace careful judgment, but it helps make hidden metadata easier to notice, remove, and verify.

---

## 📄 License

This project is released under the MIT License.

See [LICENSE](LICENSE) for details.

---

<div align="center">
  <p><strong>To be is TOBE.</strong></p>
  <p>Wash the footprints. Keep the pixels. Share with care.</p>
  <p>© 2026 J. Shuto (@jshutoh-byte)</p>
</div>
