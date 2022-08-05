#!/bin/python3

import socket
import sys
import logging
import re
import time
from termcolor import colored

#Criando uma conexao TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Permitindo reusar o endereco e a porta
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Comecando conexao na porta 445
s.bind(('', 445))
s.listen(5)

#Tratando a mensagem de erro quando sai do programa (CTRL + C)
try:
	while True:
		print("Aguardando conexao do cliente...\n")
		con, client = s.accept()
		print("---------------------------------")
		print('Conectado por ->', str(client))
		while True:
			msg = con.recv(1024)
			if not msg: break
			
			msgd = msg.decode()
			print(colored(msgd, 'green'))
			print("---------------------------------\n")
			print(msgd.lower())
			if 'dojo' in msgd.lower():
				clientIP = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str(client)).group()
				clientIpReplace = clientIP.replace(".", "-")
				with open('./log-' + time.strftime("%Y%m%d-%H%M%S") + '-' + clientIpReplace + '.txt', 'w') as f:
					f.write(msgd)
		con.close()
except KeyboardInterrupt:
    sys.exit(0)
