-- Create the crimes table
CREATE TABLE IF NOT EXISTS crimes (
    Crime_id SERIAL PRIMARY KEY,            -- Auto-incremented primary key in PostgreSQL
    Category VARCHAR(100) NOT NULL,
    Subcategory VARCHAR(100) NOT NULL,
    Crime_discreption TEXT NOT NULL,
    Date DATE NOT NULL,
    Location VARCHAR(150),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Insert example crime records
INSERT INTO crimes (Category, Subcategory, Crime_discreption, Date, Location)
VALUES 
('Theft', 'Bicycle Theft', 'A person stole a bicycle from the park.', '2024-10-25', 'Central Park'),
('Burglary', 'Residential Burglary', 'A house was broken into during the night.', '2024-10-26', '123 Main St'),
('Assault', 'Physical Assault', 'A physical fight occurred at the bar.', '2024-10-27', 'Downtown Bar');

-- Query to check the inserted records
SELECT *
FROM crimes
LIMIT 10;
