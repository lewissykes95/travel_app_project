DROP TABLE bucket-list
DROP TABLE destination
DROP TABLE country
DROP TABLE travellers; 

CREATE TABLE travellers (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
);


CREATE TABLE country (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);


CREATE TABLE destinations (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
    country_id SERIAL NOT NULL REFERENCES country(id)
);

CREATE TABLE bucket-list (
    id SERIAL PRIMARY KEY,
    traveller_id SERIAL NOT NULL REFERENCES traveller(id),
    destination_id SERIAL NOT NULL REFERENCES destination(id),
    visited BOOLEAN
);


    


