CREATE DATABASE  IF NOT EXISTS `db_alunos` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_alunos`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: db_alunos
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alunos excel`
--

DROP TABLE IF EXISTS `alunos excel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alunos excel` (
  `Nome` text,
  `ExperienciaProfissional` text,
  `DataNascimento` text,
  `Sexo` text,
  `GrauInstrucao` text,
  `RA` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos excel`
--

LOCK TABLES `alunos excel` WRITE;
/*!40000 ALTER TABLE `alunos excel` DISABLE KEYS */;
INSERT INTO `alunos excel` VALUES ('Alexandre Ferreira','Estagiário','10/10/2000','Masculino','Ensino Médio',22000001),('Ana Clara','Estagiária','01/01/2001','Feminino','Ensino Médio',22000002),('Angelo Jordăo','Estudante universitário','30/06/1999','Masculino','Ensino Médio',22000003),('Antônio Luiz','Năo tenho','12/12/1999','Masculino','Ensino Superior',22000004),('Bruno Rios','Programador Júnior','10/05/1999','Masculino','Ensino Médio',22000005),('Carlos Henrique','Analista Pleno ','08/02/1999','Masculino','Ensino Médio',22000006),('Daniel Cunha','Estudante','25/05/2001','Masculino','Ensino Superior',22000007),('Danilo Rebouças','Estagiário','20/05/2002','Masculino','Ensino Médio',22000008),('Davi Pereira','Năo possuo','14/04/1998','Masculino','Ensino Fundamental',22000009),('Gabriela Souza','Engenheira','10/10/1990','Feminino','Pós-Graduaçăo',22000010),('Gabriela Souza','Estagiária','10/10/2000','Feminino','Mestrado',22000011);
/*!40000 ALTER TABLE `alunos excel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-30  8:14:02
