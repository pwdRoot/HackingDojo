# Desafio HackingDojo

![alt text](https://becodoexploit.com/HackingDojo/img/logo.png)

### TODAS AS TAREFAS REALIZADAS NO DESAFIO:
#### https://becodoexploit.com/HackingDojo/

## Anotações e Observações

### Task 1:
- Código simples de conexão com a porta 445 (Como pede o desafio) para se conectar ao Servidor;
- Esse código ja envia uma mensagem para o Servidor que está sendo executado no Kali Linux;

### Task 2:
- Código configurado para receber qualquer conexão com a porta 445;
- Inseri um "Try/except" para resolver a mensagem de erro que dava quando eu parava a execução com "CTRL + C" (Não é obrigatório usar).;

### Task 3:
- Tentei pegar somente o IP que a função Socket coletava, contudo não obtive sucesso, então decidi remover todos os caracteres que não fazem parte do IP com o código abaixo:
```python
clientIP = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str(client)).group()
```
- Foi substituido os caracteres "." para "-", com o objetivo de seguir o que o desafio pede e para evitar problemas no nome do arquivo de log:
```python
clientIpReplace = clientIP.replace(".", "-")
```

### Task 4:
- Através da pesquisa identifiquei que todos os dados de login ficam armazenados no arquivo "Login Data.db"
- Acessei o arquivo .db usando sqlite3.
- Para automatizar o acesso ao arquivo com as credenciais, inseri o comando "os.path.expanduser('~')", que adiciona o caminho raiz do computador que está executando o script (Exemplo: "C:\Users\fulano")
- Tive dificuldade para interpretar o caracter "\" sem dar erro, então través de uma pesquisa vi que é possível usar o caraceter "\\" para que o Python reconheça o caminho inteiro.
- Foi adicionado um For para apresentar de forma organizada as credenciais, conforme pede o desafio.

### Taks 5:
- Pesquisei varias formas de enviar as credencias, pois o password estava dando erro ao enviar, por ter caraceteres que não são permitidos via "send" do Socket.
- Decidi usar o método simples e mais "feio" kkkkkk: o famoso converter em String a senha e mandar tudo em uma só variavel unica encodada em UTF-8.
```python
msgT = ("\nUrl: " + url + "\nUser: " + username + "\nPassword: " + str(password) + "\n")
```
- Ainda estou tentando resolver o problema do servidor mostrar a primeira credencial com 2 linhas depois e as outras com espaçamento certo.
- Pensei em usar Json para enviar as credencias via Socket para o servidor, porém decidi implementar com mais calma nas próximas tarefas.
