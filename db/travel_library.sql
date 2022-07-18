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
    continent VARCHAR(255)
);

-- CREATE TABLE bucket_list (
--     id SERIAL PRIMARY KEY, 
--     traveller_id INT NOT NULL REFERENCES travellers(id) ON DELETE CASCADE, 
--     destination_id INT NOT NULL REFERENCES destinations(id) ON DELETE CASCADE,
--     review TEXT
-- );