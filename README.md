# a1z26-cipher-tool
This project implements a basic encryption and decryption tool supporting both Shift Cipher and A1Z26 Cipher algorithms. The A1Z26 algorithm maps letters to numbers (A = 1, B = 2, ..., Z = 26). Additionally, it includes image generation functionality for encrypted text using Pillow.

## Features:
- **Shift Cipher**: Encrypt and decrypt text with a specified shift value.
- **A1Z26 Cipher**: Encrypt and decrypt text by converting letters to their corresponding numbers.
- **Image Generation**: Generate images containing the encrypted text with added noise for visualization.
- **Interactive Shell Script**: Use `encryption_tool.sh` for an interactive menu to choose encryption methods and options.

## Usage:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/a1z26-cipher-tool.git
   cd a1z26-cipher-tool

2. Install dependencies:
   ```bash
   pip install pillow numpy

3. Run the Python script directly:
   ```bash
   # For Shift Cipher
   python3 a1z26_cipher.py --encrypt "HELLO" --shift 3
   python3 a1z26_cipher.py --decrypt "KHOOR" --shift 3

   # For A1Z26 Cipher
   python3 a1z26_cipher.py --a1z26-encrypt "HELLO"
   python3 a1z26_cipher.py --a1z26-decrypt "8 5 12 12 15"

   # Generate image with encrypted text
   python3 a1z26_cipher.py --a1z26-encrypt "HELLO" --generate-image

4. Or use the interactive shell script:
   ```bash
   ./encryption_tool.sh
   ```
   Follow the prompts to select encryption method and options.

## Requirements:
- Python 3.x
- Pillow (PIL)
- NumPy
- fzf (for the shell script)

## Notes:
- Generated images are saved in the `generated_images/` folder.
- The `.gitignore` file excludes the `generated_images/` folder from version control.
