#!/bin/bash

# Select encryption method using fzf
encryption_method=$(echo -e "Shift Cipher\nA1Z26 Cipher" | fzf --reverse --prompt="Select encryption method: " --height=10 --border)

# Check if user chose Shift Cipher or A1Z26 Cipher
if [[ "$encryption_method" == "Shift Cipher" ]]; then
    # Ask for text and shift value
    echo "You chose Shift Cipher."
    read -p "Enter text to encrypt/decrypt: " text
    read -p "Enter shift value: " shift_value

    # Call the Python script for Shift Cipher encryption/decryption
    echo "Encrypting text..."
    encrypted_text=$(python3 a1z26_cipher.py --encrypt "$text" --shift "$shift_value")
    echo "Encrypted Text: $encrypted_text"
    
    # Call Python script for decryption
    echo "Decrypting text..."
    decrypted_text=$(python3 a1z26_cipher.py --decrypt "$encrypted_text" --shift "$shift_value")
    echo "Decrypted Text: $decrypted_text"
    
elif [[ "$encryption_method" == "A1Z26 Cipher" ]]; then
    # Ask for text to encrypt
    echo "You chose A1Z26 Cipher."
    read -p "Enter text to encrypt: " text

    # Call the Python script for A1Z26 encryption
    encrypted_output=$(python3 a1z26_cipher.py --a1z26-encrypt "$text")
    encrypted_numbers=$(echo "$encrypted_output" | sed 's/Encrypted (A1Z26): //')
    echo "Encrypted Text (A1Z26): $encrypted_numbers"

    # Ask if user wants to generate an image
    read -p "Do you want to generate an image with the encrypted text? (y/n): " generate_image
    if [[ "$generate_image" == "y" || "$generate_image" == "Y" ]]; then
        python3 a1z26_cipher.py --a1z26-encrypt "$text" --generate-image
        echo "Image generated and saved in generated_images/ folder."
    else
        # Call Python script for decryption
        echo "Decrypted Text (A1Z26): $(python3 a1z26_cipher.py --a1z26-decrypt "$encrypted_numbers" | sed 's/Decrypted (A1Z26): //')"
    fi
else
    echo "Invalid selection"
fi
