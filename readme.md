
# MEOW RANSOMWARE

## Disclaimer

This project is designed strictly for educational purposes to demonstrate file encryption techniques and understand cybersecurity measures. **It is not intended for illegal use.** Misuse of this tool violates ethical standards and may contravene local, state, and federal laws. By using this software, you agree to use it in a manner that is legal, ethical, and in accordance with all applicable regulations and laws. The creators of this tool assume no responsibility for misuse or damages caused by this software.

## Overview

This project is a demonstration of how file encryption works, simulating a basic version of what is commonly known as ransomware. It's a tool meant to encrypt files in a specified directory, changing their access until decrypted. The primary goal here is to educate about encryption algorithms, their application, and the importance of cybersecurity.

## Features

- Encryption of files in a target directory
- Utilization of a strong encryption standard (Fernet, part of the cryptography library)
- Simulated behavior of file-targeting malware for educational purposes

## Installation

1. Ensure you have Python installed on your machine.
2. Install the required packages using pip:

```bash
pip install cryptography
```

3. Clone this repository or download the project files to your local machine.

## Usage

1. **Important**: Only run this script in a safe, controlled environment, such as a virtual machine or a dedicated test directory. Do not run this script on any critical system or personal files.
2. Modify the `directory_path` in the script to point to the directory containing the files you wish to encrypt.
3. Run the script:

```bash
python encrypt_script.py
```

4. To decrypt the files, a decryption script with the appropriate key is required. Ensure you have a backup of your files and the encryption key stored securely.

## Contribution

Contributions to this project should focus on enhancing its educational value, improving security features, and developing defensive strategies against malware. Please ensure that all contributions adhere to ethical guidelines and legal standards.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This project is for educational purposes only.
- Special thanks to the cybersecurity community for their ongoing efforts to educate and protect against digital threats.
