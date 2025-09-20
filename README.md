# Pillow batch compressor

A lightweight Python tool for batch image compression and resizing using [Pillow](https://python-pillow.org).  
Recursively compresses `.jpg`, `.jpeg`, and `.png` images in a folder, with customizable quality, scale factor, and optional overwrite.

## Features
- Batch process all images in a directory
- Supports `.jpg`, `.jpeg`, `.png`
- Customizable quality and scale factor
- Option to overwrite originals or save as new files
- Minimal dependencies (`Pillow`)

## Usage

```bash
python3 compressor.py <images_dir> <quality> <scale_factor> <should_replace>
```
