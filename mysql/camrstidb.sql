set NAMES 'utf8mb4';

USE camrstidb;

UNLOCK TABLES;
DROP TABLE IF EXISTS `User`;
DROP TABLE IF EXISTS `MicroViewData`;
DROP TABLE IF EXISTS `MicroView`;
DROP TABLE IF EXISTS `SampleInfo`;
DROP TABLE IF EXISTS `MineContentInfo`;
DROP TABLE IF EXISTS `MineSurveyInfo`;
DROP TABLE IF EXISTS `MineXRDInfo`;
DROP TABLE IF EXISTS `MineChemistryInfo`;
DROP TABLE IF EXISTS `MineChemistryInfoSingle`;
DROP TABLE IF EXISTS `MinePhysicsInfo`;
DROP TABLE IF EXISTS `MineThermalInfo`;

--
-- Table structure for table `User`
--

CREATE TABLE `User` (
  `username` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户名',
  `passwd` varchar(65) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '密码',
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `MicroView`
--

LOCK TABLES `User` WRITE;
INSERT INTO `User` VALUES ('admin', 'c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646');
UNLOCK TABLES;

--
-- Table structure for table `SampleInfo`
--

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

--
-- Dumping data for table `SampleInfo`
--

LOCK TABLES `SampleInfo` WRITE;
INSERT INTO `SampleInfo` VALUES ('11Y3:9-1','炉壁','北京延庆水泉沟',2019,'刘海峰','[\"IMG_20190512_33333.jpg\"]','取自炉体上半部分，红色，质地疏松多空','自内向外取三处，分别做薄片后矿相观察，制备粉末样品开展XRD分析'),('11Y3:9-2','炉壁','北京延庆水泉沟',2019,'刘海峰','[\"IMG_20190512_33333.jpg\"]','取自炉体上半部分，红色，质地疏松多空','自内向外取三处，分别做薄片后矿相观察，制备粉末样品开展XRD分析'),('11Y3:9-3','炉壁','北京延庆水泉沟',2019,'刘海峰','[\"IMG_20190512_33333.jpg\"]','取自炉体上半部分，红色，质地疏松多空','自内向外取三处，分别做薄片后矿相观察，制备粉末样品开展XRD分析');
UNLOCK TABLES;


--
-- Table structure for table `MicroView`
--

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

--
-- Dumping data for table `MicroView`
--

LOCK TABLES `MicroView` WRITE;
INSERT INTO `MicroView` VALUES (1,'矿相','[\"图片2.jpg\"]','红色区域，有较多的粗砂和岩屑，该部分黏土基质较多','徕卡2700P','11Y3:9-1');
UNLOCK TABLES;

--
-- Table structure for table `MicroViewData`
--

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

--
-- Dumping data for table `MicroViewData`
--

LOCK TABLES `MicroViewData` WRITE;
INSERT INTO `MicroViewData` VALUES (1,10,'图片3.jpg','XPL','整体结构为大量的岩石和砂颗粒和少量黏土基质，图中上下为石英砂岩和花岗岩颗粒，中间为黏土+粉砂',1),(2,10,'图片4.jpg','PPL','与左图正交偏光图像综合对比，可以辅助判定矿相、空洞和不透明物质',1);
UNLOCK TABLES;

--
-- Table structure for table `MineContentInfo`
--

CREATE TABLE `MineContentInfo` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品号',
  `clay` double DEFAULT NULL COMMENT '粘土',
  `quartz` double DEFAULT NULL COMMENT '粉砂',
  `sand_quartz` double DEFAULT NULL COMMENT '砂-石英',
  `sand_feldspar` double DEFAULT NULL COMMENT '砂-长石',
  `sand_other` double DEFAULT NULL COMMENT '砂-其他矿物',
  `debris` double DEFAULT NULL COMMENT '岩屑',
  `hollow_close` double DEFAULT NULL COMMENT '空洞-闭气孔',
  `hollow_open` double DEFAULT NULL COMMENT '空洞-开气孔',
  `hollow_through` double DEFAULT NULL COMMENT '空洞-贯通气孔',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='矿物含量信息';

--
-- Dumping data for table `MineContentInfo`
--

LOCK TABLES `MineContentInfo` WRITE;
INSERT INTO `MineContentInfo` VALUES ('11Y3:9-1',34.7,7.3,12.5,2,3,25,null,null,null),('11Y3:9-2',31.8,6.4,10.9,1.6,4.5,29.1,null,null,null),('11Y3:9-3',34.2,8.2,13.9,1.6,1.3,22.9,null,null,null);
UNLOCK TABLES;

--
-- Table structure for table `MineSurveyInfo`
--

CREATE TABLE `MineSurveyInfo` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品号',
  `debris_0um` double DEFAULT NULL COMMENT '岩屑直径≤67μm',
  `debris_67um` double DEFAULT NULL COMMENT '岩屑直径67-167μm',
  `debris_167um` double DEFAULT NULL COMMENT '岩屑直径167-501μm',
  `debris_501um` double DEFAULT NULL COMMENT '岩屑直径501-1002μm',
  `debris_1002um` double DEFAULT NULL COMMENT '岩屑直径≥1002μm',
  `hollow_0um` double DEFAULT NULL COMMENT '岩屑直径≤67μm',
  `hollow_67um` double DEFAULT NULL COMMENT '岩屑直径67-501μm',
  `hollow_501um` double DEFAULT NULL COMMENT '岩屑直径501-1002μm',
  `hollow_1002um` double DEFAULT NULL COMMENT '岩屑直径1002-2004μm',
  `hollow_2004um` double DEFAULT NULL COMMENT '岩屑直径≥2004μm',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='矿物测量数据';

--
-- Dumping data for table `MineSurveyInfo`
--

LOCK TABLES `MineSurveyInfo` WRITE;
INSERT INTO `MineSurveyInfo` VALUES ('11Y3:9-1',20.7,23.5,11.8,13.4,30.6,61.2,8.7,10.4,12.6,7.1),('11Y3:9-2',21.7,30.6,6.4,9.3,32.1,59.1,11,18.8,11,null),('11Y3:9-3',24.2,27.5,13.6,12.2,22.4,68.9,12.6,3.6,4.8,10.2);
UNLOCK TABLES;

--
-- Table structure for table `MineXRDInfo`
--

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
  `other` double DEFAULT NULL COMMENT '其他',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='XRD分析数据';

--
-- Dumping data for table `MineXRDInfo`
--

LOCK TABLES `MineXRDInfo` WRITE;
INSERT INTO `MineXRDInfo` VALUES ('11Y3:9-1','炉衬',0.76,0.24,null,null,null,null,null,null,null,null,null,null,null),('11Y3:9-2','炉衬',0.63,0.14,0.2,null,null,0.04,null,null,null,null,null,null,null),('11Y3:9-3','炉衬',0.45,0.19,0.22,null,0.06,null,0.02,0.06,null,null,null,null,null);
UNLOCK TABLES;

--
-- Table structure for table `MineChemistryInfo`
--

CREATE TABLE `MineChemistryInfo` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品号',
  `Na2O` double DEFAULT NULL,
  `MgO` double DEFAULT NULL,
  `Al2O3` double DEFAULT NULL,
  `SiO2` double DEFAULT NULL,
  `P2O5` double DEFAULT NULL,
  `SO2` double DEFAULT NULL,
  `K2O` double DEFAULT NULL,
  `CaO` double DEFAULT NULL,
  `TiO2` double DEFAULT NULL,
  `MnO` double DEFAULT NULL,
  `FeO` double DEFAULT NULL,
  `CuO` double DEFAULT NULL,
  `ZnO` double DEFAULT NULL,
  `As2O3` double DEFAULT NULL,
  `SnO2` double DEFAULT NULL,
  `PbO` double DEFAULT NULL,
  `other` double DEFAULT NULL COMMENT '其他',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='化学成分数据-氧化物';

--
-- Dumping data for table `MineChemistryInfo`
--

LOCK TABLES `MineChemistryInfo` WRITE;
INSERT INTO `MineChemistryInfo` VALUES ('11Y3:9-1',2.2,1.4,17.8,60.3,null,null,2.9,1,null,null,null,null,null,null,null,null,null),('11Y3:9-2',2.3,1.4,21.2,61.9,null,null,3,1,null,null,null,null,null,null,null,null,null),('11Y3:9-3',2.2,1.4,14.3,58.6,null,null,2.8,1,null,null,null,null,null,null,null,null,null);
UNLOCK TABLES;

--
-- Table structure for table `MineChemistryInfoSingle`
--

CREATE TABLE `MineChemistryInfoSingle` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品号',
  `C` double DEFAULT NULL,
  `Na` double DEFAULT NULL,
  `Mg` double DEFAULT NULL,
  `Al` double DEFAULT NULL,
  `Si` double DEFAULT NULL,
  `P` double DEFAULT NULL,
  `S` double DEFAULT NULL,
  `Cl` double DEFAULT NULL,
  `K` double DEFAULT NULL,
  `Ca` double DEFAULT NULL,
  `Ti` double DEFAULT NULL,
  `V` double DEFAULT NULL,
  `Mn` double DEFAULT NULL,
  `Fe` double DEFAULT NULL,
  `Co` double DEFAULT NULL,
  `Ni` double DEFAULT NULL,
  `Cu` double DEFAULT NULL,
  `Zn` double DEFAULT NULL,
  `As` double DEFAULT NULL,
  `Ag` double DEFAULT NULL,
  `Sn` double DEFAULT NULL,
  `Sb` double DEFAULT NULL,
  `Au` double DEFAULT NULL,
  `Hg` double DEFAULT NULL,
  `Pb` double DEFAULT NULL,
  `other` double DEFAULT NULL COMMENT '其他',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='化学成分数据-单质';

--
-- Table structure for table `MinePhysicsInfo`
--

CREATE TABLE `MinePhysicsInfo` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品号',
  `type` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '类型',
  `trueDensity` double DEFAULT NULL COMMENT '密度',
  `apparentPorosity` double DEFAULT NULL COMMENT '气孔率',
  `waterAbsorption` double DEFAULT NULL COMMENT '吸水率',
  `bending` double DEFAULT NULL COMMENT '高温抗折强度',
  `resistance` double DEFAULT NULL COMMENT '热震稳定性系数',
  `slag` double DEFAULT NULL COMMENT '抗渣性系数',
  `alkali` double DEFAULT NULL COMMENT '耐碱性系数',
  `refractoriness` double DEFAULT NULL COMMENT '荷重软化温度',
  `heat` double DEFAULT NULL COMMENT '导热系数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='物理性能数据';

--
-- Dumping data for table `MinePhysicsInfo`
--

LOCK TABLES `MinePhysicsInfo` WRITE;
INSERT INTO `MinePhysicsInfo` VALUES ('11Y3:9-1','砂泥质大块炉衬',2.612,39.5,24.8,null,null,null,null,null,null);
UNLOCK TABLES;

--
-- Table structure for table `MineThermalInfo`
--

CREATE TABLE `MineThermalInfo` (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '样品号',
  `melting` double DEFAULT NULL COMMENT '熔点',
  `fireResis` double DEFAULT NULL COMMENT '耐火度',
  `termTemper` double DEFAULT NULL COMMENT '烧成温度',
  `data` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '原始数据（Excel）',
  `surveImage` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '曲线图',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='热分析';

--
-- Dumping data for table `MineThermalInfo`
--

LOCK TABLES `MineThermalInfo` WRITE;
INSERT INTO `MineThermalInfo` VALUES ('11Y3:9-1',null,1303,1015,null,null),('11Y3:9-2',null,1306,929,null,null),('11Y3:9-3',null,1307,1025,null,null);
UNLOCK TABLES;
