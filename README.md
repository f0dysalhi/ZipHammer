# ZipHammer

ZipHammer is a Python script designed to brute-force zip file passwords using a wordlist. It allows users to specify the path to the zip file and the wordlist containing potential passwords. The tool attempts to crack the zip file password by trying each password in the wordlist until successful.
Usage

   Ensure you have Python installed on your system.

   Clone or download the ZipHammer repository.

   Open a terminal or command prompt and navigate to the directory containing the ZipHammer script.

  Run the script using the following command:

   ```bash
    python3 ZipHammer.py
   ```


   Follow the prompts to enter the path to the zip file and the wordlist.

  Optionally, specify the number of threads to use for parallel processing.
    Wait for the tool to finish attempting to crack the zip file password.
    If successful, the password will be displayed. Otherwise, a message indicating that all passwords were incorrect will be shown.

Requirements

    Python 3.x
    zipfile module

Disclaimer

This tool is intended for educational and legal use only. Do not use it for illegal purposes or against files that you do not have permission to access.
