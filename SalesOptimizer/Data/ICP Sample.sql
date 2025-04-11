-- This SQL File Resets and Inserts the default ICP configuration Data into the database
-- Executing this will reset the table 'icp' , and 'icp_rules' and may affect the 'lead_score' table data.

SET SQL_SAFE_UPDATES = 0;

DELETE FROM `crm`.`icp_rules`;
DELETE FROM `crm`.`icp`;

-- ICP Table Insert -----------------------------------------------------------------

-- Reset Foreign Key to 1
ALTER TABLE `crm`.`icp` AUTO_INCREMENT = 1;

INSERT INTO `crm`.`icp` (attribute, weight) VALUES("Demographics", 0.14);
INSERT INTO `crm`.`icp` (attribute, weight) VALUES("Profession", 0.28);
INSERT INTO `crm`.`icp` (attribute, weight) VALUES("Industry", 0.25);
INSERT INTO `crm`.`icp` (attribute, weight) VALUES("Age", 0.32);

-- View Table 
select * from `crm`.`icp` ORDER BY attribute_id ASC;






-- ICP Rules Table Insert -----------------------------------------------------------------

-- Location
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(1, "QC", 10);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(1, "MANILA", 8);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(1, "ANY", 5);

-- Profession
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(2, "IT", 10);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(2, "CS", 9);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(2, "ANY", 5);

-- Industry
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(3, "TECH", 10);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(3, "MARKETING", 8);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(3, "COMMERCE", 6);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(3, "ANY", 5);

-- Age
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(4, "25 <= X >= 30", 10);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(4, "31 <= X >= 35", 8);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(4, "ANY", 5);

-- View Table 
select * from `crm`.`icp_rules` ORDER BY icp_attribute_id ASC, attribute_score DESC;




SET SQL_SAFE_UPDATES = 1;