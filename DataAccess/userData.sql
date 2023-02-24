CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `registration_date` date NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `store_name` varchar(255) NOT NULL,
  `store_address` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
);

