CREATE DATABASE IF NOT EXISTS soc2;

USE soc2;

CREATE TABLE `authors` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `author` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `publications` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `pub_key` varchar(255) DEFAULT NULL,
  `pub_type` varchar(15) NOT NULL DEFAULT '',
  `editor` mediumtext,
  `title` varchar(1024) DEFAULT NULL,
  `booktitle` varchar(1024) DEFAULT NULL,
  `pages` varchar(255) DEFAULT NULL,
  `pub_year` int(11) DEFAULT NULL,
  `address` mediumtext,
  `journal` mediumtext,
  `volume` varchar(100) DEFAULT NULL,
  `number` varchar(100) DEFAULT NULL,
  `pub_month` varchar(10) DEFAULT NULL,
  `url` varchar(1000) DEFAULT NULL,
  `ee` varchar(1000) DEFAULT NULL,
  `cdrom` varchar(1000) DEFAULT NULL,
  `cite` mediumtext,
  `publisher` varchar(1024) DEFAULT NULL,
  `note` mediumtext,
  `crossref` mediumtext,
  `isbn` varchar(1000) DEFAULT NULL,
  `series` varchar(1000) DEFAULT NULL,
  `school` varchar(1024) DEFAULT NULL,
  `chapter` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `authors_publications` (
  `author_id` int(11) unsigned NOT NULL,
  `publication_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`author_id`,`publication_id`),
  KEY `publication_pk` (`publication_id`),
  CONSTRAINT `author_pk` FOREIGN KEY (`author_id`) REFERENCES `authors` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `publication_pk` FOREIGN KEY (`publication_id`) REFERENCES `publications` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
