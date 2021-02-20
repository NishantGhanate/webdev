CREATE TABLE test.user (
    id VARCHAR(10) PRIMARY KEY,
    real_name VARCHAR(50),
    time_zone VARCHAR(30),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE test.user_activity(
    id INT NOT NULL AUTO_INCREMENT,
    user_id VARCHAR(10),
    start_time VARCHAR(30),
    end_time VARCHAR(30),
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES user (id)
);