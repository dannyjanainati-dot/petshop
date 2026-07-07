-- CRIANDO O BANCO DE DADOS PETSHOP --
CREATE DATABASE Petshop
USE Petshop;

-- CRIANDO A TABELA ESPÉCIES --
CREATE TABLE especies (
id INT  AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50)
);

-- CRIANDO A TABELA PETS --
CREATE TABLE pets (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR (80),
raca VARCHAR (80),
idade INT,
nome_dono VARCHAR (100),
especie_id INT, FOREIGN KEY ( especie_id) REFERENCES especies (id)
);

-- POPULANDO A TABELA ESPÉCIES --
INSERT INTO especies (id,nome) VALUES (1,'cachorro');
INSERT INTO especies (id,nome) VALUES (2,'gato');
INSERT INTO especies (id,nome) VALUES (3,'passaro');
INSERT INTO especies (id,nome) VALUES (4,'roedor');

-- POPULANDO A TABELA PETS --
INSERT INTO pets (nome,raca,idade,nome_dono,especie_id) VALUES
('Rex', 'Labrador', 3, "Carlos Silva", 1),     -- Cachorro do Carlos
('Mimi', 'Siamês', 2, "Ana Souza", 2),        -- Gato da Ana
('Loro', 'Calopsita', 1, "João Pereira", 3),   -- Pássaro do João
('Thor', 'Poodle', 5, "Maria Santos", 4),      -- Cachorro da Maria
('Frajola', 'Persa', 4, "Pedro Lima", 2),      -- Gato do Pedro
('Bidu', 'Hamster', 1, "Júlia Costa",4);      -- Roedor da Júlia
