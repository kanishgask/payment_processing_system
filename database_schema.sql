CREATE TABLE users (
user_id INT PRIMARY KEY,
name VARCHAR(100)
);

CREATE TABLE payments (
payment_id INT PRIMARY KEY,
user_id INT,
amount DECIMAL,
status VARCHAR(50)
);

CREATE TABLE transactions (
transaction_id INT PRIMARY KEY,
payment_id INT,
amount DECIMAL,
status VARCHAR(50)
);
