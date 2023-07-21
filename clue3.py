import RPi.GPIO as GPIO
import time
import socket
import subprocess


TCP_IP = '192.168.254.11'
TCP_PORT = 5612
BUFFER_SIZE = 1024



MESSAGE7 = b"Clue3"


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))





s.send(MESSAGE7)
time.sleep(1)

