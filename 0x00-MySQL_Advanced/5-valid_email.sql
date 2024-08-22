-- This script creates a trigger that resets the 'valid_email' attribute
-- in the 'users' table to 0 when the 'email' column is updated.
-- The trigger ensures that the 'valid_email' field is only updated if the email value has changed.
DROP TRIGGER IF EXISTS reset_valid_email;

DELIMITER $$

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END $$

DELIMITER ;