SELECT * 
FROM Customer
WHERE cust_name LIKE 'a%';

SELECT * 
FROM Customer
WHERE cust_name LIKE '%or%';

SELECT Customer.cust_name, Product.pro_name, Country.country_name
FROM Customer
JOIN Orders ON Customer.customer_id = Orders.customer_id
JOIN Product ON Orders.product_id = Product.product_id
JOIN Country ON Customer.country_id = Country.country_id;