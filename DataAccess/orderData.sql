CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `order_date` date NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  FOREIGN KEY (`goods_id`) REFERENCES `goods` (`id`)
);
