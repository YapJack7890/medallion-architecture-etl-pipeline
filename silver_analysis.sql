select customer_unique_id, COUNT(customer_unique_id) as customer_unique_count
from silver.customers 
group by customer_unique_id 
having COUNT(customer_unique_id) > 1 
order by COUNT(customer_unique_id);

select * from silver.customers where customer_unique_id = '004b45ec5c64187465168251cd1c9c2f';


select * from silver.order_payments;
select * from silver.order_items where order_item_id > 1 order by order_id, order_item_id;
select * from silver.orders;
select * from silver.customers;
select * from silver.sellers;

select * from silver.customers
where customer_unique_id in (
	select customer_unique_id 
	-- count(customer_unique_id) as count
	from silver.customers c 
	join silver.geolocation g
	on c.customer_zip_code_prefix = g.geolocation_zip_code_prefix 
	group by customer_unique_id 
	having COUNT(*) > 1
)
order by customer_unique_id;

SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT (order_id, order_item_id,product_id)) AS unique_ids
FROM silver.order_items;

select customer_unique_id,
count(distinct customer_zip_code_prefix) as count_unique_zip_code
from silver.customers c 
join silver.geolocation g
on c.customer_zip_code_prefix = g.geolocation_zip_code_prefix 
group by customer_unique_id 
having count(distinct customer_zip_code_prefix) > 1

select * from silver.order_payments 
where order_id ='c5bdd8ef3c0ec420232e668302179113'
order by payment_installments desc;

WITH fact AS (
    SELECT
        oi.order_id,
        -- oi.order_item_id,
        oi.product_id,
        oi.seller_id,
        o.customer_id,
        o.order_purchase_timestamp,
        op.payment_sequential,
        op.payment_value
    FROM silver.order_items oi
    JOIN silver.orders o
        ON oi.order_id = o.order_id
    JOIN silver.customers c
        ON o.customer_id = c.customer_id
    JOIN silver.sellers s
        ON oi.seller_id = s.seller_id
    LEFT JOIN silver.order_payments op
        ON o.order_id = op.order_id
)
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT (order_id, product_id, seller_id)) AS unique_rows
FROM fact;

SELECT
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'silver'
  AND table_name = 'order_payments'
ORDER BY ordinal_position;

select product_id, count(*) as occurance
from silver.products
group by product_id
having count(*) > 1;

-- prototype fact table
select o.order_id, 
	oi.product_id, 
	-- o.seller_id, 
	-- p.customer_id, 
	COUNT(oi.order_item_id) AS total_items, 
	sum(oi.price) as total_price, 
	sum(oi.freight_value) as total_freight, 
	o.order_status, 
	SUM(op.payment_value) as paid_total 
from silver.order_items oi
left join silver.orders o
on o.order_id = oi.order_id
left join silver.order_payments op 
on o.order_id = op.order_id
group by o.order_id, oi.product_id, oi.seller_id, o.customer_id, o.order_status
having sum(price) + sum(oi.freight_value) != SUM(op.payment_value)
order by order_id desc;

--cf5c8d9f52807cb2d2f0a0ff54c478da	24543438ec09114a42a153f76ae693f2
-- 54f79e394bb60e8e7d5d56756d4722b1	a25583531530c0913ea4dee2c5c73685
-- ffb9a9cd00c74c11c24aa30b3d78e03b	03bb06cda40712fb8473f7962fb7d198
-- ffb9a9cd00c74c11c24aa30b3d78e03b	3321ad579f19476d0d668f726f8dffec
-- ffb9a9cd00c74c11c24aa30b3d78e03b	fec565c4e3ad965c73fb1a21bb809257

SELECT *
FROM silver.order_items
WHERE order_id = 'ffb9a9cd00c74c11c24aa30b3d78e03b'
and product_id in (
'03bb06cda40712fb8473f7962fb7d198', 
'3321ad579f19476d0d668f726f8dffec', 
'fec565c4e3ad965c73fb1a21bb809257');

SELECT *
FROM silver.customers
WHERE customer_id = '9ed5e522dd9dd85b4af4a077526d8117';

SELECT *
FROM silver.order_payments
WHERE order_id = 'ffb9a9cd00c74c11c24aa30b3d78e03b';

SELECT *
FROM silver.customers s
left join silver.geolocation g 
on s.customer_zip_code_prefix = g.geolocation_zip_code_prefix 
where geolocation_zip_code_prefix is null;

DROP TABLE IF EXISTS silver.order_items CASCADE;
DROP TABLE IF EXISTS silver.order_payments CASCADE;
DROP TABLE IF EXISTS silver.order_reviews CASCADE;
DROP TABLE IF EXISTS silver.orders CASCADE;
DROP TABLE IF EXISTS silver.products CASCADE;
DROP TABLE IF EXISTS silver.product_category_translation CASCADE;
DROP TABLE IF EXISTS silver.sellers CASCADE;
DROP TABLE IF EXISTS silver.customers CASCADE;
DROP TABLE IF EXISTS silver.geolocation CASCADE;

TRUNCATE TABLE silver.order_items CASCADE;
TRUNCATE TABLE silver.order_payments CASCADE;
TRUNCATE TABLE silver.order_reviews CASCADE;
TRUNCATE TABLE silver.orders CASCADE;
TRUNCATE TABLE silver.products CASCADE;
TRUNCATE TABLE silver.sellers CASCADE;
TRUNCATE TABLE silver.customers CASCADE;
TRUNCATE TABLE silver.geolocation CASCADE;

select * from silver.order_reviews
