#!/usr/bin/env python

import socket

def getData():
	data, addr = sock.recvfrom(1024)
	return data

UDP_IP = "0.0.0.0"
UDP_PORT = 3641

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(0.01)
