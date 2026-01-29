from db_manager import db_query

class Inventory:
    @staticmethod
    def add_blood(blood_type, quantity=1):
        result = db_query("SELECT quantity FROM inventory WHERE blood_type = %s", (blood_type,))
        if not result:
            return # Handle error?
        current_qty = result[0][0]
        new_qty = current_qty + quantity
        db_query("UPDATE inventory SET quantity = %s WHERE blood_type = %s", (new_qty, blood_type))

    @staticmethod
    def deduct_blood(blood_type, quantity=1):
        result = db_query("SELECT quantity FROM inventory WHERE blood_type = %s", (blood_type,))
        if not result:
            print(f"Error: Blood type {blood_type} not found")
            return

        current_qty = result[0][0]
        if current_qty < quantity:
            print(f"Not enough blood for {blood_type}")
        else:
            db_query("UPDATE inventory SET quantity = %s WHERE blood_type = %s", (current_qty - quantity, blood_type))
