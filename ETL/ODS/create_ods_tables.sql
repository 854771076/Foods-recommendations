create database ods_foods;

CREATE TABLE `ods_foods`.`ods_foods_db_spider_t_foods` (
  `id` int,
  `name` string,
  `url` string,
  `raw` string,
  `type` string,
  `img` string,
  `raw_detail` string,
  `cookbook_make` string,
  `crawler_date` timestamp,
  `cdc_sync_date` timestamp
) PARTITIONED BY (partition_date string);

CREATE TABLE `ods_foods`.`ods_foods_db_foods_t_resume` (
  `id` int,
  `type1` int,
  `type1Translation` string,
  `type2` int,
  `type2Translation` string,
  `type3` int,
  `type3Translation` string,
  `created_time`  timestamp,
  `last_update`  timestamp,
  `user_id` int,
  `cdc_sync_date` timestamp
) PARTITIONED BY (partition_date string);
