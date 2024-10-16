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
-- Table structure for table `tb_aluno`
--

DROP TABLE IF EXISTS `tb_aluno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_aluno` (
  `idAluno` int NOT NULL AUTO_INCREMENT,
  `nmAluno` varchar(50) NOT NULL,
  `deExperienciaProfissional` varchar(255) DEFAULT NULL,
  `dtNascimento` date DEFAULT NULL,
  `idSexo` int NOT NULL,
  `idGrauInstrucao` int NOT NULL,
  `nuRA` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`idAluno`),
  UNIQUE KEY `NONCLUSTERED` (`nuRA`),
  KEY `FK_Aluno_Sexo` (`idSexo`),
  KEY `FK_Aluno_GrauInstrucao` (`idGrauInstrucao`),
  CONSTRAINT `FK_Aluno_GrauInstrucao` FOREIGN KEY (`idGrauInstrucao`) REFERENCES `tb_grauinstrucao` (`idGrauInstrucao`),
  CONSTRAINT `FK_Aluno_Sexo` FOREIGN KEY (`idSexo`) REFERENCES `tb_sexo` (`idSexo`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_aluno`
--

LOCK TABLES `tb_aluno` WRITE;
/*!40000 ALTER TABLE `tb_aluno` DISABLE KEYS */;
INSERT INTO `tb_aluno` VALUES (1,'Sérgio Cozzetti','Professor e Gerente de Desenvolvimento de Sistemas','1967-06-30',1,5,'20202020'),(3,'Alexandre Ferreira','Estagiário','2000-10-10',1,2,'22000001'),(4,'Ana Clara','Estagiária','2001-01-01',2,2,'22000002'),(5,'Angelo Jordăo','Estudante universitário','1999-06-30',1,2,'22000003'),(6,'Bruno Rios','Programador Júnior','1999-05-10',1,2,'22000005'),(7,'Carlos Henrique','Analista Pleno ','1999-02-08',1,2,'22000006'),(8,'Danilo Rebouças','Estagiário','2002-05-20',1,2,'22000008'),(9,'Davi Pereira','Năo possuo','1998-04-14',1,1,'22000009'),(10,'Gabriela Souza','Estagiária','2000-10-10',2,5,'22000011'),(18,'Antônio Luiz','Năo tenho','1999-12-12',1,3,'22000004'),(19,'Daniel Cunha','Estudante','2001-05-25',1,3,'22000007'),(20,'Gabriela Souza','Engenheira','1990-10-10',2,4,'22000010');
/*!40000 ALTER TABLE `tb_aluno` ENABLE KEYS */;
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
