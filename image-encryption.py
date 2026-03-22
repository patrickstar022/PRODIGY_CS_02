from pathlib import Path
import argparse
from PIL import Image
import numpy as np


def encrypt(input_path:Path,output_path:Path,key:int):
    img=Image.open(input_path)
    img_arr=np.array(img, dtype=np.int16)
    encrypted_arr=(img_arr+key)%256
    encrypted_img=Image.fromarray(encrypted_arr.astype("uint8"))
    encrypted_img.save(output_path)

def decrypt(input_path:Path,output_path:Path,key:int):
    img=Image.open(input_path)
    img_arr=np.array(img, dtype=np.int16)
    decrypted_arr=(img_arr-key)%256
    decrypted_img=Image.fromarray(decrypted_arr.astype("uint8"))
    decrypted_img.save(output_path)


parser=argparse.ArgumentParser(
        description="Encrypt or Decrypt an image"
    )
parser.add_argument(
        "mode",
        choices=["encrypt","decrypt"],
        help="Operation to perform. Please choose one option",
    )
parser.add_argument(
        "input",
        help="Input path of the image"
    )
parser.add_argument(
        "key",
        help="A key used to encrypt/decrypt"
    )
args=parser.parse_args()

input_path=Path(args.input)
if not input_path.is_file():
    raise FileNotFoundError("Please enter the correct path")

try:
    key=int(args.key)
except ValueError:
    raise ValueError("Key must be an integer")

if args.mode=="encrypt":
    output_path=input_path.with_name("encrypted.png")
    encrypt(input_path,output_path,key)

else:
    output_path=input_path.with_name("decrypted.png")
    decrypt(input_path,output_path,key)
    
print(f"{args.mode}ed file as {str(output_path)}")