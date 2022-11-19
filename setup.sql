-- @block

CREATE TABLE  IF NOT EXISTS logins (
    username varchar(20) UNIQUE,
    permission enum('attendant', 'passenger'),
    password_hash tinytext,
    salt tinytext
) 
-- @block
CREATE TABLE IF NOT EXISTS bus_routes(
    route_num int NOT NULL PRIMARY KEY,
    route_length decimal(3,1),
    stop_count int,
    capacity int
)

-- @block
CREATE TABLE  IF NOT EXISTS stops(
    stop_id varchar(10) NOT NULL PRIMARY KEY,
    stop_name varchar(100),
    route_num int,
    latitude decimal(7,5),
    longitude decimal(7,5),
    pass_count int,
    morning_time time,
    FOREIGN KEY (route_num) REFERENCES bus_routes (route_num)
    ON DELETE CASCADE ON UPDATE CASCADE
)
-- @block

CREATE TABLE  IF NOT EXISTS passengers(
    pass_id varchar(20) UNIQUE NOT NULL ,
    pass_name varchar(50),
    route_num int,
    stop_id varchar(10) NOT NULL,
    pass_phnum char(10),    
    FOREIGN KEY (route_num) REFERENCES bus_routes (route_num)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (stop_id) REFERENCES stops (stop_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(pass_id) REFERENCES logins(username)
    ON DELETE CASCADE ON UPDATE CASCADE
    
)


-- @block

CREATE TABLE IF NOT EXISTS drivers (
    route_num int UNIQUE NOT NULL,
    driver_name varchar(50) NOT NULL,
    driver_phnum char(10),
    FOREIGN KEY (route_num) REFERENCES bus_routes (route_num)
    ON DELETE CASCADE ON UPDATE CASCADE
)
-- @block

CREATE TABLE IF NOT EXISTS conductors (
    route_num int UNIQUE NOT NULL,
    conductor_name varchar(50) NOT NULL,
    conductor_phnum char(10),
    FOREIGN KEY (route_num) REFERENCES bus_routes (route_num)
    ON DELETE CASCADE ON UPDATE CASCADE
)
-- @block

CREATE TABLE  IF NOT EXISTS attendants (
    route_num int UNIQUE NOT NULL,
    attendant_name varchar(50),
    attendant_phnum varchar(20) UNIQUE,
    FOREIGN KEY (route_num) REFERENCES bus_routes (route_num)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (attendant_phnum) REFERENCES logins (username)
    ON DELETE CASCADE ON UPDATE CASCADE
)

-- @block
select * from passengers;



