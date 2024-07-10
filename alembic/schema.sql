-- schema.sql
CREATE SCHEMA IF NOT EXISTS my_schema;

CREATE TABLE my_schema.user2 (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE my_schema.products2 (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);
