# Ghost Washer 👻🧼

**A bilingual privacy shield that "physically" washes image metadata via pixel reconstruction.**
*Safety check with Japanese "Yoshi!" style or Global "LGTM" style.*

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Privacy-Protected-red.svg)

## 📖 Overview
**Ghost Washer** is a powerful image sanitization tool designed to protect you from OSINT (Open Source Intelligence) investigations and accidental data leaks on social media.

Unlike standard tools that simply delete metadata tags, Ghost Washer **reconstructs the image pixel-by-pixel onto a new canvas**. This process physically isolates and discards all invisible data, including Exif, GPS coordinates, and proprietary "MakerNotes".

It provides a visual and psychological "Safety Check" before you post.

---

## 🔰 How to Use
**No complex operations required. Just 4 steps to get "LGTM!"**

1.  **Launch**
    * Run the app and select your mode:
        * **English**: "LGTM Mode" (Global standard)
        * **Japanese**: "Yoshi! Mode" (Genba Neko style)
2.  **Drop**
    * Drag & drop your photos into the window. (Supports multiple files!)
    * The app automatically scans for hidden "danger" signals.
3.  **Wash**
    * If metadata is detected, a warning appears. Click "Yes" to wash.
    * A clean file with the suffix `_washed` will be saved in the same folder.
4.  **Verify (LGTM!)**
    * **Drop the `_washed` file again** to double-check.
    * When you see **"No information found. LGTM! 👉😸✨"**, it is 100% safe to post.

---

## 🔧 Technical Mechanism
**※ For developers and privacy enthusiasts:**

Ghost Washer ensures a "Zero-Footprint" result through a **Physical Reconstruction Process**, rather than just editing binary tags.

1.  **Pixel Extraction**
    * Extracts only the raw RGB color data from the source image using `Image.open()`.
2.  **New Canvas Creation**
    * Generates a completely fresh canvas (`Image.new`) in memory that has never held metadata.
3.  **Physical Redraw**
    * Transcribes the extracted pixel data one by one onto the new canvas (`putdata`).
4.  **Total Isolation**
    * This guarantees that **Exif**, **GPS**, and stubborn **MakerNotes** (hidden manufacturer data) are physically impossible to inherit.

> [!NOTE]
> **Image Quality**: Since the pixel values (colors) are transferred directly, there is no visible degradation in quality. Your memories remain beautiful, but your digital footprint vanishes.

---

## 🛠️ Requirements & Installation

* Python 3.x
* [Pillow](https://python-pillow.org/)
* [tkinterdnd2](https://github.com/pmgagne/tkinterdnd2)

```bash
# 1. Clone the repository
git clone [https://github.com/jshutoh-byte/GhostWasher.git](https://github.com/jshutoh-byte/GhostWasher.git)
cd GhostWasher

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python ghost_washer.py
