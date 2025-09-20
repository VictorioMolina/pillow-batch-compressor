# Pillow batch compressor

A lightweight Python tool for batch image compression and resizing using [Pillow](https://python-pillow.org).  
Recursively compresses `.jpg`, `.jpeg`, and `.png` images in a folder, with customizable quality, scale factor, and optional overwrite.

## Features
- Batch process all images in a directory
- Supports `.jpg`, `.jpeg`, `.png`
- Customizable quality and scale factor
- Option to overwrite originals or save as new files
- Minimal dependencies (`Pillow`)

## Installation

Clone the repository and install requirements:

```bash
git clone https://github.com/<your-username>/pillow-batch-compressor.git
cd pillow-batch-compressor
pip install -r requirements.txt
```

## Usage

```bash
python3 compressor.py <images_dir> <quality> <scale_factor> <should_replace>
```
