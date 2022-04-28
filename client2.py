# this is second computer

import socket
import sys
import threading

DEST_IP = ""
DEST_PORT = 50001
SEND_PORT = 50002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', SEND_PORT))

print("punching a hole")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', SEND_PORT))
sock.sendto(b'0', (DEST_IP, DEST_PORT))

def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', SEND_PORT))

    while True:
        data = sock.recv(1024)
        print('\rpeer: {}\n> '.format(data.decode()), end='')

listener = threading.Thread(target=listen, daemon=True);
listener.start()

print("beginning message transmission")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', DEST_PORT))

while True:
    msg = input('> ')
    sock.sendto(msg.encode(), (DEST_IP, SEND_PORT))