-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema The_X_Files
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema The_X_Files
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `The_X_Files` DEFAULT CHARACTER SET utf8 ;
USE `The_X_Files` ;

-- -----------------------------------------------------
-- Table `The_X_Files`.`Characters`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `The_X_Files`.`Characters` (
  `idCharacters` INT NOT NULL AUTO_INCREMENT,
  `Character` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idCharacters`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `The_X_Files`.`Scenes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `The_X_Files`.`Scenes` (
  `idScenes` INT NOT NULL AUTO_INCREMENT,
  `Scenescol` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idScenes`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `The_X_Files`.`Dialogues`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `The_X_Files`.`Dialogues` (
  `idDialogues` INT NOT NULL AUTO_INCREMENT,
  `Phrase` VARCHAR(5000) NOT NULL,
  `Characters_idCharacters` INT NOT NULL,
  PRIMARY KEY (`idDialogues`),
  INDEX `fk_Dialogues_Characters_idx` (`Characters_idCharacters` ASC) VISIBLE,
  CONSTRAINT `fk_Dialogues_Characters`
    FOREIGN KEY (`Characters_idCharacters`)
    REFERENCES `The_X_Files`.`Characters` (`idCharacters`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `The_X_Files`.`Scenes_has_Characters`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `The_X_Files`.`Scenes_has_Characters` (
  `Scenes_idScenes` INT NOT NULL,
  `Characters_idCharacters` INT NOT NULL,
  PRIMARY KEY (`Scenes_idScenes`, `Characters_idCharacters`),
  INDEX `fk_Scenes_has_Characters_Characters1_idx` (`Characters_idCharacters` ASC) VISIBLE,
  INDEX `fk_Scenes_has_Characters_Scenes1_idx` (`Scenes_idScenes` ASC) VISIBLE,
  CONSTRAINT `fk_Scenes_has_Characters_Scenes1`
    FOREIGN KEY (`Scenes_idScenes`)
    REFERENCES `The_X_Files`.`Scenes` (`idScenes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Scenes_has_Characters_Characters1`
    FOREIGN KEY (`Characters_idCharacters`)
    REFERENCES `The_X_Files`.`Characters` (`idCharacters`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `The_X_Files`.`Dialogues_has_Scenes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `The_X_Files`.`Dialogues_has_Scenes` (
  `Dialogues_idDialogues` INT NOT NULL,
  `Scenes_idScenes` INT NOT NULL,
  PRIMARY KEY (`Dialogues_idDialogues`, `Scenes_idScenes`),
  INDEX `fk_Dialogues_has_Scenes_Scenes1_idx` (`Scenes_idScenes` ASC) VISIBLE,
  INDEX `fk_Dialogues_has_Scenes_Dialogues1_idx` (`Dialogues_idDialogues` ASC) VISIBLE,
  CONSTRAINT `fk_Dialogues_has_Scenes_Dialogues1`
    FOREIGN KEY (`Dialogues_idDialogues`)
    REFERENCES `The_X_Files`.`Dialogues` (`idDialogues`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Dialogues_has_Scenes_Scenes1`
    FOREIGN KEY (`Scenes_idScenes`)
    REFERENCES `The_X_Files`.`Scenes` (`idScenes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
