import time
import hashlib

true_username = "admin"
true_password_hash = "dda69783f28fdf6f1c5a83e8400f2472e9300887d1dffffe12a07b92a3d0aa25"      #"securepassword123"

wrong_attempts = {}
max_attempts = 5

def entrance_verification(username, password):

    time.sleep(0.1) # Simulate processing delay

    if username in wrong_attempts and wrong_attempts[username] >= max_attempts:
        print("Too many wrong attempts. Access denied.")
        return "Locked"
    

    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    if username == true_username and password_hash == true_password_hash:
        if username in wrong_attempts:
            del wrong_attempts[username]  # Reset wrong attempts on successful login
        return "Successful login"
    else:
        wrong_attempts[username] = wrong_attempts.get(username, 0) + 1
        print("Incorrect username or password.")
        return "Failed login"
    

def brute_force_attack(username, word_list):
    attempts = 0
    start_time = time.time()

    print(f"Target user: {username}")
    print(f"Starting brute-force attack using word list: {word_list}")
    print("-" * 40)

    try:
        with open(word_list, 'r', encoding='utf-8') as file:
            for line in file:
                password = line.strip()
                if not password:
                    continue  # Skip empty lines
                
                attempts += 1

                result = entrance_verification(username, password)

                # Simulate the entrance verification process
                if result == "Successful login":
                    end_time = time.time()
                    print(f"Password found: {password}")
                    print(f"Total attempts: {attempts}")
                    print(f"Time taken: {end_time - start_time:.2f} seconds")
                    return True
                elif result == "Locked":
                    print("Account locked due to too many failed attempts.")
                    return False
                else:
                    print(f"Attempt {attempts}: Tried password '{password}' - Failed")
                
    except FileNotFoundError:
        print(f"Word list file '{word_list}' not found.")
        return False
    
    print("Brute-force attack failed. Password not found in the word list.")
    return False

if __name__ == "__main__":

    print("----Brute-Force Attack Simulator----")

    user_to_attack = "admin"
    word_list_file = "word_list.txt"  # Ensure this file exists with potential passwords

    brute_force_attack(user_to_attack, word_list_file)
