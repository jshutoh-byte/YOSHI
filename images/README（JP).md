# Ghost Washer 👻🧼

**画像のメタデータ（Exif）をピクセル再構成によって「物理的に」洗浄するプライバシー保護ツール。**
*現場猫流「ヨシッ！」と、エンジニア流「LGTM」で安全確認。*

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Privacy-Protected-red.svg)

## 📖 概要 (Overview)
**Ghost Washer** は、SNS投稿時の「特定」リスクから身を守るために開発された、強力な画像洗浄ツールです。

一般的な削除ツールとは異なり、このアプリはメタデータ領域を単に削除するのではなく、**画像データをピクセル単位で新しいキャンバスに描き直す（Reconstruction）** ことで、Exif、GPS情報、メーカー固有の不可視領域（MakerNotes）などを物理的に断ち切ります。

特定班の解析から逃れたい方、デジタルタトゥーを残したくない方に「ヨシッ！」という確実な安心を提供します。

## ✨ 特徴 (Features)

* **🌍 現場確認モード（バイリンガル対応）**
    * **日本語モード**: 現場猫リスペクトの **「ヨシッ！ (Yoshi!)」** 表示で、直感的に安全確認が可能。
    * **英語モード**: グローバルエンジニア向けの **「LGTM (Looks Good To Me)」** 表示に対応。
* **🛡️ 完全洗浄 (Binary Pixel Wash)**
    * `Image.new` + `putdata` による画像の再構成処理を行い、メタデータの継承をゼロにします。
* **🚀 高速ワークフロー**
    * ドラッグ＆ドロップで連続処理が可能。大量の「現場写真」もサクサク洗浄できます。
* **👁️ 可視化と確認**
    * 埋め込まれている情報を隠さずリスト表示。「何が消されたか」を確認してから洗浄できます。
    * 洗浄後のファイルを再度ドロップすることで、本当に空っぽになったかダブルチェックが可能。

## 🛠️ 動作環境 (Requirements)

* Python 3.x
* [Pillow](https://python-pillow.org/) (画像処理ライブラリ)
* [tkinterdnd2](https://github.com/pmgagne/tkinterdnd2) (D&Dサポート)

## 📦 インストールと使い方

1.  **リポジトリのクローン**
    ```bash
    git clone [https://github.com/jshutoh-byte/GhostWasher.git](https://github.com/jshutoh-byte/GhostWasher.git)
    cd GhostWasher
    ```

2.  **依存ライブラリのインストール**
    ```bash
    pip install -r requirements.txt
    ```

3.  **アプリの起動**
    ```bash
    python ghost_washer.py
    ```
    *(起動時に「日本語（ヨシッ！モード）」か「English (LGTM Mode)」を選択してください)*

## 🖼️ 仕組み (How it Works)

1.  **スキャン**: 画像をドロップすると、埋め込まれている全てのメタデータ（撮影日時、GPS、使用ソフト等）を解析して表示します。
2.  **洗浄（Wash）**: 確認ダイアログで「はい」を押すと、ピクセルデータのみを抽出・再描画し、メタデータを持たない新しい画像を生成します。
3.  **保存**: `_washed` という接尾辞をつけて保存します。
4.  **最終確認**: 生成されたファイルを再度アプリにドロップし、**「ヨシッ！」** が表示されれば洗浄完了です。

## 📝 ライセンス

本プロジェクトは MIT License の下で公開されています。詳細は [LICENSE](LICENSE) をご覧ください。

---

<div align="center">
  <p>To be is TOBE.</p>
  <p>© 2026 J. Shuto (<a href="https://github.com/jshutoh-byte">@jshutoh-byte</a>)</p>
</div>