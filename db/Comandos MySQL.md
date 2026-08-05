CREATE DATABASE sistema_vendas;

USE sistema_vendas;

CREATE TABLE clientes(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_cadastro DATE DEFAULT (CURRENT_DATE)
);

ALTER TABLE clientes 
ADD COLUMN idade INT,
ADD COLUMN cidade VARCHAR(50),
ADD COLUMN condicao VARCHAR(20) DEFAULT 'ativo';

ALTER TABLE clientes MODIFY COLUMN nome VARCHAR(150) NOT NULL;

ALTER TABLE clientes MODIFY COLUMN cidade VARCHAR(50) NOT NULL;

ALTER TABLE clientes ADD CONSTRAINT chk_idade CHECK (idade>=18);

INSERT INTO clientes (nome, email, idade, cidade) VALUES ('Gustavo2', 'guga@hotmail.com', 10, 'Itaperuna');

INSERT INTO clientes (nome, email) VALUES ('Guilherme Vieira', 'guilherminho_da_night@hotmail.com');

INSERT INTO clientes (nome, email, idade, cidade) VALUES
('Ana Silva', 'ana.silva@email.com', 25, 'Rio de Janeiro'),
('Bruno Costa', 'bruno.costa@email.com', 31, 'São Paulo'),
('Carla Souza', 'carla.souza@email.com', 28, 'Belo Horizonte'),
('Diego Lima', 'diego.lima@email.com', 22, 'Curitiba'),
('Eduarda Martins', 'eduarda.martins@email.com', 35, 'Salvador'),
('Felipe Rocha', 'felipe.rocha@email.com', 27, 'Fortaleza'),
('Gabriela Alves', 'gabriela.alves@email.com', 24, 'Recife'),
('Henrique Santos', 'henrique.santos@email.com', 29, 'Brasília'),
('Isabela Ferreira', 'isabela.ferreira@email.com', 33, 'Campinas'),
('João Pedro', 'joao.pedro@email.com', 20, 'Niterói');

UPDATE clientes SET idade = 36, cidade = 'Itaperuna' WHERE id = 1;

ALTER TABLE clientes DROP COLUMN condicao;
ALTER TABLE clientes DROP CHECK chk_idade;

SELECT * FROM clientes;

SELECT * FROM clientes WHERE cidade = 'Rio de Janeiro' AND idade > 30;

-- ASC e DESC (Ascendente e Descendente)
SELECT nome, idade, cidade FROM clientes ORDER BY idade ASC;

SELECT DISTINCT idade FROM clientes;

DROP TABLE clientes;

DROP DATABASE sistema_vendas;