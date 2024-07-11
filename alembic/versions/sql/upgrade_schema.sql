-- upgrade_schema.sql

DROP TABLE IF EXISTS my_schema.products;
DROP TABLE IF EXISTS my_schema.user;

CREATE SCHEMA IF NOT EXISTS my_schema;

CREATE TABLE my_schema.products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE my_schema.user (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);
