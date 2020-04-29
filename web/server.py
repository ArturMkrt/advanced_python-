import socket
import datetime
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', 5555))
    sock.listen(1)
    conn, addr = sock.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if data == b'exit':
                break
            elif data == b'day':
                conn.sendall((str(datetime.datetime.now().day).encode()))
            elif data == b'month':
                conn.sendall((str(datetime.datetime.now().month).encode()))
            elif data == b'year':
                conn.sendall((str(datetime.datetime.now().year).encode()))
            elif data == b'time':
                conn.sendall(((datetime.datetime.now().time().strftime('%H:%M')).encode()))
            else:
                conn.sendall(b'Unrecognized command '+data)
