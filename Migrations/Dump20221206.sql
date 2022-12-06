-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: telegrambot
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add notify',7,'add_notify'),(26,'Can change notify',7,'change_notify'),(27,'Can delete notify',7,'delete_notify'),(28,'Can view notify',7,'view_notify'),(29,'Can add requests',8,'add_requests'),(30,'Can change requests',8,'change_requests'),(31,'Can delete requests',8,'delete_requests'),(32,'Can view requests',8,'view_requests'),(33,'Can add users',9,'add_users'),(34,'Can change users',9,'change_users'),(35,'Can delete users',9,'delete_users'),(36,'Can view users',9,'view_users');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tg_id` int DEFAULT '0',
  `password` varchar(128) NOT NULL,
  `token_requests_count` int NOT NULL DEFAULT '0',
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `descrtext` text,
  `first_token` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,1855954960,'pbkdf2_sha256$390000$PFk7JPOlob5m8VsB47gkXJ$kGIxmWOMPnK0uj27Sf5QgLyHh/9sq6rzdNFY/sRuWFE=',0,'2022-11-14 08:31:05.339935',1,'AlexEltc','Ельцов','Алексей','aleksey18rus@inbox.ru',1,1,'2022-11-14 09:10:08.000000','','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(2,0,'',0,'2022-11-14 08:30:34.742951',0,'','','','',0,1,'2022-11-14 08:38:21.000000','','');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-11-09 12:08:29.649518','5','Users object (5)',1,'[{\"added\": {}}]',9,1),(2,'2022-11-09 12:09:22.028183','5','Users object (5)',3,'',9,1),(3,'2022-11-10 10:23:09.720064','7','Notify object (7)',3,'',7,1),(4,'2022-11-10 10:40:43.889125','6','Users object (6)',1,'[{\"added\": {}}]',9,1),(5,'2022-11-10 10:40:59.317094','6','Users object (6)',3,'',9,1),(6,'2022-11-11 07:46:55.254770','6','Notify object (6)',2,'[{\"changed\": {\"fields\": [\"Sended\"]}}]',7,1),(7,'2022-11-11 07:47:00.430185','5','Notify object (5)',2,'[{\"changed\": {\"fields\": [\"Sended\"]}}]',7,1),(8,'2022-11-11 07:51:21.064004','2','newUser',1,'[{\"added\": {}}]',4,1),(9,'2022-11-11 07:51:44.893430','2','newUser',2,'[{\"changed\": {\"fields\": [\"Last login\"]}}]',4,1),(10,'2022-11-11 08:43:40.507613','1','AuthUser object (1)',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email\", \"First token\"]}}]',10,1),(11,'2022-11-18 06:21:33.572811','104','Requests object (104)',1,'[{\"added\": {}}]',8,1),(12,'2022-11-18 06:22:22.330663','104','Requests object (104)',2,'[{\"changed\": {\"fields\": [\"Tg id\"]}}]',8,1),(13,'2022-11-18 06:22:34.711281','104','Requests object (104)',3,'',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(10,'telegramBot','authuser'),(7,'telegramBot','notify'),(8,'telegramBot','requests'),(9,'telegramBot','users');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-11-09 12:02:16.120180'),(2,'auth','0001_initial','2022-11-09 12:02:16.637796'),(3,'admin','0001_initial','2022-11-09 12:02:16.798396'),(4,'admin','0002_logentry_remove_auto_add','2022-11-09 12:02:16.820336'),(5,'admin','0003_logentry_add_action_flag_choices','2022-11-09 12:02:16.831338'),(6,'contenttypes','0002_remove_content_type_name','2022-11-09 12:02:16.898128'),(7,'auth','0002_alter_permission_name_max_length','2022-11-09 12:02:16.953979'),(8,'auth','0003_alter_user_email_max_length','2022-11-09 12:02:16.975922'),(9,'auth','0004_alter_user_username_opts','2022-11-09 12:02:16.986891'),(10,'auth','0005_alter_user_last_login_null','2022-11-09 12:02:17.051718'),(11,'auth','0006_require_contenttypes_0002','2022-11-09 12:02:17.056706'),(12,'auth','0007_alter_validators_add_error_messages','2022-11-09 12:02:17.069671'),(13,'auth','0008_alter_user_username_max_length','2022-11-09 12:02:17.151452'),(14,'auth','0009_alter_user_last_name_max_length','2022-11-09 12:02:17.237222'),(15,'auth','0010_alter_group_name_max_length','2022-11-09 12:02:17.267142'),(16,'auth','0011_update_proxy_permissions','2022-11-09 12:02:17.283100'),(17,'auth','0012_alter_user_first_name_max_length','2022-11-09 12:02:17.355905'),(18,'sessions','0001_initial','2022-11-09 12:02:17.389814'),(19,'telegramBot','0001_initial','2022-11-09 12:02:17.397793');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('m4c8a9vyg36twewbc7a330yzxry2edhe','.eJxVjEsOAiEQBe_C2hAYaT4u3c8ZSNMNMmogmc_KeHedZBa6fVX1XiLitta4LXmOE4uL0OL0uyWkR2474Du2W5fU2zpPSe6KPOgix875eT3cv4OKS_3WNBCpoL0_F8vgVIGCrmQC8hgMJ1WYAlhgh8qgNkGB0WD8EKwffAHx_gDxoTeK:1ouUrx:DyTR4t3a00h271eY0AIW1IFcHQhfzPVR8FS3glNAGlA','2022-11-28 08:31:05.343409');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notify`
--

DROP TABLE IF EXISTS `notify`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notify` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tg_id` int NOT NULL DEFAULT '0',
  `notify_text` text,
  `sended` smallint NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notify`
--

LOCK TABLES `notify` WRITE;
/*!40000 ALTER TABLE `notify` DISABLE KEYS */;
INSERT INTO `notify` VALUES (1,1855954960,'test',1),(2,1855954960,'test',1),(3,1855954960,'test2',1),(4,1855954960,'test2',1),(5,1855954960,'test2',1),(6,1855954960,'test2',1);
/*!40000 ALTER TABLE `notify` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requests` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tg_id` int NOT NULL DEFAULT '0',
  `ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `request_text` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
INSERT INTO `requests` VALUES (1,1855954960,'2022-11-02 06:14:48','H'),(2,1855954960,'2022-11-02 06:15:48','W'),(3,1855954960,'2022-11-02 06:17:04','N'),(4,1855954960,'2022-11-02 06:17:18','J'),(5,1855954960,'2022-11-02 06:17:42','G'),(6,1855954960,'2022-11-02 06:43:36','J'),(7,1855954960,'2022-11-02 07:27:22','123'),(8,1855954960,'2022-11-02 07:34:16','123'),(9,1855954960,'2022-11-02 08:30:46','123'),(10,1855954960,'2022-11-02 08:36:49','123'),(11,1855954960,'2022-11-02 08:48:03','Лвлвлв'),(12,1855954960,'2022-11-02 08:48:44','123'),(13,1855954960,'2022-11-02 08:49:33','123'),(14,1855954960,'2022-11-02 08:53:40','123'),(15,1855954960,'2022-11-02 08:53:50','?)₽:'),(16,1855954960,'2022-11-02 08:53:51','!:!:'),(17,1855954960,'2022-11-02 08:54:31','123'),(18,1855954960,'2022-11-02 09:02:14','впролд'),(19,1855954960,'2022-11-02 09:02:17','Паша'),(20,1855954960,'2022-11-02 09:04:19','Балла'),(21,1855954960,'2022-11-02 09:04:21','Аджа'),(22,1855954960,'2022-11-02 09:04:29','Млрд'),(23,1855954960,'2022-11-02 09:07:03','Шашапш'),(24,1855954960,'2022-11-02 09:07:05','Идти'),(25,1855954960,'2022-11-02 09:07:17','123'),(26,1855954960,'2022-11-02 09:17:38','Влады'),(27,1855954960,'2022-11-02 09:18:07','123'),(28,1855954960,'2022-11-02 09:18:17',':,))'),(29,1855954960,'2022-11-02 09:33:00','a09d7f6308438eade8541b59742c39a9e8bbc44b0c60de8acbbd9283d2d25eb608e8a2701db9c4919c868a31078114e1780d'),(30,1855954960,'2022-11-03 03:20:58','Обж'),(31,0,'2022-11-03 07:19:15','test'),(32,0,'2022-11-03 07:20:07','test'),(33,1855954960,'2022-11-03 04:41:02','Соси'),(34,1855954960,'2022-11-03 05:30:43','rhdtgf'),(35,1855954960,'2022-11-03 05:30:47','dgfhjh'),(36,1855954960,'2022-11-03 05:31:25','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(37,1855954960,'2022-11-03 05:33:21','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(38,1855954960,'2022-11-03 05:40:02','sadj'),(39,1855954960,'2022-11-03 05:42:44','czdfbn'),(40,1855954960,'2022-11-03 05:43:23','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(41,1855954960,'2022-11-03 05:43:57','dsfgdhgjkl'),(42,1855954960,'2022-11-03 05:46:01','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(43,1855954960,'2022-11-03 05:46:36','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(44,1855954960,'2022-11-03 05:49:23','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(45,1855954960,'2022-11-03 06:24:28','Дили'),(46,1855954960,'2022-11-03 06:28:41','Лвлвлв'),(47,1855954960,'2022-11-03 06:29:14','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(48,1855954960,'2022-11-07 07:30:38','Chic'),(49,1855954960,'2022-11-07 07:32:05','Huffs'),(50,1855954960,'2022-11-07 07:34:10','Nccb'),(51,1855954960,'2022-11-07 07:35:51','T'),(52,1855954960,'2022-11-07 07:37:16','Vv'),(53,1855954960,'2022-11-07 07:40:54','Goof'),(54,1855954960,'2022-11-07 07:48:39','High'),(55,1855954960,'2022-11-07 09:03:37','Hahaha'),(56,1855954960,'2022-11-07 09:03:40','Jakarta'),(57,1855954960,'2022-11-07 09:05:09','Haha'),(58,1855954960,'2022-11-07 09:08:05','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(59,1855954960,'2022-11-07 09:14:17','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(60,1855954960,'2022-11-07 09:33:50','Kansan'),(61,1855954960,'2022-11-07 09:34:19','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(62,1855954960,'2022-11-07 09:37:52','Diana'),(63,1855954960,'2022-11-08 03:24:06','dsgfdhf'),(64,1855954960,'2022-11-08 03:25:31','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(65,1855954960,'2022-11-08 03:25:34','gsrhtdjyfku'),(66,1855954960,'2022-11-08 07:31:38','ыпароп'),(67,1855954960,'2022-11-08 07:36:32','rthyju'),(68,1855954960,'2022-11-08 07:36:56','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(69,1855954960,'2022-11-08 07:36:58','fggfhgjkhlj'),(70,1855954960,'2022-11-08 07:39:27','werhjtkl'),(71,1855954960,'2022-11-08 08:06:09','укперонлгдшжщэ'),(72,1855954960,'2022-11-08 08:06:32','куфекноглшдщ'),(73,1855954960,'2022-11-08 08:21:05','efwthyrju'),(74,1855954960,'2022-11-09 07:15:19','retrytukl'),(75,1855954960,'2022-11-09 07:18:55','gfhm'),(76,1855954960,'2022-11-09 07:20:14','dsfgjk'),(77,1855954960,'2022-11-09 07:33:31','ergd'),(78,1855954960,'2022-11-09 07:35:10','fhgjku'),(79,1855954960,'2022-11-09 08:06:45','df'),(80,1855954960,'2022-11-09 08:07:28','cd'),(81,1855954960,'2022-11-09 09:09:39','dsfgdhjk'),(82,1855954960,'2022-11-10 07:32:38','аыпвро'),(83,1855954960,'2022-11-10 07:34:56','Ывапр'),(84,1855954960,'2022-11-10 09:41:28','dafsgdhfjku'),(85,1855954960,'2022-11-10 09:45:27','efsrgthyu'),(86,1855954960,'2022-11-10 11:18:36','АВРПАОЛ'),(87,1855954960,'2022-11-11 03:15:28','Вовой'),(88,1855954960,'2022-11-11 04:40:50','Лвлвлв'),(89,1855954960,'2022-11-11 05:44:36','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(90,1855954960,'2022-11-11 05:48:30','cdsfbgh'),(91,1855954960,'2022-11-12 08:13:35','Абдаллы'),(92,1855954960,'2022-11-14 03:32:39','thyjkul'),(93,1855954960,'2022-11-14 05:36:23','trbwgt'),(94,1855954960,'2022-11-14 05:38:21','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(95,1855954960,'2022-11-14 05:39:25','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(96,1855954960,'2022-11-14 05:39:58','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(97,1855954960,'2022-11-14 05:46:02','gvhbjkl'),(98,1855954960,'2022-11-14 05:46:55','hbjkl;'),(99,1855954960,'2022-11-14 06:03:20','thryjtuyk'),(100,1855954960,'2022-11-14 06:03:24','efwrgthy'),(101,1855954960,'2022-11-14 06:04:08','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(102,1855954960,'2022-11-14 06:09:34','rethryjtu'),(103,1855954960,'2022-11-14 06:10:08','ba4aca5286ee05e5cc486b61a3d9a960847abbd6b24f4a6eec7792a2cb7f75c5731a351fd1f6860f98e17a7b7dcd892c7b06'),(105,1855954960,'2022-11-18 04:04:07','dfghjl;o\''),(106,1855954960,'2022-11-18 04:07:04','dfdghjkl;\''),(107,1855954960,'2022-11-18 04:11:18','cdfsrgthy'),(108,1855954960,'2022-11-18 04:12:06','fsrgdhjkl'),(109,1855954960,'2022-11-18 04:29:28','dsfdhyj'),(110,1855954960,'2022-11-28 06:19:44','Тоже'),(111,1855954960,'2022-11-28 06:20:34','Лулв'),(112,1855954960,'2022-11-28 06:21:13','Очагов');
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-06 10:39:34
