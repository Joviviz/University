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
-- Table structure for table `tb_alunocurso`
--

DROP TABLE IF EXISTS `tb_alunocurso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_alunocurso` (
  `idAlunoCurso` int NOT NULL AUTO_INCREMENT,
  `idAluno` int NOT NULL,
  `idCurso` int NOT NULL,
  `dtConclusao` date DEFAULT NULL,
  PRIMARY KEY (`idAlunoCurso`),
  UNIQUE KEY `NONCLUSTERED` (`idAluno`,`idCurso`),
  KEY `FK_AlunoCurso_Curso` (`idCurso`),
  CONSTRAINT `FK_AlunoCurso_Aluno` FOREIGN KEY (`idAluno`) REFERENCES `tb_aluno` (`idAluno`),
  CONSTRAINT `FK_AlunoCurso_Curso` FOREIGN KEY (`idCurso`) REFERENCES `tb_curso` (`idCurso`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_alunocurso`
--

LOCK TABLES `tb_alunocurso` WRITE;
/*!40000 ALTER TABLE `tb_alunocurso` DISABLE KEYS */;
INSERT INTO `tb_alunocurso` VALUES (7,20,2,'2020-01-01'),(8,10,6,'2020-01-01'),(9,10,3,'2020-01-01'),(10,19,3,'2020-01-01'),(11,9,6,'2020-01-01'),(12,18,6,'2020-01-01');
/*!40000 ALTER TABLE `tb_alunocurso` ENABLE KEYS */;
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
