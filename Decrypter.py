
message = []

def decrypt(encryption, key):
    for i in encryption:
        letter_ascii = ord(i)
        decrypted_letter = letter_ascii - key
        other_letter = chr(decrypted_letter)
        message.append(other_letter)
        decrypted_text = convert(message)

    print("-" * 60)
    print(f"[+] encrypted message: [{encryption}]")
    print(f"[+] key: [{key}]")
    print(f"[+] message: [{decrypted_text}]")

def convert(string):
    decrypted_text = ""
    for x in message:
        decrypted_text += x
    return decrypted_text

x = input("[+] enter encrypted message: ")
y = input("[+] enter key: ")

decrypt(str(x), int(y))