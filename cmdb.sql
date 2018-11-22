-- MySQL Workbench Forward Engineering

SET FOREIGN_KEY_CHECKS=0;


CREATE TABLE IF NOT EXISTS `schema` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(48) NOT NULL,
  `desc` VARCHAR(128) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cmdb`.`filed`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `filed` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(48) NOT NULL,
  `meta` TEXT NULL,
  `schema_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_filed_schema1_idx` (`schema_id`),
  CONSTRAINT `fk_filed_schema1`
    FOREIGN KEY (`schema_id`)
    REFERENCES `schema` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cmdb`.`entity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `entity` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `key` VARCHAR(48) NOT NULL COMMENT 'weiyi',
  `schema_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_entity_schema1_idx` (`schema_id`),
  CONSTRAINT `fk_entity_schema1`
    FOREIGN KEY (`schema_id`)
    REFERENCES `schema` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cmdb`.`value`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `value` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(48) NOT NULL,
  `entity_id` BIGINT NOT NULL,
  `filed_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_table2_entity1_idx` (`entity_id`),
  KEY `fk_value_filed1_idx` (`filed_id`),
  CONSTRAINT `fk_table2_entity1`
    FOREIGN KEY (`entity_id`)
    REFERENCES `entity` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_value_filed1`
    FOREIGN KEY (`filed_id`)
    REFERENCES `filed` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

