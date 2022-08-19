-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema login_red
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema login_red
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `login_red` DEFAULT CHARACTER SET utf8 ;
USE `login_red` ;

-- -----------------------------------------------------
-- Table `login_red`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `login_red`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(55) NULL,
  `last_name` VARCHAR(95) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `login_red`.`recetas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `login_red`.`recetas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre_receta` VARCHAR(250) NULL,
  `descripcion` TEXT NULL,
  `instrucciones` TEXT NULL,
  `fecha_creacion` DATE NULL,
  `menor30` TINYINT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `creador_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recetas_users_idx` (`creador_id` ASC) VISIBLE,
  CONSTRAINT `fk_recetas_users`
    FOREIGN KEY (`creador_id`)
    REFERENCES `login_red`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
