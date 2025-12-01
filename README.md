# 🛡️ Brute-Force Attack Simulator

This project is a simple Python application that simulates a brute-force attack against a login system.
It includes password verification, failed-attempt tracking, account lockout, and wordlist-based brute-force functionality.

## 🚀 Features

✔️ SHA-256–based password verification

✔️ Failed login attempt limit (max_attempts)

✔️ Automatic account lockout

✔️ Brute-force attack using a wordlist

✔️ Reports attempt count and elapsed time

## 🛠️ Setup and Execution

Prerequisites

Python 3.x is required to run this simulation. There are no other library dependencies (time and hashlib are included in the Python standard library).

Steps:

  - Download the auth_simulator.py (or your main file's name) file from this repository.

  - In the same directory, create a file named word_list.txt containing potential passwords to be tested.

  - Example word_list.txt content:

        123456
        password
        securepassword123  # The correct password
        qwerty
        ...

  - Run the script using your terminal/command prompt:

        python auth_simulator.py

## 📝 Code Overview
🔑 entrance_verification(username, password)

- Performs SHA-256 hash comparison

- Tracks incorrect login attempts

- Locks the account after exceeding max_attempts

🔍 brute_force_attack(username, word_list)

- Iterates through each password in the wordlist

- Stops when the correct password is found

- Halts if the account becomes locked


## ⚠️ Legal Disclaimer

This project is intended for educational and research purposes only. Performing brute-force attacks on systems without explicit permission is illegal. The author is not responsible for any misuse of this code.

    
