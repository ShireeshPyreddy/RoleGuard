-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: organization
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `emp_hr`
--

DROP TABLE IF EXISTS `emp_hr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_hr` (
  `id` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone_no` varchar(20) DEFAULT NULL,
  `user_rank` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_hr`
--

LOCK TABLES `emp_hr` WRITE;
/*!40000 ALTER TABLE `emp_hr` DISABLE KEYS */;
INSERT INTO `emp_hr` VALUES ('INFOCOMHR1','854347','984577','2'),('INFOCOMHR2','dddd','33234','12');
/*!40000 ALTER TABLE `emp_hr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emp_pr`
--

DROP TABLE IF EXISTS `emp_pr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_pr` (
  `id` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone_no` varchar(20) DEFAULT NULL,
  `salary` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_pr`
--

LOCK TABLES `emp_pr` WRITE;
/*!40000 ALTER TABLE `emp_pr` DISABLE KEYS */;
INSERT INTO `emp_pr` VALUES ('INFOCOMPR1','11','234334',34534.00),('INFOCOMPR2','kjkfnfn','3483989',3843439.00),('INFOCOMPR3','3213123','232133',23232133.00);
/*!40000 ALTER TABLE `emp_pr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emp_se`
--

DROP TABLE IF EXISTS `emp_se`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_se` (
  `id` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone_no` varchar(20) DEFAULT NULL,
  `salary` decimal(10,2) DEFAULT NULL,
  `bloodgroup` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_se`
--

LOCK TABLES `emp_se` WRITE;
/*!40000 ALTER TABLE `emp_se` DISABLE KEYS */;
INSERT INTO `emp_se` VALUES ('INFOCOMSE1','1234 Watson St','+1 908-890-8908',-1.00,'A+'),('INFOCOMSE2','124 St','1234',123.00,'');
/*!40000 ALTER TABLE `emp_se` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hr_data`
--

DROP TABLE IF EXISTS `hr_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hr_data` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `department` varchar(255) NOT NULL,
  `supervisor` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_data`
--

LOCK TABLES `hr_data` WRITE;
/*!40000 ALTER TABLE `hr_data` DISABLE KEYS */;
INSERT INTO `hr_data` VALUES ('INFOCOMHR1','xdfbsb','jdjgbjb','aaa'),('INFOCOMHR2','abc','cccc','cccc');
/*!40000 ALTER TABLE `hr_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_credential`
--

DROP TABLE IF EXISTS `login_credential`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_credential` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_credential`
--

LOCK TABLES `login_credential` WRITE;
/*!40000 ALTER TABLE `login_credential` DISABLE KEYS */;
INSERT INTO `login_credential` VALUES ('abc','abc@123','GENERAL'),('Eva','Eva@123','SE'),('Maria','maria@123','PR'),('Mustafa','Mustafa@123','HR'),('Nami','Nami@123','PR'),('Shireesh','shireesh@123','Admin'),('Tom','Tom@123','GENERAL');
/*!40000 ALTER TABLE `login_credential` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pr_data`
--

DROP TABLE IF EXISTS `pr_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pr_data` (
  `id` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pr_data`
--

LOCK TABLES `pr_data` WRITE;
/*!40000 ALTER TABLE `pr_data` DISABLE KEYS */;
INSERT INTO `pr_data` VALUES ('INFOCOMPR1','Nami','kjkdb','2222-12-22'),('INFOCOMPR2','djnkjjsfn','KKKKKKKK','2222-12-22');
/*!40000 ALTER TABLE `pr_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `se_data`
--

DROP TABLE IF EXISTS `se_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `se_data` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `projectname` varchar(255) NOT NULL,
  `supervisor` varchar(255) DEFAULT NULL,
  `deadline` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `se_data`
--

LOCK TABLES `se_data` WRITE;
/*!40000 ALTER TABLE `se_data` DISABLE KEYS */;
INSERT INTO `se_data` VALUES ('INFOCOMSE2','Sam S1','Sam','Sam','2022-12-24'),('INFOCOMSE3','fjnsjnfskfn','kdjcnknj','skdkjfnkfjs','2023-12-23');
/*!40000 ALTER TABLE `se_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-04 17:02:02
