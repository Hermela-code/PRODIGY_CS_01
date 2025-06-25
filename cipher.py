def encrypt(string, key):
    result = ""
    for i in string:
        asci = ord(i) + key
        character = chr(asci)
        result += character
    return result

def decrypt(string, key):
    result = ""
    for i in string:
        asci = ord(i) - key
        character = chr(asci)
        result += character
    return result

print("Welcome to the Caesar Cipher")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter 1 or 2: ")

if choice == "1":
    string = input("Enter the string you want to encrypt: ")
    key = int(input("Enter a secret key (number you’ll remember): "))
    encrypted = encrypt(string, key)
    print("Encrypted message:", encrypted)

elif choice == "2":
    string = input("Enter the string you want to decrypt: ")
    key = int(input("Enter the secret key used for encryption: "))
    decrypted = decrypt(string, key)
    print("Decrypted message:", decrypted)

else:
    print("Invalid choice.")

