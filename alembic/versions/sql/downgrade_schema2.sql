DO $$
BEGIN
    -- Downgrade logic
    DROP TABLE IF EXISTS my_schema.sales CASCADE;
    DROP TABLE IF EXISTS my_schema.products CASCADE;
    DROP TABLE IF EXISTS my_schema.user CASCADE;
    DROP SCHEMA IF EXISTS my_schema CASCADE;
END $$;
