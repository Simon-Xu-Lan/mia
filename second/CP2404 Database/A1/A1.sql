-- MySQL dump 10.13  Distrib 8.0.30, for macos12 (x86_64)
--
-- Host: 127.0.0.1    Database: activekids_db
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
-- Table structure for table `access_card`
--

DROP TABLE IF EXISTS `access_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `access_card` (
  `access_card_id` int NOT NULL,
  `employee_id` int DEFAULT NULL,
  `worker_id` int DEFAULT NULL,
  PRIMARY KEY (`access_card_id`),
  KEY `access_card_to_worker_idx` (`worker_id`),
  KEY `access_card_to_employee_idx` (`employee_id`),
  CONSTRAINT `access_card_to_employee` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`),
  CONSTRAINT `access_card_to_worker` FOREIGN KEY (`worker_id`) REFERENCES `casual_worker` (`worker_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `access_card`
--

LOCK TABLES `access_card` WRITE;
/*!40000 ALTER TABLE `access_card` DISABLE KEYS */;
/*!40000 ALTER TABLE `access_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch` (
  `branch_id` int NOT NULL,
  `district` varchar(45) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `manager` int DEFAULT NULL,
  PRIMARY KEY (`branch_id`),
  KEY `branch_to_employee_idx` (`manager`),
  CONSTRAINT `branch_to_employee` FOREIGN KEY (`manager`) REFERENCES `employee` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `buiilding`
--

DROP TABLE IF EXISTS `buiilding`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buiilding` (
  `building_id` int NOT NULL,
  `building_name` varchar(45) DEFAULT NULL,
  `building_other_info` varchar(45) DEFAULT NULL,
  `access_card_id` int DEFAULT NULL,
  PRIMARY KEY (`building_id`),
  KEY `building_to_access_card_idx` (`access_card_id`),
  CONSTRAINT `building_to_access_card` FOREIGN KEY (`access_card_id`) REFERENCES `access_card` (`access_card_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buiilding`
--

LOCK TABLES `buiilding` WRITE;
/*!40000 ALTER TABLE `buiilding` DISABLE KEYS */;
/*!40000 ALTER TABLE `buiilding` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `casual_worker`
--

DROP TABLE IF EXISTS `casual_worker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `casual_worker` (
  `worker_id` int NOT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `contact` varchar(45) DEFAULT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `start_date` datetime DEFAULT NULL,
  `end_date` datetime DEFAULT NULL,
  `payment_rate` int DEFAULT NULL,
  `work_hours` int DEFAULT NULL,
  `branch_id` int DEFAULT NULL,
  PRIMARY KEY (`worker_id`),
  KEY `casual_worker_to_branch_idx` (`branch_id`),
  CONSTRAINT `casual_worker_to_branch` FOREIGN KEY (`branch_id`) REFERENCES `branch` (`branch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `casual_worker`
--

LOCK TABLES `casual_worker` WRITE;
/*!40000 ALTER TABLE `casual_worker` DISABLE KEYS */;
/*!40000 ALTER TABLE `casual_worker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `children`
--

DROP TABLE IF EXISTS `children`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `children` (
  `child_id` int NOT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `height` float DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `digital_photo` varchar(100) DEFAULT NULL,
  `parent` int DEFAULT NULL,
  PRIMARY KEY (`child_id`),
  KEY `children_to_customer_idx` (`parent`),
  CONSTRAINT `children_to_customer` FOREIGN KEY (`parent`) REFERENCES `customer` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `children`
--

LOCK TABLES `children` WRITE;
/*!40000 ALTER TABLE `children` DISABLE KEYS */;
/*!40000 ALTER TABLE `children` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `children_gear`
--

DROP TABLE IF EXISTS `children_gear`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `children_gear` (
  `child_id` int NOT NULL,
  `gear_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`child_id`),
  KEY `children_gear_to_gear_idx` (`gear_id`),
  CONSTRAINT `children_gear_to_children` FOREIGN KEY (`child_id`) REFERENCES `children` (`child_id`),
  CONSTRAINT `children_gear_to_gear` FOREIGN KEY (`gear_id`) REFERENCES `sport_gear` (`gear_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `children_gear`
--

LOCK TABLES `children_gear` WRITE;
/*!40000 ALTER TABLE `children_gear` DISABLE KEYS */;
/*!40000 ALTER TABLE `children_gear` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `children_session`
--

DROP TABLE IF EXISTS `children_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `children_session` (
  `child_id` int NOT NULL,
  `session_id` int NOT NULL,
  `session_date` datetime NOT NULL,
  `hours` int DEFAULT NULL,
  PRIMARY KEY (`child_id`,`session_id`,`session_date`),
  KEY `children_session_to_session_idx` (`session_id`),
  CONSTRAINT `children_session_to_child` FOREIGN KEY (`child_id`) REFERENCES `children` (`child_id`),
  CONSTRAINT `children_session_to_session` FOREIGN KEY (`session_id`) REFERENCES `training_session` (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `children_session`
--

LOCK TABLES `children_session` WRITE;
/*!40000 ALTER TABLE `children_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `children_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL,
  `contact` varchar(45) DEFAULT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employee_id` int NOT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `contact` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `previous_manager` int DEFAULT NULL,
  `current_manager` int DEFAULT NULL,
  `qualification` varchar(45) DEFAULT NULL,
  `certification_start_date` datetime DEFAULT NULL,
  `certification_end_date` datetime DEFAULT NULL,
  `staff_type_id` int DEFAULT NULL,
  `branch_id` int DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `employee_to_branch_idx` (`branch_id`),
  KEY `employee_to_staff_type_idx` (`staff_type_id`),
  KEY `employee_to_employee_idx` (`previous_manager`),
  KEY `employee_to_employee_curr_idx` (`current_manager`),
  CONSTRAINT `employee_to_branch` FOREIGN KEY (`branch_id`) REFERENCES `branch` (`branch_id`),
  CONSTRAINT `employee_to_employee_curr` FOREIGN KEY (`current_manager`) REFERENCES `employee` (`employee_id`),
  CONSTRAINT `employee_to_employee_prev` FOREIGN KEY (`previous_manager`) REFERENCES `employee` (`employee_id`),
  CONSTRAINT `employee_to_staff_type` FOREIGN KEY (`staff_type_id`) REFERENCES `staff_type` (`staff_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipad`
--

DROP TABLE IF EXISTS `ipad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipad` (
  `ipad_id` int NOT NULL,
  `ipad_name` varchar(45) DEFAULT NULL,
  `model` varchar(45) DEFAULT NULL,
  `color` varchar(45) DEFAULT NULL,
  `other_spec` varchar(300) DEFAULT NULL,
  `history_of_repair` varchar(200) DEFAULT NULL,
  `purchase_date` datetime DEFAULT NULL,
  `employee_id` int DEFAULT NULL,
  PRIMARY KEY (`ipad_id`),
  KEY `ipad_to_employee_idx` (`employee_id`),
  CONSTRAINT `ipad_to_employee` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipad`
--

LOCK TABLES `ipad` WRITE;
/*!40000 ALTER TABLE `ipad` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary` (
  `salary_start_date` int NOT NULL,
  `employee_id` int NOT NULL,
  `salary_end)_date` datetime DEFAULT NULL,
  PRIMARY KEY (`salary_start_date`,`employee_id`),
  KEY `salary_to_employee_idx` (`employee_id`),
  CONSTRAINT `salary_to_employee` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sport_gear`
--

DROP TABLE IF EXISTS `sport_gear`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sport_gear` (
  `gear_id` int NOT NULL,
  `gear_name` varchar(45) DEFAULT NULL,
  `gear_details` varchar(200) DEFAULT NULL,
  `unit_price` float DEFAULT NULL,
  PRIMARY KEY (`gear_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sport_gear`
--

LOCK TABLES `sport_gear` WRITE;
/*!40000 ALTER TABLE `sport_gear` DISABLE KEYS */;
/*!40000 ALTER TABLE `sport_gear` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_type`
--

DROP TABLE IF EXISTS `staff_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_type` (
  `staff_type_id` int NOT NULL,
  `type_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`staff_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_type`
--

LOCK TABLES `staff_type` WRITE;
/*!40000 ALTER TABLE `staff_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `staff_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `training_session`
--

DROP TABLE IF EXISTS `training_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `training_session` (
  `session_id` int NOT NULL,
  `session_name` varchar(45) DEFAULT NULL,
  `session_fees` float DEFAULT NULL,
  `trainer_id` int DEFAULT NULL,
  PRIMARY KEY (`session_id`),
  KEY `session_to_employee_idx` (`trainer_id`),
  CONSTRAINT `session_to_employee` FOREIGN KEY (`trainer_id`) REFERENCES `employee` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `training_session`
--

LOCK TABLES `training_session` WRITE;
/*!40000 ALTER TABLE `training_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `training_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work_hour`
--

DROP TABLE IF EXISTS `work_hour`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `work_hour` (
  `month` datetime NOT NULL,
  `worker_id` int NOT NULL,
  `working_hours` int DEFAULT NULL,
  PRIMARY KEY (`month`,`worker_id`),
  KEY `work_hour_to_casual_worker_idx` (`worker_id`),
  CONSTRAINT `work_hour_to_casual_worker` FOREIGN KEY (`worker_id`) REFERENCES `casual_worker` (`worker_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_hour`
--

LOCK TABLES `work_hour` WRITE;
/*!40000 ALTER TABLE `work_hour` DISABLE KEYS */;
/*!40000 ALTER TABLE `work_hour` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-27 11:42:09
