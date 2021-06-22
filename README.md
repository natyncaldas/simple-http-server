# Simple HTTP Server using Sockets
>Tarefa prática da disciplina Redes I (CK0249) 2021.1 da Universidade Federal do Ceará (UFC)

>Python 3 + HTML

## Introdução
### Sobre
Servidor Web simples em Python capaz de processar apenas uma requisição. Cria um socket de conexão quando contatado por um cliente (navegador). O servidor, então:
 - Recebe e analisa a requisição HTTP dessa conexão; 
 - Determina o arquivo específico sendo requisitado; 
 - Obtêm o arquivo requisitado do sistema de arquivo do servidor;
 -    Cria uma mensagem de resposta HTTP consistindo no arquivo requisitado precedido por um *header*; 
	 - Envia a resposta pela conexão TCP ao navegador requisitante. 
	 
### Autenticação
Não requer autenticação

### Códigos de Erro
```http
Status Code: 404 Not Found
 ```
Ocorre quando o cliente solicita um arquivo inexistente no servidor.
```http
Status Code: 415 Unsupported Media Type
 ```
 Ocorre quando o cliente solicita um arquivo com uma codificação diferente de UTF-8

## Instruções de instalação
### Requerimentos

 - [ ] Python 3.8+
 
 Execute o comando a seguir para instalar o módulo de sockets para Python
 ```sh
 python3 -m pip install socket
 ```
 Posteriormente, execute o seguinte comando para iniciar o servidor
 
  ```sh
 python3 WebServer.py
 ```
Por último, acesse o servidor pelo navegador: `http://localhost:8000/`

## Funcionamento

### Cliente
|Método HTTP| Path  | Resposta do Servidor | Sucesso | Erro 
|--|--|--|--|--|
| `GET` | / | [1.a] |  200 | n/a | 
| `GET` | /{path-do-arquivo} | [1.b]  | 200 | 404 [1.c] 415 [1.d] |

|1.a| 1.b |
|--|--|
| ![1.a](https://i.imgur.com/d8e78ZP.png) | ![1.b](https://i.imgur.com/zcsVJuB.png)|

|1.c| 1.d |
|--|--|
| ![1.c](https://i.imgur.com/QIVfmpd.png) | ![1.d](https://i.imgur.com/skEyCVW.png)|

### Servidor
![server](https://i.imgur.com/cjdFVaf.png)


