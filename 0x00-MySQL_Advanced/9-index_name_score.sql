-- Creating idx_name_first on the table names
-- and first letter of the name and he score
CREATE INDEX idx_name_first_score ON names (name(1), score);
