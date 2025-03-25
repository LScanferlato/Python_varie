from cryptography.fernet import Fernet
import sys

# Funzione per generare una chiave e salvarla in un file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Funzione per caricare la chiave dal file `secret.key`
def load_key():
    return open("secret.key", "rb").read()

# Funzione per criptare un file
def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

# Funzione per decriptare un file
def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(file_name, "wb") as dec_file:
        dec_file.write(decrypted)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python audiocrypt.py <encrypt/decrypt/key> <file_name>")
        sys.exit(1)

    action = sys.argv[1]
    file_name = sys.argv[2]

    if action == "encrypt":
        encrypt_file(file_name)
        print(f"{file_name} has been encrypted.")
    elif action == "decrypt":
        decrypt_file(file_name)
        print(f"{file_name} has been decrypted.")
    elif action == "key":
        generate_key()
        print("KEY has been decrypted.")
    else:
        print("Invalid action. Use encrypt or decrypt.")
