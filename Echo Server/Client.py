import socket

HOST = "127.0.0.1"
PORT = 56428

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        text = input("Enter input text to be sent : ")
        if text.lower() == "exit":
            break
        s.sendall(text.encode())
        s.sendall(text.encode())
        data = s.recv(1024)
        print(f"Received {data!r}")
