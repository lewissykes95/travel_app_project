DROP TABLE destinations;
DROP TABLE travellers; 

CREATE TABLE travellers (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
    age INTEGER
);

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY, 
    city VARCHAR(255),
    country VARCHAR(255),
    duration VARCHAR(255),
    checked_off BOOLEAN, 
    traveller_id INT NOT NULL REFERENCES travellers(id)
);

CREATE TABLE visits (
    id SERIAL PRIMARY KEY,
    destination_id SERIAL NOT NULL REFERENCES destinations(id),
    traveller_id SERIAL NOT NULL REFERENCES travellers(id)
);


