-- combined_schema.sql

DO $$
DECLARE
    operation VARCHAR := 'upgrade'; -- Change this to 'downgrade' when running a downgrade
BEGIN
    IF operation = 'upgrade' THEN
        -- Upgrade logic
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

    ELSIF operation = 'downgrade' THEN
        -- Downgrade logic
        DROP TABLE IF EXISTS my_schema.products;
        DROP TABLE IF EXISTS my_schema.user;
        DROP SCHEMA IF EXISTS my_schema;
    END IF;
END $$;
