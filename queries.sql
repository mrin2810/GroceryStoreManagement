-- CREATE TABLE grocery_store.products (
--     product_id INT NOT NULL AUTO_INCREMENT,
--     name VARCHAR(100) NOT NULL,
--     uom_id INT NOT NULL,
--     price_per_unit DOUBLE NOT NULL,
--     PRIMARY KEY (product_id)
-- );

-- CREATE TABLE grocery_store.uom (
-- uom_id INT NOT NULL AUTO_INCREMENT,
-- uom_name VARCHAR(45) NOT NULL, PRIMARY KEY (uom_id));

-- ALTER TABLE grocery_store.products
-- ADD CONSTRAINT fk_uom_id
-- FOREIGN KEY (uom_id)
-- REFERENCES uom(uom_id);

-- Create table grocery_store.orders (
-- 	order_id INT NOT NULL AUTO_INCREMENT,
--     customer_name VARCHAR(100) NOT NULL,
--     total DOUBLE NOT NULL,
--     datetime DATETIME NOT NULL,
--     primary key (order_id)
--     );

-- CREATE TABLE grocery_store.order (
-- 	order_id INT NOT NULL AUTO_INCREMENT,
--     product_id INT NOT NULL,
--     quantity DOUBLE NOT NULL,
--     total_price DOUBLE NOT NULL,
--     primary key (order_id),
--     FOREIGN KEY (order_id) REFERENCES orders(order_id),
--     FOREIGN KEY (product_id) REFERENCES products(product_id)
-- )