
DROP DATABASE IF EXISTS vlbk7122d7cbev23;
CREATE DATABASE vlbk7122d7cbev23;
USE vlbk7122d7cbev23;

CREATE TABLE activities (
  recid INT NOT NULL AUTO_INCREMENT,
  id INT, 
  name VARCHAR(20), 
  live BOOL, 
  created_at VARCHAR(30), 
  updated_at VARCHAR(30), 
  absolute_min_players INT, 
  absolute_max_players INT, 
  duration INT, 
  default_min_players INT, 
  default_max_players INT, 
  icon_name VARCHAR(30),
  PRIMARY KEY (recid)
);


CREATE TABLE locations (
  rec_loc_id INT NOT NULL AUTO_INCREMENT,
  id INT, 
  name VARCHAR(60), 
  area VARCHAR(20), 
  address VARCHAR(60), 
  venue_type VARCHAR(30), 
  is_outdoor BOOL, 
  phone VARCHAR(20), 
  cost VARCHAR(10), 
  activity_id INT, 
  activity_accomodations VARCHAR(20), 
  courts_fields_count INT, 
  quality INT, 
  created_at VARCHAR(30), 
  updated_at VARCHAR(30),  
  longitude DOUBLE, 
  latitude DOUBLE, 
  image1 VARCHAR(60), 
  image2 VARCHAR(60), 
  image3 VARCHAR(60), 
  activity_name VARCHAR(30), 
  distance_from_center DOUBLE,
  PRIMARY KEY (rec_loc_id)
);

