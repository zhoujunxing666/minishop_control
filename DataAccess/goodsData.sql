CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_cn` varchar(255) NOT NULL,
  `name_en` varchar(255) NOT NULL,
  `barcode` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `production_date` date DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `cost_price` decimal(10,2) NOT NULL,
  `selling_price` decimal(10,2) NOT NULL,
  `type` varchar(255) NOT NULL,
  `expiry_notification_date` date DEFAULT NULL,
  `inventory` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);
