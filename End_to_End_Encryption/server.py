import socket
from datetime import datetime
from cryptography.fernet import Fernet

# Load encryption key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("=" * 60)
print("      Secure Communication Server")
print("=" * 60)
print(f"Listening on : {HOST}:{PORT}")
print(f"Started At   : {datetime.now()}")
print("Cipher       : Fernet (Authenticated Symmetric Encryption)")
print("=" * 60)
print("\nWaiting for client connection...\n")

conn, addr = server.accept()

print("=" * 60)
print("Client Connected")
print("=" * 60)
print(f"Client IP    : {addr[0]}")
print(f"Client Port  : {addr[1]}")
print(f"Timestamp    : {datetime.now()}")
print()

encrypted_message = conn.recv(4096)

print("=" * 60)
print("Encrypted Payload")
print("=" * 60)
print(encrypted_message.decode())
print()

decrypted_message = cipher.decrypt(encrypted_message)

print("=" * 60)
print("Decrypted Message")
print("=" * 60)
print(decrypted_message.decode())
print()

print("=" * 60)
print("Connection Closed")
print("=" * 60)

conn.close()
server.close()