class DrugInventory:

    def __init__(self):
        self.inventory = []

    def add_batch(self, batch):
        self.inventory.append(batch)
        return 'batch added!'

    def search(self, search_term):
        for batch in self.inventory:
            if search_term == batch.name or search_term == batch.batch_id:
                return batch
        return None

    def check_expiry(self, current_date):
        expired_batches = []
        for batch in self.inventory:
            if batch.expiry_date < current_date:
                expired_batches.append(batch)
        return expired_batches

    def remove_batch(self, batch_id):
        for batch in self.inventory:
            if batch.batch_id == batch_id:
                self.inventory.remove(batch)
                return "batch removed!"
        return "batch not found"

    def low_stock_alert(self, threshold):
        low_stock_batches = []
        for batch in self.inventory:
            if batch.quantity <= threshold:
                low_stock_batches.append(batch)
        return low_stock_batches

    def total_stock_value(self):
        total_value = 0
        for batch in self.inventory:
            total_value += batch.quantity * batch.price
        return total_value

    def __str__(self):
        if len(self.inventory) == 0:
            return "inventory is empty"
        report = "----Current Drug Inventory----\n"
        for batch in self.inventory:
            report += str(batch) + "\n"
        return report


if __name__ == "__main__":

    class DrugBatch:
        def __init__(self, name, batch_id, quantity, price, expiry_date):
            self.name = name
            self.batch_id = batch_id
            self.quantity = quantity
            self.price = price
            self.expiry_date = expiry_date  # Format: 'YYYY-MM-DD'

        def __str__(self):
            return f"{self.name} (ID: {self.batch_id}) | Qty: {self.quantity} | ${self.price} | Exp: {self.expiry_date}"

    # --- THE STRESS TEST ---

    # 1. Open the warehouse
    my_pharmacy = DrugInventory()
    print("INITIAL STATE:")
    print(my_pharmacy)

    # 2. Create boxes (I made one expired and one low stock to test your logic)
    b1 = DrugBatch("Aspirin", "TX-11", 50, 10, "2028-01-01")
    b2 = DrugBatch("Amoxicillin", "RX-22", 5, 50,
                   "2025-05-01")  # Expired and low stock
    b3 = DrugBatch("Ibuprofen", "IB-33", 100, 15, "2027-10-15")

    # 3. Test add_batch
    print("\n--- TESTING: add_batch ---")
    print(my_pharmacy.add_batch(b1))
    print(my_pharmacy.add_batch(b2))
    print(my_pharmacy.add_batch(b3))
    print(my_pharmacy)

    # 4. Test search
    print("\n--- TESTING: search ---")
    found = my_pharmacy.search("RX-22")
    print(f"Search for RX-22: {found}")
    missing = my_pharmacy.search("FakeDrug")
    print(f"Search for FakeDrug: {missing}")

    # 5. Test check_expiry
    print("\n--- TESTING: check_expiry ---")
    today = "2026-03-19"
    expired_items = my_pharmacy.check_expiry(today)
    print(f"Found {len(expired_items)} expired batches:")
    for item in expired_items:
        print(f" -> {item.name}")

    # 6. Test low_stock_alert
    print("\n--- TESTING: low_stock_alert ---")
    low_stock = my_pharmacy.low_stock_alert(10)
    print(f"Found {len(low_stock)} batches with low stock:")
    for item in low_stock:
        print(f" -> {item.name} (Only {item.quantity} left)")

    # 7. Test total_stock_value
    print("\n--- TESTING: total_stock_value ---")
    print(f"Total Warehouse Value: ${my_pharmacy.total_stock_value()}")

    # 8. Test remove_batch
    print("\n--- TESTING: remove_batch ---")
    print(my_pharmacy.remove_batch("TX-11"))
    print("\nFINAL INVENTORY STATE:")
    print(my_pharmacy)
