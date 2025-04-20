class Inventory:
    @staticmethod
    def add_blood(blood_type, quantity=1):
        result = db_query("SELECT quantity FROM inventory WHERE blood_type = ?", (blood_type,))
        result = result[0][0] + quantity
        db_query("UPDATE inventory SET quantity = ? WHERE blood_type = ?", (result, blood_type))

    @staticmethod
    def deduct_blood(blood_type, quantity=1):
        result = db_query("SELECT quantity FROM inventory WHERE blood_type = ?", (blood_type,))
        if result[0][0] < quantity:
            print(f"Not enough blood for {blood_type}")
        else:
            db_query("UPDATE inventory SET quantity = ? WHERE blood_type = ?", (result[0][0] - quantity, blood_type))
