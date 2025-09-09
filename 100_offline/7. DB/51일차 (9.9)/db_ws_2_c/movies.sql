USE restaurant_db

DELETE FROM menus
WHERE item_name = 'Salmon Nigiri';
ALTER TABLE menus DROP FOREIGN KEY menus_ibfk_1;

DELETE FROM restaurants
WHERE name = 'Pasta Paradise';
