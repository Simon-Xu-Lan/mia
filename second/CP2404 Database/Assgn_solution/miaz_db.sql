-- MySQL dump 10.13  Distrib 8.0.30, for macos12 (x86_64)
--
-- Host: 127.0.0.1    Database: miaz_db
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `Address`
--

DROP TABLE IF EXISTS `Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Address` (
  `address_id` int NOT NULL AUTO_INCREMENT,
  `line_1_number_building` varchar(45) DEFAULT NULL,
  `line_2_number_street` varchar(45) DEFAULT NULL,
  `line_3_area_locality` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `zip_postcode` varchar(45) DEFAULT NULL,
  `state_province_county` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `other_address_details` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`address_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Address`
--

LOCK TABLES `Address` WRITE;
/*!40000 ALTER TABLE `Address` DISABLE KEYS */;
/*!40000 ALTER TABLE `Address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Patient`
--

DROP TABLE IF EXISTS `Patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Patient` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `outpatient_yn` int DEFAULT NULL,
  `hospital_number` int DEFAULT NULL,
  `nhs_number` int DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `date_of_birst` datetime DEFAULT NULL,
  `patient_first_name` varchar(45) DEFAULT NULL,
  `patient_middle_name` varchar(45) DEFAULT NULL,
  `patient_last_name` varchar(45) DEFAULT NULL,
  `height` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `next_of_kin` varchar(45) DEFAULT NULL,
  `home_phone` varchar(45) DEFAULT NULL,
  `work_phone` varchar(45) DEFAULT NULL,
  `cell_mobile_phone` varchar(45) DEFAULT NULL,
  `other_patient_details` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Patient`
--

LOCK TABLES `Patient` WRITE;
/*!40000 ALTER TABLE `Patient` DISABLE KEYS */;
/*!40000 ALTER TABLE `Patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Patient_Address`
--

DROP TABLE IF EXISTS `Patient_Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Patient_Address` (
  `patient_id` int NOT NULL,
  `aadress_id` int NOT NULL,
  `date_address_from` datetime NOT NULL,
  `date_address_to` datetime DEFAULT NULL,
  PRIMARY KEY (`aadress_id`,`date_address_from`,`patient_id`),
  KEY `fk_Patient_Address_Patient_idx` (`patient_id`),
  CONSTRAINT `fk_Patient_Address_Address` FOREIGN KEY (`aadress_id`) REFERENCES `Address` (`address_id`),
  CONSTRAINT `fk_Patient_Address_Patient` FOREIGN KEY (`patient_id`) REFERENCES `Patient` (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Patient_Address`
--

LOCK TABLES `Patient_Address` WRITE;
/*!40000 ALTER TABLE `Patient_Address` DISABLE KEYS */;
/*!40000 ALTER TABLE `Patient_Address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Staff`
--

DROP TABLE IF EXISTS `Staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Staff` (
  `staff_id` int NOT NULL AUTO_INCREMENT,
  `staff_category_code` int DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `staff_job_title` varchar(45) DEFAULT NULL,
  `staff_first_name` varchar(45) DEFAULT NULL,
  `staff_middle_name` varchar(45) DEFAULT NULL,
  `staff_last_name` varchar(45) DEFAULT NULL,
  `staff_qualifications` varchar(45) DEFAULT NULL,
  `staff_birth_date` datetime DEFAULT NULL,
  `other_staff_details` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Staff`
--

LOCK TABLES `Staff` WRITE;
/*!40000 ALTER TABLE `Staff` DISABLE KEYS */;
/*!40000 ALTER TABLE `Staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Staff_Address`
--

DROP TABLE IF EXISTS `Staff_Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Staff_Address` (
  `staff_id` int NOT NULL,
  `address_id` int NOT NULL,
  `date_address_from` datetime NOT NULL,
  `date_address_to` datetime DEFAULT NULL,
  PRIMARY KEY (`staff_id`,`address_id`,`date_address_from`),
  KEY `Staff_Address_Address_idx` (`address_id`),
  CONSTRAINT `Staff_Address_Address` FOREIGN KEY (`address_id`) REFERENCES `Address` (`address_id`),
  CONSTRAINT `Staff_address_Staff` FOREIGN KEY (`staff_id`) REFERENCES `Staff` (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Staff_Address`
--

LOCK TABLES `Staff_Address` WRITE;
/*!40000 ALTER TABLE `Staff_Address` DISABLE KEYS */;
/*!40000 ALTER TABLE `Staff_Address` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-24 15:47:19
