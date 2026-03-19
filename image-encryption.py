import argparse
from pathlib import Path

def xor_byte(data:bytes,key:bytes)->bytes:
    if not key:
        raise ValueError("Key must not be empty")
    key_length=len(key)
    return bytes(byte^key[index%key_length] for index,byte in enumerate(data))

def process_image(input_path:Path,output_path:Path,key:str)->None:
    data=input_path.read_bytes()
    transformed=xor_byte(data,key.encode("utf-8"))
    output_path.write_bytes(transformed)

def main()->None:
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
    if args.mode=="encrypt":
        output_path=input_path.with_suffix(".pfp")
    else:
        output_path=input_path.with_suffix(".png")

    if not input_path.is_file():
        raise FileNotFoundError("Please enter the correct path")
    
    process_image(input_path,output_path,args.key)
    print(f"{args.mode}ed file written to: {output_path}")

if __name__=="__main__":
    main() 