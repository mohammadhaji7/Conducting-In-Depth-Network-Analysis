import socket
from datetime import datetime
from cryptography.fernet import Fernet

# ===============================
# Load Encryption Key
# ===============================
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# ===============================
# Server Configuration
# ===============================
HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("=" * 60)
print("        Secure Communication Server")
print("=" * 60)
print(f"Listening on : {HOST}:{PORT}")
print(f"Started At   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("Cipher       : Fernet (Authenticated Symmetric Encryption)")
print("=" * 60)

try:
    while True:

        print("\nWaiting for client connection...\n")

        conn, addr = server.accept()

        print("=" * 60)
        print("Client Connected")
        print("=" * 60)
        print(f"Client IP    : {addr[0]}")
        print(f"Client Port  : {addr[1]}")
        print(f"Timestamp    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        encrypted_message = conn.recv(4096)

        print("=" * 60)
        print("Encrypted Payload")
        print("=" * 60)
        print(encrypted_message.decode())

        decrypted_message = cipher.decrypt(encrypted_message)

        print("\n" + "=" * 60)
        print("Decrypted Message")
        print("=" * 60)
        print(decrypted_message.decode())

        conn.close()

        print("\nConnection closed.")
        print("-" * 60)

except KeyboardInterrupt:

    print("\n\nShutting down server...")

finally:

    server.close()