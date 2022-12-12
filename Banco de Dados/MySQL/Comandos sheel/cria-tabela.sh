CREATE TABLE `posts` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `titulo` VARCHAR(255) NOT NULL,
    `conteudo` TEXT NOT NULL,
    `autor_id` INT NOT NULL,
    PRIMARY KEY(`id`)
    ) ENGINE=InnoDB

CREATE TABLE `autores` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nome` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
    ) ENGINE=InnoDB