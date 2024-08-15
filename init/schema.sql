CREATE DATABASE IF NOT EXISTS clean_database;

CREATE TABLE IF NOT EXISTS `clean_database`.`users` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    fist_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(60) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY (id)
);