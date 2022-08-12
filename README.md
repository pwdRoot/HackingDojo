# Desafio HackingDojo

<div>
  <a href="https://github.com/pwdRoot"></a>
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=pwdRoot&layout=compact&langs_count=7&theme=dracula"/>
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=pwdRoot&show_icons=true&theme=dracula&include_all_commits=true&count_private=true"/>
</div>


### Todas as tarefas do desafio Hacking Dojo
#### Desafio: https://becodoexploit.com/HackingDojo/

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
- Foi adicionado um For para apresentar de forma organizada as credenciais, conforme pede o desafio.

### Taks 5:
- Em execução...
