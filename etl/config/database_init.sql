CREATE DATABASE brazilian_ecommerce_dw;

CREATE SCHEMA IF NOT EXISTS bronze;

CREATE SCHEMA IF NOT EXISTS silver;

CREATE SCHEMA IF NOT EXISTS gold;

SELECT current_database();

SELECT schema_name
FROM information_schema.schemata
ORDER BY schema_name;