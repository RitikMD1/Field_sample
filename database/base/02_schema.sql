-- Versions
USE test;

CREATE TABLE IF NOT EXISTS versions (
  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  version VARCHAR(10) NOT NULL,
  supported TINYINT(1) NOT NULL DEFAULT 1
);

-- Roles
CREATE TABLE IF NOT EXISTS roles (
  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

-- Users
CREATE TABLE IF NOT EXISTS users (
  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(30) DEFAULT NULL,
  hashed_password LONGTEXT DEFAULT NULL,
  activated TINYINT(1) NOT NULL DEFAULT 0,
  role_id INT(6) UNSIGNED NOT NULL,
  created_at DATETIME NOT NULL,
  updated_at DATETIME DEFAULT NULL,
  salt VARCHAR(255) DEFAULT NULL,
  access_token VARCHAR(255) DEFAULT NULL,
  access_token_expiration DATETIME DEFAULT NULL,
  refresh_token VARCHAR(255) DEFAULT NULL,
  refresh_token_expiration DATETIME DEFAULT NULL,
  UNIQUE(access_token),
  UNIQUE(refresh_token),
  UNIQUE(username),
  FOREIGN KEY (role_id) REFERENCES roles(id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Items
CREATE TABLE IF NOT EXISTS items (
  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description LONGTEXT DEFAULT NULL,
  user_id INT(6) UNSIGNED NOT NULL,
  created_at DATETIME NOT NULL,
  updated_at DATETIME DEFAULT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS tokens (
  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  user_id INT(6) UNSIGNED NOT NULL,
  access_token VARCHAR(255) DEFAULT NULL,
  access_token_expiration DATETIME DEFAULT NULL,
  refresh_token VARCHAR(255) DEFAULT NULL,
  refresh_token_expiration DATETIME DEFAULT NULL,
  created_at DATETIME NOT NULL,
  UNIQUE(access_token),
  UNIQUE(refresh_token),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
);
