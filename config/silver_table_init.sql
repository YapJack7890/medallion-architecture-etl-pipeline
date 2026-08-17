-- ============================================
-- CUSTOMERS
-- ============================================
CREATE TABLE silver.customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_unique_id VARCHAR(50) NOT NULL,
    customer_zip_code_prefix INTEGER NOT NULL
    -- customer_city VARCHAR(100) NOT NULL,
    -- customer_state CHAR(2) NOT NULL
);

-- ============================================
-- GEOLOCATION
-- No primary key because duplicate ZIP codes
-- exist in the original dataset.
-- ============================================
CREATE TABLE silver.geolocation (
    geolocation_zip_code_prefix INTEGER NOT NULL,
    geolocation_lat DECIMAL(10,8) NOT NULL,
    geolocation_lng DECIMAL(11,8) NOT NULL,
    geolocation_city VARCHAR(100) NOT NULL,
    geolocation_state CHAR(2) NOT NULL
);

-- ============================================
-- PRODUCT CATEGORY TRANSLATION
-- ============================================
--CREATE TABLE silver.product_category_name_translation (
--    product_category_name VARCHAR(100) PRIMARY KEY,
--    product_category_name_english VARCHAR(100) NOT NULL
--);

-- ============================================
-- PRODUCTS
-- ============================================
CREATE TABLE silver.products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_category_name_english VARCHAR(100),
    product_name_lenght INTEGER,
    product_description_lenght INTEGER,
    product_photos_qty INTEGER,
    product_weight_g DECIMAL(10,2),
    product_length_cm DECIMAL(10,2),
    product_height_cm DECIMAL(10,2),
    product_width_cm DECIMAL(10,2)
);

-- ============================================
-- SELLERS
-- ============================================
CREATE TABLE silver.sellers (
    seller_id VARCHAR(50) PRIMARY KEY,
    seller_zip_code_prefix INTEGER NOT NULL
    -- seller_city VARCHAR(100) NOT NULL,
    -- seller_state CHAR(2) NOT NULL
);

-- ============================================
-- ORDERS
-- ============================================
CREATE TABLE silver.orders (
    order_id VARCHAR(50) PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL,
    order_status VARCHAR(30),
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP,

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES silver.customers(customer_id)
);

-- ============================================
-- ORDER ITEMS
-- Composite PK because one order can contain
-- multiple items.
-- ============================================
CREATE TABLE silver.order_items (
    order_id VARCHAR(50) NOT NULL,
    order_item_id INTEGER NOT NULL,
    product_id VARCHAR(50) NOT NULL,
    seller_id VARCHAR(50) NOT NULL,
    shipping_limit_date TIMESTAMP NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    freight_value DECIMAL(10,2) NOT NULL,

    PRIMARY KEY (order_id, order_item_id),

    CONSTRAINT fk_order_items_order
        FOREIGN KEY (order_id)
        REFERENCES silver.orders(order_id),

    CONSTRAINT fk_order_items_product
        FOREIGN KEY (product_id)
        REFERENCES silver.products(product_id),

    CONSTRAINT fk_order_items_seller
        FOREIGN KEY (seller_id)
        REFERENCES silver.sellers(seller_id)
);

-- ============================================
-- ORDER PAYMENTS
-- Composite PK because an order may have
-- multiple payment records.
-- ============================================
CREATE TABLE silver.order_payments (
    order_id VARCHAR(50) NOT NULL,
    payment_sequential INTEGER NOT NULL,
    payment_type VARCHAR(30) NOT NULL,
    payment_installments INTEGER NOT NULL,
    payment_value DECIMAL(10,2) NOT NULL,

    PRIMARY KEY (order_id, payment_sequential),

    CONSTRAINT fk_order_payments_order
        FOREIGN KEY (order_id)
        REFERENCES silver.orders(order_id)
);

-- ============================================
-- ORDER REVIEWS
-- ============================================
CREATE TABLE silver.order_reviews (
    review_id VARCHAR(50) not NULL,
    order_id VARCHAR(50) NOT NULL,
    review_score INTEGER NOT NULL,
    review_comment_title TEXT,
    review_comment_message TEXT,
    review_creation_date TIMESTAMP,
    review_answer_timestamp TIMESTAMP,
    
    PRIMARY KEY (order_id, review_id),

    CONSTRAINT fk_order_reviews_order
        FOREIGN KEY (order_id)
        REFERENCES silver.orders(order_id)
);
--
--CREATE TABLE silver.load_history (
--    batch_id UUID PRIMARY KEY,
--    table_name VARCHAR(100) NOT NULL,
--    batch_name VARCHAR(255) NOT NULL,
--    file_path TEXT NOT NULL,
--    ingestion_timestamp TIMESTAMP NOT NULL,
--    processed_at TIMESTAMP,
--    status VARCHAR(20) NOT NULL,
--    rows_processed INTEGER,
--    checksum VARCHAR(64),
--    error_message TEXT
--);
