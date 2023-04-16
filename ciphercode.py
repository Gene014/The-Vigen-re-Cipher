# CALMA, Eugene Marie S.
# BSCPE_1-4
# OOP Laboratory Exercise Number 2 Problem 3 (The Vigenère Cipher)

# input and inserting your acount name
account_name = input("Hi, Good day! Please enter your name.")
# data protection policy
while True:
    user_input = input("In compliance with the Data Privacy Act of 2012 and its Implementing Rules and Regulations, we execute reasonable and appropriate security measures for the protection of personal data that we collect. Please type Yes if you want to continue, otherwise, type No if you want to terminate this process.")
    if user_input.lower() == 'yes':
        # input your message and key
        print("Welcome to The Vigenère Cipher, where your code is always protected!")
        message = input("Please enter your message. ").upper().replace(" ", "")
        keyword = input("Please enter your key. ").upper().replace(" ", "")
        # generates key from keyword, extends the key until reached length of string
        key = list(keyword)
        if len(message) == len(key):
            continue
        else:
            for i in range(len(message) - len(key)):
                key.append(key[i % len(key)])
        "" . join(key)
                # tranlates the generated key to integers
        key = [ord(i) - 65 for i in key]
                # encrypts the integers
        cipher_text = ""
        for i in range(len(message)):
            encrypted_num = (ord(message[i]) - 65 + key[i % len(key)]) % 26
            cipher_text += chr(encrypted_num + 65)
                # output the cipher text
        print(f"Hi {account_name}! Here is your ciphertext: {cipher_text}")
                # ask user if he still want to input another message
        askyesno = input("Do you still want to continue? (yes/no): ")
        if askyesno.lower() == 'no':
            print("Terminating Program...")..
            exit()
    elif user_input.lower() == 'no':
        print("Terminating Program...")
        exit()
    else:
        print('Type yes/no')