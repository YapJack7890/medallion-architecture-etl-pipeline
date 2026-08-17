-- ============================================
-- CUSTOMERS
-- ============================================
CREATE TABLE bronze.customers (
    customer_id VARCHAR(50),
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix INTEGER,
    customer_city VARCHAR(100),
    customer_state CHAR(2)
);

-- ============================================
-- GEOLOCATION
-- No primary key because duplicate ZIP codes
-- exist in the original dataset.
-- ============================================
CREATE TABLE bronze.geolocation (
    geolocation_zip_code_prefix INTEGER,
    geolocation_lat DECIMAL(10,8),
    geolocation_lng DECIMAL(11,8),
    geolocation_city VARCHAR(100),
    geolocation_state CHAR(2) 
);

-- ============================================
-- PRODUCT CATEGORY TRANSLATION
-- ============================================
CREATE TABLE bronze.product_category_name_translation (
    product_category_name VARCHAR(100),
    product_category_name_english VARCHAR(100) 
);

-- ============================================
-- PRODUCTS
-- ============================================
CREATE TABLE bronze.products (
    product_id VARCHAR(50),
    product_category_name VARCHAR(100),
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
CREATE TABLE bronze.sellers (
    seller_id VARCHAR(50),
    seller_zip_code_prefix INTEGER,
    seller_city VARCHAR(100),
    seller_state CHAR(2) 
);

-- ============================================
-- ORDERS
-- ============================================
CREATE TABLE bronze.orders (
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    order_status VARCHAR(30),
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP
);

-- ============================================
-- ORDER ITEMS
-- Composite PK because one order can contain
-- multiple items.
-- ============================================
CREATE TABLE bronze.order_items (
    order_id VARCHAR(50),
    order_item_id INTEGER,
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date TIMESTAMP,
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2)
);

-- ============================================
-- ORDER PAYMENTS
-- Composite PK because an order may have
-- multiple payment records.
-- ============================================
CREATE TABLE bronze.order_payments (
    order_id VARCHAR(50),
    payment_sequential INTEGER,
    payment_type VARCHAR(30),
    payment_installments INTEGER,
    payment_value DECIMAL(10,2)
);

-- ============================================
-- ORDER REVIEWS
-- ============================================
CREATE TABLE bronze.order_reviews (
    review_id VARCHAR(50),
    order_id VARCHAR(50),
    review_score INTEGER,
    review_comment_title TEXT,
    review_comment_message TEXT,
    review_creation_date TIMESTAMP,
    review_answer_timestamp TIMESTAMP
);

