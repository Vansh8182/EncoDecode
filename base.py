"""
Base64 / Base32 Encoder-Decoder
A simple CLI tool to encode and decode text using Base64 and Base32.
"""

import base64

# ---------- Encoding Section ----------

def encode_text64():
    text = input("Encode text: ")
    encode = base64.b64encode(text.encode()).decode()
    print(f"Encoded: {encode}")
    return encode


def encode_text32():
    text = input("Encode text: ")
    encode = base64.b32encode(text.encode()).decode()
    print(f"Encoded: {encode}")
    return encode

# ---------- decoding Section ----------

def decode_txet64():
    text = input("Decode text: ")
    try:
        decode = base64.b64decode(text).decode()
        print(f"Decode: {decode}")
        return decode
    except Exception:
        print("Invalid string ")


def decode_text32():
     text = input("Decode text: ")
     try:
         decode = base64.b32decode(text).decode
         print(f"Decode: {decode}")
         return decode
     except Exception:
         print("Invalid string")

# ---------- Main Menu ----------

def main():
        print("\n=== Encoede ==")
        print("1. Encode64")
        print("2. Encode32")
        print("\n=== Decode ==")
        print("3. Decode64")
        print("4. Decode32")

        choice = input("Enter Number: ")
    
        if choice == "1":
            encode_text64()
        elif choice == "2":
            encode_text32()
        elif choice == "3":
            decode_txet64()
        elif choice == "4":
            decode_text32()
        else:
            print("Worng choise")

if __name__ == "__main__":
    main()