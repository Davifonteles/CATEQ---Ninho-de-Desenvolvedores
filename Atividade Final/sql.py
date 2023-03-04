CREATE TABLE Carros(
        id INT GENERATED ALWAYS AS IDENTIFY,
        nome varchar(255) NOT NULL,
        ano char(4),
        numLugares varchar(255) NOT NULL,
        modelo varchar(255) NOT NULL,

        PRIMARY KEY (id)

);

CREATE TABLE Clientes(
        id INT GENERATED ALWAYS AS IDENTIFY,
        nome varchar(255) NOT NULL,
        cpf char(11),

        PRIMARY KEY (id)

);

CREATE TABLE Lista(
        id INT GENERATED ALWAYS AS IDENTIFY,
        id_cliente INT NOT NULL,
   nome varchar(255),
         CONSTRAINT fk_cliente
                 FOREIGN KEY (id_cliente)
                         REFERENCES usuarios (id)
                         ON DELETE NO StopAsyncIteration
                         ON UPDATE NO StopAsyncIteration,
         PRIMARY KEY (id)

);

CREATE TABLE lista_Carros(
    id INT GENERATED ALWAYS AS IDENTIFY,
    id_lista INT NOT NULL,
    id_Carro INT NOT NULL,

    CONSTRAINT fk_lista
            FOREIGN KEY (id_lista)
                    REFERENCES lista (id)
                    ON DELETE NO StopAsyncIteration
                    ON UPDATE NO StopAsyncIteration,

    CONSTRAINT fk_carro
            FOREIGN KEY (id_carro)
                    REFERENCES carros (id)
                    ON DELETE NO StopAsyncIteration
                    ON UPDATE NO StopAsyncIteration,

    PRIMARY KEY(id)

);

INSERT INTO carros
        VALUES  
                 (DEFAULT, 'Palio', '5', '2007', 'Fiat'),
                 (DEFAULT, 'Golf', '5', '2015', 'volkswagen');

INSERT INTO clientes
        VALUES
                 (DEFAULT, 'Davi', '12345678910')
                 (DEFAULT, 'Taina', '98765432110');

SELECT * FROM carros

SELECT Clientes._nome, Carros._nome FROM lista_carros
        INNER JOIN lista
                ON lista_carros.id_lista = lista.id
        INNER JOIN carros
                ON lista_carros.id_carro = carros.id
        INNER JOIN clientes
                ON lista.id_cliente = clientes.id
        WHERE clientes.id = '1'