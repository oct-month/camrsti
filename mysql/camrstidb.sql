-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: camrstidb
-- ------------------------------------------------------
-- Server version	8.0.30

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
USE camrstidb;

--
-- Table structure for table `MicroView`
--

DROP TABLE IF EXISTS `MicroView`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MicroView` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '金相、矿相、电子显微照片',
  `sampleImage` json DEFAULT NULL COMMENT '样品全图',
  `sampleDescribe` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '描述',
  `device` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '设备',
  `sampleId` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '样品id',
  PRIMARY KEY (`id`),
  KEY `NewTable_FK` (`sampleId`),
  CONSTRAINT `NewTable_FK` FOREIGN KEY (`sampleId`) REFERENCES `SampleInfo` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MicroView`
--

LOCK TABLES `MicroView` WRITE;
/*!40000 ALTER TABLE `MicroView` DISABLE KEYS */;
INSERT INTO `MicroView` VALUES (1,'矿相','[\"图片2.jpg\"]','红色区域，有较多的粗砂和岩屑，该部分黏土基质较多','徕卡2700P','11Y3:9-1');
/*!40000 ALTER TABLE `MicroView` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MicroViewData`
--

DROP TABLE IF EXISTS `MicroViewData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MicroViewData` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `zoom` double DEFAULT NULL COMMENT '放大倍数',
  `image` varchar(50) DEFAULT NULL COMMENT '照片',
  `photoMode` varchar(30) DEFAULT NULL COMMENT '拍摄模式',
  `describe` text COMMENT '描述',
  `microId` bigint unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `MicroViewData_FK` (`microId`),
  CONSTRAINT `MicroViewData_FK` FOREIGN KEY (`microId`) REFERENCES `MicroView` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MicroViewData`
--

LOCK TABLES `MicroViewData` WRITE;
/*!40000 ALTER TABLE `MicroViewData` DISABLE KEYS */;
INSERT INTO `MicroViewData` VALUES (1,10,'图片3.jpg','XPL','整体结构为大量的岩石和砂颗粒和少量黏土基质，图中上下为石英砂岩和花岗岩颗粒，中间为黏土+粉砂',1),(2,10,'图片4.jpg','PPL','与左图正交偏光图像综合对比，可以辅助判定矿相、空洞和不透明物质',1);
/*!40000 ALTER TABLE `MicroViewData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MineChemistryInfo`
--

DROP TABLE IF EXISTS `MineChemistryInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MineChemistryInfo` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品编号',
  `type` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '类型',
  `Na2O` double DEFAULT NULL,
  `MgO` double DEFAULT NULL,
  `Al2O3` double DEFAULT NULL,
  `SiO2` double DEFAULT NULL,
  `K2O` double DEFAULT NULL,
  `CaO` double DEFAULT NULL,
  `Fe2O3` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='化学成分数据';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MineChemistryInfo`
--

LOCK TABLES `MineChemistryInfo` WRITE;
/*!40000 ALTER TABLE `MineChemistryInfo` DISABLE KEYS */;
INSERT INTO `MineChemistryInfo` VALUES ('11Y3:9-1','炉衬',2.2,1.4,17.8,60.3,2.9,1,4.8),('11Y3:9-2','炉衬',2.2,1.4,21.2,61.9,3,1,4.2),('11Y3:9-3','炉衬',2.2,1.4,14.3,58.6,2.8,1,5.5);
/*!40000 ALTER TABLE `MineChemistryInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MineContentInfo`
--

DROP TABLE IF EXISTS `MineContentInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MineContentInfo` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品号',
  `sampleName` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '样品名称',
  `clay` double DEFAULT NULL COMMENT '粘土基质',
  `quartz` double DEFAULT NULL COMMENT '石英粉砂',
  `sand` json DEFAULT NULL COMMENT '砂',
  `debris` double DEFAULT NULL COMMENT '岩屑',
  `hollow` double DEFAULT NULL COMMENT '空洞',
  `other` double DEFAULT NULL COMMENT '其他',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='矿物含量信息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MineContentInfo`
--

LOCK TABLES `MineContentInfo` WRITE;
/*!40000 ALTER TABLE `MineContentInfo` DISABLE KEYS */;
INSERT INTO `MineContentInfo` VALUES ('11Y3:9-1','炉衬',34.7,7.3,'{\"quartz\": 12.5, \"feldspar\": 2, \"Ominerals\": 3}',25,15.4,NULL),('11Y3:9-2','炉衬',31.8,6.4,'{\"quartz\": 10.9, \"feldspar\": 1.6, \"Ominerals\": 4.5}',29.1,15.7,NULL),('11Y3:9-3','炉衬',34.2,8.2,'{\"quartz\": 13.9, \"feldspar\": 1.6, \"Ominerals\": 1.3}',22.9,17.9,NULL);
/*!40000 ALTER TABLE `MineContentInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MinePhysicsInfo`
--

DROP TABLE IF EXISTS `MinePhysicsInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MinePhysicsInfo` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品编号',
  `type` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '类型',
  `apparentPorosity` double DEFAULT NULL COMMENT '显气孔率',
  `trueDensity` double DEFAULT NULL COMMENT '真密度',
  `waterAbsorption` double DEFAULT NULL COMMENT '吸水率',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='物理结构数据';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MinePhysicsInfo`
--

LOCK TABLES `MinePhysicsInfo` WRITE;
/*!40000 ALTER TABLE `MinePhysicsInfo` DISABLE KEYS */;
INSERT INTO `MinePhysicsInfo` VALUES ('11Y3:9-1','砂泥质大块炉衬',39.5,2.612,24.8);
/*!40000 ALTER TABLE `MinePhysicsInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MineSurveyInfo`
--

DROP TABLE IF EXISTS `MineSurveyInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MineSurveyInfo` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品号',
  `debrisData` json DEFAULT NULL COMMENT '岩屑直径分布',
  `hollowData` json DEFAULT NULL COMMENT '空洞长度分布',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='矿物测量数据';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MineSurveyInfo`
--

LOCK TABLES `MineSurveyInfo` WRITE;
/*!40000 ALTER TABLE `MineSurveyInfo` DISABLE KEYS */;
INSERT INTO `MineSurveyInfo` VALUES ('11Y3:9-1','{\"167-501\": 11.8, \"≥1002\": 30.6, \"501-1002\": 13.4, \"≤67μm\": 20.7, \"67-167μm\": 23.5}','{\"≤167\": 61.2, \"167-501\": 8.7, \"＞2004\": 7.1, \"501-1002\": 10.4, \"1002-2004\": 12.6}'),('11Y3:9-2','{\"167-501\": 6.4, \"≥1002\": 32.1, \"501-1002\": 9.3, \"≤67μm\": 21.7, \"67-167μm\": 30.6}','{\"≤167\": 59.1, \"167-501\": 11, \"＞2004\": null, \"501-1002\": 18.8, \"1002-2004\": 11}'),('11Y3:9-3','{\"167-501\": 13.6, \"≥1002\": 22.4, \"501-1002\": 12.2, \"≤67μm\": 24.2, \"67-167μm\": 27.5}','{\"≤167\": 68.9, \"167-501\": 12.6, \"＞2004\": 10.2, \"501-1002\": 3.6, \"1002-2004\": 4.8}');
/*!40000 ALTER TABLE `MineSurveyInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MineThermalInfo`
--

DROP TABLE IF EXISTS `MineThermalInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MineThermalInfo` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品号',
  `termTemper` double DEFAULT NULL COMMENT '终止温度',
  `fireResis` double DEFAULT NULL COMMENT '耐火度',
  `data` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '热分析数据',
  `surveImage` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '热分析曲线',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='热分析';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MineThermalInfo`
--

LOCK TABLES `MineThermalInfo` WRITE;
/*!40000 ALTER TABLE `MineThermalInfo` DISABLE KEYS */;
INSERT INTO `MineThermalInfo` VALUES ('11Y3:9-1',1015,1303,NULL,'图片1.png'),('11Y3:9-2',929,1306,NULL,'图片1.png'),('11Y3:9-3',1025,1307,NULL,'图片1.png');
/*!40000 ALTER TABLE `MineThermalInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MineXRDInfo`
--

DROP TABLE IF EXISTS `MineXRDInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MineXRDInfo` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品编号',
  `type` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '类型',
  `quartz` double DEFAULT NULL COMMENT '石英',
  `albite` double DEFAULT NULL COMMENT '钠长石',
  `potashFeldspar` double DEFAULT NULL COMMENT '钾长石',
  `mica` double DEFAULT NULL COMMENT '云母',
  `amphibole` double DEFAULT NULL COMMENT '闪石',
  `hematite` double DEFAULT NULL COMMENT '赤铁矿',
  `magnetite` double DEFAULT NULL COMMENT '磁铁矿',
  `dolomite` double DEFAULT NULL COMMENT '白云石',
  `analcite` double DEFAULT NULL COMMENT '方沸石',
  `tridymite` double DEFAULT NULL COMMENT '磷石英',
  `cristobalite` double DEFAULT NULL COMMENT '方石英',
  `mullite` double DEFAULT NULL COMMENT '莫来石',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='XRD分析数据';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MineXRDInfo`
--

LOCK TABLES `MineXRDInfo` WRITE;
/*!40000 ALTER TABLE `MineXRDInfo` DISABLE KEYS */;
INSERT INTO `MineXRDInfo` VALUES ('11Y3:9-1','炉衬',76,24,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('11Y3:9-2','炉衬',63,14,20,NULL,NULL,4,NULL,NULL,NULL,NULL,NULL,NULL),('11Y3:9-3','炉衬',45,19,22,NULL,6,NULL,2,6,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `MineXRDInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SampleInfo`
--

DROP TABLE IF EXISTS `SampleInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SampleInfo` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品号',
  `type` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '样品类型',
  `source` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '样品来源',
  `year` year DEFAULT NULL COMMENT '取样年份',
  `people` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '取样人',
  `imageId` json DEFAULT NULL COMMENT '照片号',
  `describe` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '描述',
  `explain` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '样品制备说明',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='样品基本信息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SampleInfo`
--

LOCK TABLES `SampleInfo` WRITE;
/*!40000 ALTER TABLE `SampleInfo` DISABLE KEYS */;
INSERT INTO `SampleInfo` VALUES ('11Y3:9-1','炉壁','北京延庆水泉沟',2019,'刘海峰','[\"IMG_20190512_33333.jpg\"]','取自炉体上半部分，红色，质地疏松多空','自内向外取三处，分别做薄片后矿相观察，制备粉末样品开展XRD分析'),('11Y3:9-2','炉壁','北京延庆水泉沟',2019,'刘海峰','[\"IMG_20190512_33333.jpg\"]','取自炉体上半部分，红色，质地疏松多空','自内向外取三处，分别做薄片后矿相观察，制备粉末样品开展XRD分析'),('11Y3:9-3','炉壁','北京延庆水泉沟',2019,'刘海峰','[\"IMG_20190512_33333.jpg\"]','取自炉体上半部分，红色，质地疏松多空','自内向外取三处，分别做薄片后矿相观察，制备粉末样品开展XRD分析');
/*!40000 ALTER TABLE `SampleInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'camrstidb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-23 22:53:26
