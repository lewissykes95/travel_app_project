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

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visits INTEGER
    traveller_id SERIAL NOT NULL REFERENCES travellers(id),
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255)
)


    


