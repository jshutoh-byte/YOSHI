# Ghost Washer 👻🧼

**A bilingual (JP/EN) privacy shield that "washes" image metadata by reconstructing pixels.** *デジタル足跡を完全消去。現場猫流「ヨシッ！」と、エンジニア流「LGTM」で安全を確認。*

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Privacy-Protected-red.svg)

## 📖 Overview
**Ghost Washer** is a GUI tool designed for privacy-conscious users who want to share photos without leaking sensitive metadata (Exif, GPS, Camera Model, etc.).

Unlike standard tools that simply delete tags, Ghost Washer **reconstructs the image pixel-by-pixel** onto a new canvas. This ensures that no hidden metadata or manufacturer-specific "MakerNotes" are carried over.

## ✨ Features

* **🌍 Bilingual Interface (Multi-language Support)**
    * **JP Mode**: Features the "Genba Neko" style safety check: **"ヨシッ！ (Yoshi!)"**
    * **EN Mode**: Features the global engineer standard: **"LGTM (Looks Good To Me)"**
* **🛡️ Binary Pixel Wash**
    * Physically reconstructs the image (`Image.new` + `putdata`) to ensure a zero-footprint file.
* **🚀 High-Speed Workflow**
    * Simple Drag & Drop interface.
    * Continuous processing support.
* **👁️ Visual Safety Check**
    * Scans and displays hidden metadata before deletion.
    * Verifies the "washed" file to guarantee it is 100% clean.

## 🛠️ Requirements

* Python 3.x
* [Pillow](https://python-pillow.org/) (Image processing)
* [tkinterdnd2](https://github.com/pmgagne/tkinterdnd2) (Drag & Drop support)

## 📦 Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/jshutoh-byte/GhostWasher.git](https://github.com/jshutoh-byte/GhostWasher.git)
    cd GhostWasher
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application**
    ```bash
    python ghost_washer.py
    ```
    *(Note: Select your preferred language/mode at startup.)*

## 🖼️ How it Works

1.  **Scan**: The tool reads the uploaded image using `Pillow` and lists any detected Exif/Metadata.
2.  **Wash**: If confirmed, it extracts the raw pixel data and paints it onto a fresh, metadata-free canvas.
3.  **Save**: The clean image is saved with a `_washed` suffix.
4.  **Verify**: Dropping the `_washed` file again will result in a **"Yoshi! / LGTM!"** confirmation, proving the file is empty of metadata.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <p>To be is TOBE.</p>
  <p>© 2026 J. Shuto (<a href="https://github.com/jshutoh-byte">@jshutoh-byte</a>)</p>
</div>