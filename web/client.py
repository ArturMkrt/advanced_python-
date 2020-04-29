import socket
import datetime
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect(('127.0.0.1',5555))
    while True:
        word = input('Send Command ')
        client.sendall(word.encode())
        if word == 'exit':
            break
        data = client.recv(1024)
        print(data.decode())
