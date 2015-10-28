
-- Progress
SELECT `option`.`display` AS "TAG", (count(*)) AS "COUNT" FROM `item`
       JOIN `option` ON `option`.`id` = `tag` GROUP BY `tag`;