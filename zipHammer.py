import zipfile
import os
import threading

print("""
             _                                                
 ___(_)_ __ | |__   __ _ _ __ ___  _ __ ___   ___ _ __ 
|_  / | '_ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 / /| | |_) | | | | (_| | | | | | | | | | | |  __/ |   
/___|_| .__/|_| |_|\__,_|_| |_| |_|_| |_| |_|\___|_|   
      |_|     s0misalhi                                          
       
      """)

def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        return True
    except Exception as e:
        return False

def brute_force(zip_file_path, wordlist_path, threads):
    with zipfile.ZipFile(zip_file_path) as zip_file:
        with open(wordlist_path, 'r') as wordlist_file:
            passwords = wordlist_file.readlines()
            for password in passwords:
                password = password.strip()
                if extract_zip(zip_file, password):
                    print(f"The Password Successfully cracked: {password}")
                    return
    print("All passwords are wrong.")

def main():
    while True:
        zip_file_path = input("Enter the path to the zip file: ")
        wordlist_path = input("Enter the path to the wordlist file: ")
        threads = input("Enter the number of threads: ")
        
        if not os.path.exists(zip_file_path) or not os.path.exists(wordlist_path):
            print("Invalid file paths. Please try again.")
            continue
        
        brute_force(zip_file_path, wordlist_path, threads)

        again = input("Do you want to try again? (yes/no): ")
        if again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
