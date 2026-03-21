import csv


class DrugBatch:
    def __init__(self, name, batch_id, quantity, price, expiry_date):
        self.name = name
        self.batch_id = batch_id
        self.quantity = int(quantity)
        self.price = float(price)
        self.expiry_date = expiry_date

    def __str__(self):
        return f"{self.name:22} | ID: {self.batch_id:10} | Qty: {self.quantity:4} | ${self.price:7.2f} | Exp: {self.expiry_date}"


class DrugInventory:
    def __init__(self):
        self.inventory = []

    def load_from_csv(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                self.inventory = [
                    DrugBatch(r[0], r[1], r[2], r[3], r[4]) for r in reader]
            return f"✅ Loaded {len(self.inventory)} items."
        except FileNotFoundError:
            return "❌ Error: drug_stock.csv not found in this folder!"

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                ['name', 'batch_id', 'quantity', 'price', 'expiry_date'])
            for b in self.inventory:
                writer.writerow(
                    [b.name, b.batch_id, b.quantity, b.price, b.expiry_date])
        return "💾 Changes saved to CSV!"

    def restock(self, batch_id, amount):
        for b in self.inventory:
            if b.batch_id == batch_id:
                b.quantity += amount
                return f"📈 Updated {b.name} to {b.quantity} units."
        return "❌ Batch ID not found."

    def __str__(self):
        if not self.inventory:
            return "Inventory Empty"
        header = f"\n{'NAME':22} | {'BATCH ID':10} | {'QTY':4} | {'PRICE':7} | {'EXPIRY'}\n" + "-"*75
        return header + "\n" + "\n".join(str(b) for b in self.inventory)


# --- THE INTERACTIVE MENU ---
if __name__ == "__main__":
    pharmacy = DrugInventory()
    FILE = 'drug_stock.csv'
    print(pharmacy.load_from_csv(FILE))

    while True:
        print("\n1. View Inventory | 2. Restock | 3. Save & Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print(pharmacy)
        elif choice == '2':
            bid = input("Enter Batch ID: ")
            amt = int(input("Amount to add: "))
            print(pharmacy.restock(bid, amt))
        elif choice == '3':
            print(pharmacy.save_to_csv(FILE))
            print("Goodbye!")
            break
