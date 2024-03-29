import socket

HOST = "0.0.0.0"  # Host for Server
PORT = 56428 # Port for Server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                print("data received : {d}".format(d=data))
                if not data:
                    continue
                elif data.decode().lower() == "end":
                    break
                conn.sendall(data)
