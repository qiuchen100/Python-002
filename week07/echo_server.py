#!/usr/bin/env python
import socket

HOST = 'localhost'
PORT = 10000

is_exit = False


def echo_server():
    global is_exit
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    # 只接收1个连接
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if data.decode('utf-8') == 'exit':
                is_exit = True
                conn.sendall(b'bye!')
                break
            print(f'recieve from {addr}, data: {data}')
            conn.sendall(data)
        conn.close()
        if is_exit is True:
            print('exit!')
            break
    s.close()


if __name__ == "__main__":
    echo_server()
