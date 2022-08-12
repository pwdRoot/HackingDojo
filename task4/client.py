import sqlite3
import os

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
    print("Url:", url)
    print("User:", username)
    print("Password:", password, "\n")

# finalizando a conexão com o arquivo
con.close()
