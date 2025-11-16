# a1z26_cipher.py

import argparse
import string

# Mapping A to 1, B to 2, ..., Z to 26
alphabet = string.ascii_uppercase

# Function for Shift Cipher (already existing)
def shift_letter(letter, shift):
    if letter in alphabet:
        index = alphabet.index(letter)
        shifted_index = (index + shift) % 26
        return alphabet[shifted_index]
    else:
        return letter

def encrypt(plaintext, shift):
    return ''.join(shift_letter(char, shift) for char in plaintext.upper())

def decrypt(ciphertext, shift):
    return ''.join(shift_letter(char, -shift) for char in ciphertext.upper())

# New functions for A1Z26 encryption
def a1z26_encrypt(plaintext):
    return ' '.join(str(ord(char) - ord('A') + 1) if char.isalpha() else char for char in plaintext.upper())

def a1z26_decrypt(ciphertext):
    numbers = ciphertext.split()
    return ''.join(chr(int(num) + ord('A') - 1) if num.isdigit() else num for num in numbers)

# # Helper function to validate input (only A-Z and spaces allowed)
# def validate_input(text):
#     if not all(c.isalpha() or c.isspace() for c in text):
#         raise ValueError("Input text must only contain letters and spaces.")

def main():
    parser = argparse.ArgumentParser(description="A1Z26 Cipher Tool")
    parser.add_argument('--encrypt', type=str, help="Text to encrypt")
    parser.add_argument('--decrypt', type=str, help="Text to decrypt")
    parser.add_argument('--shift', type=int, help="Shift value for encryption/decryption")
    parser.add_argument('--a1z26-encrypt', type=str, help="Text to encrypt using A1Z26")
    parser.add_argument('--a1z26-decrypt', type=str, help="Text to decrypt using A1Z26")
    
    args = parser.parse_args()

    if args.encrypt and args.shift is not None:
        print(f"Encrypted: {encrypt(args.encrypt, args.shift)}")
    elif args.decrypt and args.shift is not None:
        print(f"Decrypted: {decrypt(args.decrypt, args.shift)}")
    elif args.a1z26_encrypt:
        print(f"Encrypted (A1Z26): {a1z26_encrypt(args.a1z26_encrypt)}")
    elif args.a1z26_decrypt:
        print(f"Decrypted (A1Z26): {a1z26_decrypt(args.a1z26_decrypt)}")
    else:
        print("Invalid arguments")

if __name__ == "__main__":
    main()