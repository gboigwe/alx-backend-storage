-- Create trigger to decrease item quantity after adding a new order
DELIMITER //

CREATE TRIGGER quant_decresa
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE id = NEW.item_id;
END//

DELIMITER ;
