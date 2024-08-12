-- Creating idx_name_first on the table names
-- and first letter of the name
CREATE INDEX idx_name_first ON names (name(1));
