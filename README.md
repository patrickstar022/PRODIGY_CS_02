
# PRODIGY_CS_02

## Features
- Image encryption and decryption using pixel manipulation
- XOR-based cipher implementation
- File I/O for image processing
- Simple and intuitive command-line interface

## How It Works
The application encrypts images by manipulating pixel values using XOR operations with a secret key. Each pixel's RGB values are transformed, making the image unreadable without the correct decryption key.

## Installation
```bash
git clone <repository-url>
cd PRODIGY_CS_02
pip install -r requirements.txt
```

## Usage
```bash
python image_encryptor.py --encrypt input.png key output_encrypted.png
python image_encryptor.py --decrypt output_encrypted.png key output_decrypted.png
```

## Example
```bash
python image_encryptor.py --encrypt photo.jpg mykey123 photo_encrypted.png
python image_encryptor.py --decrypt photo_encrypted.png mykey123 photo_restored.jpg
```

## Knowledge Gained
- XOR cipher fundamentals and cryptography basics
- Image processing with Python (PIL/Pillow)
- File handling and binary data manipulation
- Command-line argument parsing
- Encryption/decryption algorithm implementation
