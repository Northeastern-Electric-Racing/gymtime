CREATE TABLE `record` (
  `id` int NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL,
  `count` int NOT NULL,
  `percent` int NOT NULL,
  `section_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40256 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
