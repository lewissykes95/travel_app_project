DROP TABLE destinations;
DROP TABLE travellers; 

CREATE TABLE travellers (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
    age INT NULL O
);


CREATE TABLE destinations (
    id SERIAL PRIMARY KEY, 
    city VARCHAR(255),
    country VARCHAR(255),
    continet VARCHAR(255)
);