from pathlib import Path
import argparse
from PIL import Image
import numpy as np

def encrypt_image(input_path:Path, output_path:Path, method:str):
    image = Image.open(input_path).convert("RGB")
    image_array = np.array(image).astype("uint16")

    if method == "swap":
        encrypted_pixels = swap_pixels(image_array)
    elif method == "math":
        encrypted_pixels = math_operation("encrypt",image_array)
    else:
        raise ValueError("Choose 'swap' or 'math' as method.")

    Image.fromarray(encrypted_pixels.astype("uint8"), "RGB").save(output_path)
    print(f"✅ Encryption successful! Saved to: {output_path}")

def decrypt_image(input_path:Path, output_path:Path, method:str):
    image = Image.open(input_path).convert("RGB")
    image_array = np.array(image).astype("uint16")

    if method == "swap":
        decrypted_pixels = swap_pixels(image_array)
    elif method == "math":
        decrypted_pixels = math_operation("decrypt",image_array)
    else:
        raise ValueError("Choose 'swap' or 'math' as method.")

    Image.fromarray(decrypted_pixels.astype("uint8"), "RGB").save(output_path)
    print(f"🔓 Decryption successful! Saved to: {output_path}")


def swap_pixels(image_array: np.ndarray) -> np.ndarray:
    swapped = image_array.copy()
    rows, cols, _ = image_array.shape
    for i in range(rows):
        for j in range(0, cols - 1, 2):
            swapped[i, j], swapped[i, j + 1] = (
                swapped[i, j + 1],
                swapped[i, j],
            )
    return swapped

def math_operation(mode:str,image_array: np.ndarray) -> np.ndarray:
    if(mode=="encrypt"):
        result=(image_array + 37) % 256
    else:
        result=(image_array - 37) % 256
    return result


def main():
    parser = argparse.ArgumentParser(description="🖼️Image Encryption/Decryption Tool")
    parser.add_argument("mode",choices=["encrypt", "decrypt"],help="Choose to encrypt or decrypt an image.",)
    parser.add_argument("input", help="Path to the image file.")
    parser.add_argument("output", help="Path to save the output")
    parser.add_argument("--method",choices=["swap", "math"],help="Choose encryption method: 'swap' or 'math'.",)

    args = parser.parse_args()

    print("🔐 Processing...")
    if args.mode == "encrypt":
        encrypt_image(args.input, args.output, args.method)
    else:
        decrypt_image(args.input, args.output, args.method)


if __name__ == "__main__":
    main()