select item_id, item_name, total_price, price, pos from item NATURAL JOIN item_pos where item_name like '%刃%';