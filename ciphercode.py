# CALMA, Eugene Marie S.
# BSCPE_1-4
# OOP Laboratory Exercise Number 2 Problem 3 (The Vigenère Cipher)

# input and inserting your acount name
account_name = input("\n\33[33mHi, Good day! Please enter your name.\33[0m ")
# data protection policy
while True:
    user_input = input("\n\33[1m In compliance with the Data Privacy Act of 2012 and its Implementing Rules and Regulations, we execute reasonable and appropriate security measures for the protection of personal data that we collect. Please type \33[32mYes\33[0m\33[1m if you want to continue, otherwise, type \033[31mNo\033[0m\33[1m if you want to terminate this process.\33[0m ")
    if user_input.lower() == 'yes':
        # input your message and key
        print("\n\33[35mWelcome to The Vigenère Cipher, where your code is always protected!\33[35m")
        message = input("\33[1mPlease enter your message.\33[1m ").upper().replace(" ", "")
        keyword = input("\33[1mPlease enter your key.\33[1m ").upper().replace(" ", "")
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
        print(f"\n\33[37mHi {account_name}! Here is your ciphertext: {cipher_text}")
                # ask user if he still want to input another message
        askyesno = input("\n\33[36mDo you still want to continue? (yes/no):\33[0m ")
        if askyesno.lower() == 'no':
            print("\33[41mTerminating Program... ")
            exit()
    elif user_input.lower() == 'no':
        print("\33[41mTerminating Program...\33[41m ")
        exit()
    else:
        print('Type yes/no')