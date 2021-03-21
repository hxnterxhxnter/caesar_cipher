
cipher = []

def encrypt(message, key):
    for i in message:
        letter_ascii = ord(i)
        ciphered_letter = letter_ascii + key
        other_letter = chr(ciphered_letter)
        cipher.append(other_letter)
        new_message = convert(cipher)

    print("-" * 60)
    print(f"[+] message: [{message}]")
    print(f"[+] key: [{key}]")
    print(f"[+] encrypted message: [{new_message}]")

def convert(string):
    encrypted_message = ""
    for x in cipher:
        encrypted_message += x
    return encrypted_message

x = input("[+] enter message: ")
y = input("[+] enter key: ")

encrypt(str(x), int(y))