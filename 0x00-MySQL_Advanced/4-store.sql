-- Creating a trigger to decrease item quantity after adding a new order
CREATE TRIGGER trigger_create
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
