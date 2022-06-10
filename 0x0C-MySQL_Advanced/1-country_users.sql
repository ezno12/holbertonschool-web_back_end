-- create table users
-- with attributes: id, email, name, country (US, CO, TN)
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM("US", "CO", "TN") NOT NULL
)
