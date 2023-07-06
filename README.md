# Desafio HackingDojo

![alt text](https://becodoexploit.com/HackingDojo/img/logo.png)

### TODAS AS TAREFAS REALIZADAS NO DESAFIO:
#### https://becodoexploit.com/HackingDojo/

## Ferramentas Usadas
- Pycharm (https://www.jetbrains.com/pt-br/pycharm/download/#section=windows): para programar em Windows e executar os Scripts.
- Mousepad (https://pkg.kali.org/pkg/mousepad): para editar os códigos em Python no Kali Linux.
- Python3 (https://www.kali.org/docs/general-use/python3-transition/): para executar os códigos em Python.
- Google: para pesquisar e estudar bastante.

## Anotações e Observações

### Task 1:
- Código simples de conexão com a porta 445 (Como pede o desafio) para se conectar ao Servidor;
- Esse código já envia uma mensagem para o Servidor que está sendo executado no Kali Linux;

### Task 2:
- Código configurado para receber qualquer conexão com a porta 445;
- Inseri um "Try/except" para resolver a mensagem de erro que dava quando eu parava a execução com "CTRL + C" (Não é obrigatório usar).;
- Coloquei o código abaixo para evitar que a porta 445 fique travada, ou seja, para liberar a porta para novas conexões de forma imediata:
```python
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

### Task 3:
- Tentei pegar somente o IP que a função Socket coletava, contudo, não obtive sucesso, então decidi remover todos os caracteres que não fazem parte do IP com o código abaixo:
```python
clientIP = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str(client)).group()
```
- Foi substituído os caracteres "." para "-", com o objetivo de seguir o que o desafio pede e para evitar problemas no nome do arquivo de log:
```python
clientIpReplace = clientIP.replace(".", "-")
```

### Task 4:
- Através da pesquisa identifiquei que todos os dados de login ficam armazenados no arquivo "Login Data.db"
- Acessei o arquivo ".db" usando sqlite3.
- Para automatizar o acesso ao arquivo com as credenciais, inseri o comando "os.path.expanduser('~')", que adiciona o caminho raiz do computador que está executando o script (Exemplo: "C:\Users\fulano")
- Tive dificuldade para interpretar o carácter "\" sem dar erro, então través de uma pesquisa vi que é possível usar o caracter "\\" para que o Python reconheça o caminho inteiro.
- Foi adicionado um For para apresentar de forma organizada as credenciais, conforme pede o desafio.

### Taks 5:
- Pesquisei várias formas de enviar as credências, pois o password estava dando erro ao enviar, por ter caracteres que não são permitidos via "send" do Socket.
- Decidi usar o método simples e mais "feio" kkkkkk: o famoso converter em String a senha e mandar tudo em uma só variável única encodada em UTF-8.
```python
msgT = ("\nUrl: " + url + "\nUser: " + username + "\nPassword: " + str(password) + "\n")
```
- Pensei em usar Json para enviar as credências via Socket para o servidor, porém decidi implementar com mais calma nas próximas tarefas.

### Task 6:
- Por algum motivo ele não estava salvando a primeira credencial no Log, então eu mudei o tamanho dos bytes de recebimento da conexão para 2048 e adicionei o comando "s.close" no final do Script da task 5.
- Além disso, removi o "If" que detectava a palavra "Dojo" na mensagem recebida pelo Client e arrumei a identação do código para não dar erro.

### Task 7:
- Sem informação.

### Task 8:
- Sem informação

---

### Task 9:
- Em execução...
