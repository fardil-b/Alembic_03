DO $$
DECLARE
    operation VARCHAR := 'upgrade'; -- Change this to 'downgrade' when running a downgrade
BEGIN
    IF operation = 'upgrade' THEN
        -- Upgrade logic
        DROP TABLE IF EXISTS my_schema.sales;
        DROP TABLE IF EXISTS my_schema.products;
        DROP TABLE IF EXISTS my_schema.user;

        CREATE SCHEMA IF NOT EXISTS my_schema;

        CREATE TABLE my_schema.products (
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            stock INT DEFAULT 0 -- New column added
        );

        CREATE TABLE my_schema.user (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            last_login TIMESTAMP -- New column added
        );

        -- New table 'sales' added
        CREATE TABLE my_schema.sales (
            sale_id SERIAL PRIMARY KEY,
            product_id INT REFERENCES my_schema.products(product_id),
            user_id INT REFERENCES my_schema.user(user_id),
            sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            quantity INT NOT NULL,
            total_price DECIMAL(10, 2) NOT NULL
        );

        -- Insert some data into 'products' and 'user' tables
        INSERT INTO my_schema.products (name, price, stock) VALUES
        ('Product 1', 19.99, 100),
        ('Product 2', 29.99, 200),
        ('Product 3', 39.99, 150);

        INSERT INTO my_schema.user (username, password, email, last_login) VALUES
        ('user1', 'password1', 'user1@example.com', CURRENT_TIMESTAMP),
        ('user2', 'password2', 'user2@example.com', CURRENT_TIMESTAMP);

        -- Insert some data into 'sales' table
        INSERT INTO my_schema.sales (product_id, user_id, quantity, total_price) VALUES
        (1, 1, 2, 39.98),
        (2, 2, 1, 29.99),
        (3, 1, 3, 119.97);

    ELSIF operation = 'downgrade' THEN
        -- Downgrade logic
        DROP TABLE IF EXISTS my_schema.sales;
        DROP TABLE IF EXISTS my_schema.products;
        DROP TABLE IF EXISTS my_schema.user;
        DROP SCHEMA IF EXISTS my_schema;
    END IF;
END $$;
