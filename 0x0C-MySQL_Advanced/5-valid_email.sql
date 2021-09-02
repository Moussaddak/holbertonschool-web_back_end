-- 5. Email validation to sent
-- create a trigger that resets the attribute valid_email
CREATE TRIGGER email_IsValid
    BEFORE UPDATE ON users
    FOR EACH ROW
    BEGIN
        IF NEW.email <> old.email
        THEN
            SET NEW.valid_email = 0;
        END IF;
    END; //
delimiter ;