SET SQL_SAFE_UPDATES = 0;
DELETE FROM `crm`.`icp_rules`;
DELETE FROM `crm`.`icp`;
ALTER TABLE `crm`.`icp` AUTO_INCREMENT = 1;
INSERT INTO `crm`.`icp` (attribute, weight) VALUES("City", 0.14);
INSERT INTO `crm`.`icp` (attribute, weight) VALUES("Profession", 0.29);
INSERT INTO `crm`.`icp` (attribute, weight) VALUES("Industry", 0.25);
INSERT INTO `crm`.`icp` (attribute, weight) VALUES("Age", 0.32);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(1, "QC", 10);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(1, "MANILA", 8);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(1, "ANY", 5);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(2, "IT", 10);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(2, "CS", 9);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(2, "ANY", 5);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(3, "TECH", 10);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(3, "MARKETING", 8);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(3, "COMMERCE", 6);
INSERT INTO `crm`.`icp_rules` (icp_attribute_id, attribute_value, attribute_score) VALUES(3, "ANY", 5);

-- For range 25 to 30 (score 10)
INSERT INTO crm.icp_rules (icp_attribute_id, attribute_value, attribute_score) VALUES (4, '25', 10);
INSERT INTO crm.icp_rules (icp_attribute_id, attribute_value, attribute_score) VALUES (4, '26', 10);
INSERT INTO crm.icp_rules (icp_attribute_id, attribute_value, attribute_score) VALUES (4, '27', 10);
INSERT INTO crm.icp_rules (icp_attribute_id, attribute_value, attribute_score) VALUES (4, '28', 10);
INSERT INTO crm.icp_rules (icp_attribute_id, attribute_value, attribute_score) VALUES (4, '29', 10);
INSERT INTO crm.icp_rules (icp_attribute_id, attribute_value, attribute_score) VALUES (4, '30', 10);

-- For range 31 to 35 (score 8)
INSERT INTO crm.icp_rules (icp_attribute_id, attribute_value, attribute_score) VALUES (4, '31', 8);
INSERT INTO crm.icp_rules (icp_attribute_id, attribute_value, attribute_score) VALUES (4, '32', 8);
INSERT INTO crm.icp_rules (icp_attribute_id, attribute_value, attribute_score) VALUES (4, '33', 8);
INSERT INTO crm.icp_rules (icp_attribute_id, attribute_value, attribute_score) VALUES (4, '34', 8);
INSERT INTO crm.icp_rules (icp_attribute_id, attribute_value, attribute_score) VALUES (4, '35', 8);

-- For ANY
INSERT INTO crm.icp_rules (icp_attribute_id, attribute_value, attribute_score) VALUES (4, 'ANY', 5);

SET SQL_SAFE_UPDATES = 1;