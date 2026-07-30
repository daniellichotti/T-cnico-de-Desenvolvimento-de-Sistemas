## Instalar Marquina:
`wsl --install`

## Atualizar sistema:
`sudo apt update`

## Instalar o sqlite3 na WSL:
`sudo apt install sqlite3 -y`

## Criar um banco:
`sqlite3 meubanco.db`

## Criando uma tabela de usuários
```
CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE
); 
```

## Inserindo alguns Registros
```
INSERT INTO usuarios (nome, email) VALUES ('Gustavo Erthal', 'gustavinhodolol67@hotmail.com');
INSERT INTO usuarios (nome, email) VALUES ('Gabriel Borgath', 'gabizinho_cliente_do_claudio@hotmail.com');
```

## Lendo os registros de uma tabela
```
SELECT * FROM USUARIOS;
```

## Ler um registro específico
```
SELECT * FROM USUARIOS WHERE email='moisesinho_de_campos@hotmail.com';
```

## Comandos úteis
```
.mode table - Deixa bonitinho
.tables - Lista tabelas
.databases - Lista o banco
.quit ou .exit - sair
```