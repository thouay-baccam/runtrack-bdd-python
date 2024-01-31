
CREATE DATABASE IF NOT EXISTS lethalcompany;
USE lethalcompany;

CREATE TABLE IF NOT EXISTS employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    salaire DECIMAL(10, 2) NOT NULL,
    id_service INT,
);

CREATE TABLE IF NOT EXISTS service (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

INSERT INTO service (nom) VALUES ('Cybersecurité'), ('Web Dev'), ('Fullstack Dev');

INSERT INTO employe (nom, prenom, salaire, id_service) VALUES 
('Baccam', 'Teddy', 3200.00, (SELECT id FROM service WHERE nom = 'Cybersecurité')),
('Baccam', 'Théo', 2900.00, (SELECT id FROM service WHERE nom = 'Web Dev')),
('Attias', 'Raphael', 3050.00, (SELECT id FROM service WHERE nom = 'Fullstack Dev'));
