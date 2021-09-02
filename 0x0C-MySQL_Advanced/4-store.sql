-- 4. Buy buy buy
--  decrease the quantity of an item after adding a new order
CREATE TRIGGER update_quantity
    AFTER INSERT on orders
    FOR EACH ROW
        UPDATE items
        SET items.quantity = items.quantity - NEW.number
        WHERE items.name = NEW.item_name