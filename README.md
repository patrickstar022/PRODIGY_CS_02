
# PRODIGY_CS_02

## Features
- Image encryption and decryption using pixel manipulation
- Two encryption methods: pixel swapping and mathematical operations
- File I/O for image processing
- Simple and intuitive command-line interface

## How It Works
The application encrypts images by manipulating pixel values using two methods: swapping adjacent pixels horizontally or applying a mathematical transformation (adding 37 modulo 256). Decryption reverses these operations to restore the original image.

## Installation
```bash
git clone <repository-url>
cd PRODIGY_CS_02
pip install -r requirements.txt
```

## Usage
```bash
python image-encryption.py encrypt input.png output_encrypted.png --method {swap|math}
python image-encryption.py decrypt output_encrypted.png output_decrypted.png --method {swap|math}
```

## Example
```bash
python image-encryption.py encrypt photo.jpg photo_encrypted.png --method math
python image-encryption.py decrypt photo_encrypted.png photo_restored.jpg --method math
```

## Knowledge Gained
- Pixel manipulation techniques in image processing
- Image processing with Python (PIL/Pillow and NumPy)
- File handling and binary data manipulation
- Command-line argument parsing with argparse
- Basic encryption/decryption algorithm implementation
