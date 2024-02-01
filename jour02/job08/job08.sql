CREATE DATABASE zoo;

USE zoo;

CREATE TABLE cage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    superficie FLOAT NOT NULL,  
    capacite_max INT NOT NULL
);

CREATE TABLE animal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    race VARCHAR(255) NOT NULL,
    id_cage INT,
    date_naissance DATE NOT NULL,
    pays_origine VARCHAR(255) NOT NULL
);