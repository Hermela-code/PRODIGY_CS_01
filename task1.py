def encrypt(string):
    result = ""
    for i in string:
        asci = ord(i) + key
        character = chr(asci)
        result += character
    return result


def key():
	enc_key= key + key
	dec_key=enc_key - key






def decrypt(string):
    result = ""
    for i in string:
        asci = ord(i) - dec_key
        character = chr(asci)
        result += character
    return result

print("Welcome to the Caesar Cipher")
print("1. Encrypt")
print("2. Decrypt")
choice = input("Enter 1 or 2: ")
key=int(input("Enter a key"))
if choice == "1":
    string = input("Enter the string you want to encrypt: ")
    print("Encrypted:", encrypt(string))
    print("Here is you key", enc_key)
elif choice == "2":
    string = input("Enter the string you want to decrypt: ")
    print("Decrypted:", decrypt(string))
   
else:
    print("Invalid choice.")

