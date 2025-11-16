# a1z26_cipher.py

import argparse
import string
from PIL import Image, ImageDraw, ImageFont
import numpy as np

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

# Function to generate an image with encrypted text
def generate_image_with_text(text, output_path="generated_images/encrypted_text.png"):
    # Create a blank white image
    width, height = 1200, 600  # Larger image for bigger text
    image = Image.new("RGB", (width, height), color=(255, 255, 255))  # White background
    
    # Initialize drawing context
    draw = ImageDraw.Draw(image)
    
    # Define font and size (make sure you have a font available, or specify a path to one)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 120)  # Use system font with larger size
    except IOError:
        try:
            font = ImageFont.truetype("DejaVuSans.ttf", 120)  # Fallback to another path
        except IOError:
            font = ImageFont.load_default()  # Use default if no truetype fonts are found

    # Set text position (centered)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((width - text_width) // 2, (height - text_height) // 2)

    # Draw the text on the image
    draw.text(position, text, fill=(0, 0, 0), font=font)  # Black text

    # Add noise to the image
    noisy_image = add_noise_to_image(image)

    # Save the image
    noisy_image.save(output_path)
    print(f"Image saved to {output_path}")

# Function to add noise to an image (salt-and-pepper noise)
def add_noise_to_image(image):
    # Convert to NumPy array for pixel manipulation
    np_image = np.array(image)

    # Add random noise (salt-and-pepper noise) - 5% density
    noise_mask = np.random.rand(*np_image.shape[:2]) < 0.05
    np_image[noise_mask] = 0  # Set noisy pixels to black

    # Convert back to image
    noisy_image = Image.fromarray(np_image)
    return noisy_image

def main():
    parser = argparse.ArgumentParser(description="A1Z26 Cipher Tool")
    parser.add_argument('--encrypt', type=str, help="Text to encrypt")
    parser.add_argument('--decrypt', type=str, help="Text to decrypt")
    parser.add_argument('--shift', type=int, help="Shift value for encryption/decryption")
    parser.add_argument('--a1z26-encrypt', type=str, help="Text to encrypt using A1Z26")
    parser.add_argument('--a1z26-decrypt', type=str, help="Text to decrypt using A1Z26")
    parser.add_argument('--generate-image', action='store_true', help="Generate an image with encrypted text")
    
    args = parser.parse_args()

    # Process encryption and decryption based on arguments
    if args.encrypt and args.shift is not None:
        print(f"Encrypted: {encrypt(args.encrypt, args.shift)}")
    elif args.decrypt and args.shift is not None:
        print(f"Decrypted: {decrypt(args.decrypt, args.shift)}")
    elif args.a1z26_encrypt:
        encrypted_text = a1z26_encrypt(args.a1z26_encrypt)
        print(f"Encrypted (A1Z26): {encrypted_text}")
        # If the user wants to generate an image
        if args.generate_image:
            generate_image_with_text(encrypted_text)
    elif args.a1z26_decrypt:
        print(f"Decrypted (A1Z26): {a1z26_decrypt(args.a1z26_decrypt)}")
    else:
        print("Invalid arguments")

if __name__ == "__main__":
    main()
