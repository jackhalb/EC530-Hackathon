# this is second computer

import socket
import sys
import threading

SOURCE_IP = "10.0.0.219"
DEST_IP = "10.0.0.22"
DEST_PORT = 50001
SEND_PORT = 50002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SOURCE_IP, SEND_PORT))

print("punching a hole")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SOURCE_IP, SEND_PORT))
sock.sendto(b'0', (DEST_IP, DEST_PORT))

def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((SOURCE_IP, SEND_PORT))

    while True:
        data = sock.recv(1024)
        print('\rpeer: {}\n> '.format(data.decode()))

listener = threading.Thread(target=listen);
listener.start()

print("beginning message transmission")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SOURCE_IP, DEST_PORT))

while True:
    msg = input('> ')
    sock.sendto(msg.encode(), (DEST_IP, SEND_PORT))