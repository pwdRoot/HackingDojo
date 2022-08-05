#!/usr/bin/python3

import socket

dest = ('192.168.0.91', 445)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(dest)
print("Iniciando conexão na porta 445\n")
print("--------------------------------\n")
msg = "Hacking Dojo"
msgEncode = msg.encode("utf-8")
s.send(msgEncode)
s.close()
