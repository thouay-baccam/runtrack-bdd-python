/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
DROP TABLE IF EXISTS employe;
CREATE TABLE `employe` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `salaire` decimal(10,2) NOT NULL,
  `id_service` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_service` (`id_service`),
  CONSTRAINT `employe_ibfk_1` FOREIGN KEY (`id_service`) REFERENCES `service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS service;
CREATE TABLE `service` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO employe(id,nom,prenom,salaire,id_service) VALUES('1','\'Baccam\'','\'Teddy\'','3200.00','1'),('2','\'Baccam\'','\'Théo\'','2900.00','2'),('3','\'Attias\'','\'Raphael\'','3050.00','3');
INSERT INTO service(id,nom) VALUES('1','\'Cybersecurité\''),('2','\'Web Dev\''),('3','\'Fullstack Dev\'');