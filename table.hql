set hive.exec.mode.local.auto=true;
set hive.exec.mode.local.auto.inputbytes.max=1150000000;
set hive.exec.mode.local.auto.input.files.max=10;

CREATE database IF NOT EXISTS gzh;

use gzh;
-- 加载科技领域公众号csv数据到到hive表格里
CREATE TABLE IF NOT EXISTS gzh_all(
    timefield STRING,
    dates STRING,
    class STRING,
    subclass STRING,
    province string,
    city string,
    district string,
    ranking INT,
    name STRING,
    id string,
    passage_count INT,
    read INT,
    read_viral INT,
    read_avg INT,
    tops INT,
    likes INT,
    forward INT,
    wci DECIMAL(10, 2),
    avatar string
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH 'Documents/202412work/science.csv' INTO TABLE gzh_kj;

-- 查看gzh-kj的数据
SELECT * FROM gzh_kj;
-- 查看gzh-kj的数据规模
SELECT COUNT(*) FROM gzh_kj;

-- 去重
CREATE TABLE IF NOT EXISTS gzh_kj2 AS
SELECT DISTINCT * FROM gzh_kj2;

-- 保留需要的字段构建新表
CREATE TABLE IF NOT EXISTS gzh_kj3 AS
SELECT dates,ranking,name,id,passage_count,read,read_viral,read_avg,tops,likes,forward,wci,avatar
FROM gzh_kj2;

-- 查看gzh-kj3的数据结构
DESCRIBE gzh_kj3;

-- 基于gzh_kj3构建透视表，字段包括各项指标在每日的计算值，其中wci、read_avg求均值，其他求和
CREATE TABLE IF NOT EXISTS gzh_kjts AS
SELECT dates,
    SUM(passage_count) AS passage_count,
    SUM(read) AS read,
    SUM(read_viral) AS read_viral,
    AVG(read_avg) AS read_avg,
    SUM(tops) AS tops,
    SUM(likes) AS likes,
    SUM(forward) AS forward,
    AVG(wci) AS wci
FROM gzh_kj3
GROUP BY dates;


-- 加载全领域公众号csv数据到到hive表格里
CREATE TABLE IF NOT EXISTS gzh_all(
    timefield STRING,
    dates STRING,
    class STRING,
    subclass STRING,
    province string,
    city string,
    district string,
    ranking INT,
    name STRING,
    id string,
    passage_count INT,
    read INT,
    read_viral INT,
    read_avg INT,
    tops INT,
    likes INT,
    forward INT,
    wci DECIMAL(10, 2),
    avatar string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH 'Documents/202412work/allclass.csv' INTO TABLE gzh_all;

-- 查看gzh_all的数据
SELECT * FROM gzh_all LIMIT 10;

-- 查看gzh_all的数据结构
DESCRIBE gzh_all;
-- 找出所有重复的dates的记录
SELECT dates from gzh_all GROUP BY dates;


-- 把“likes”字段中含有"W+"的值替换成“0000”，并把字段转为INT类型
ALTER TABLE gzh_all ADD COLUMN likes_new INT;
UPDATE gzh_all SET likes_new = CASE 
WHEN likes LIKE '%W+%' THEN 0000 
ELSE CAST(likes AS INT) END;
ALTER TABLE gzh_all ADD COLUMN forward_new INT;
UPDATE gzh_all SET forward_new = CASE 
WHEN forward LIKE '%W+%' 
THEN 0000 ELSE CAST(forward AS INT) END;
ALTER TABLE gzh_all ADD COLUMN read_new INT;
UPDATE gzh_all SET read_new = CASE WHEN read LIKE '%W+%' THEN 0000 ELSE CAST(read AS INT) END;

-- 把forward字段中含有“--”的值都改成0，并把字段转为INT类型
UPDATE gzh_all SET forward_new = CASE 
WHEN forward LIKE '%--%' 
THEN 0 ELSE forward_new END;

-- 使用平均阅读*篇数来重新给阅读数赋值，并删除原来的阅读字段
ALTER TABLE gzh_all ADD COLUMN read_avg INT;
UPDATE gzh_all SET read_avg = read_new / passage_count;
ALTER TABLE gzh_all DROP COLUMN read;
ALTER TABLE gzh_all DROP COLUMN read_new;


-- 保留需要的字段构建新表
CREATE TABLE IF NOT EXISTS gzh_all2 AS
SELECT dates,ranking,name,id,passage_count,read,read_viral,read_avg,tops,likes,forward,wci,avatar
FROM gzh_all;

-- 全领域的透视表
CREATE TABLE IF NOT EXISTS gzh_allts AS
SELECT dates,
    SUM(passage_count) AS passage_count,
    SUM(read) AS read,
    SUM(read_viral) AS read_viral,
    AVG(read_avg) AS read_avg,
    SUM(tops) AS tops,
    SUM(likes) AS likes,
    SUM(forward) AS forward,
    AVG(wci) AS wci
FROM gzh_all
GROUP BY dates;

-- 导出gzh_all，格式是csv文件
INSERT OVERWRITE LOCAL DIRECTORY 'Documents/202412work' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM gzh_allts;
INSERT OVERWRITE LOCAL DIRECTORY 'Documents/202412work/gzh_all.csv' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM gzh_all;

-- 把上面所有的表导出到csv文件，一共6个
INSERT OVERWRITE LOCAL DIRECTORY 'Documents/202412work' 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
SELECT * FROM gzh_allts;
INSERT OVERWRITE LOCAL DIRECTORY 'Documents/202412work/gzh_all.csv' 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
SELECT * FROM gzh_all;
INSERT OVERWRITE LOCAL DIRECTORY 'Documents/202412work/gzh_kj.csv' 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
SELECT * FROM gzh_kjts;
INSERT OVERWRITE LOCAL DIRECTORY 'Documents/202412work' 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
SELECT * FROM gzh_allts;
INSERT OVERWRITE LOCAL DIRECTORY 'Documents/202412work/gzh_all.csv' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM gzh_all;
INSERT OVERWRITE LOCAL DIRECTORY 'Documents/202412work/gzh_kj.csv' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM gzh_kjts;