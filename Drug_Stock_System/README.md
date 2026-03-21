# Drug Inventory Engine 🏥💊

Part of the master **Healthcare OOP Suite**, this module is a fully interactive, Object-Oriented Python system designed to manage pharmaceutical warehouse data. 

It features a two-way data-binding architecture that reads, updates, and permanently saves stock levels to an external CSV database via a Command Line Interface (CLI).

## ⚙️ Core Architecture

* **`DrugBatch` Class:** The blueprint for individual medication units. It strictly enforces data types (parsing strings to integers/floats) for accurate mathematical operations.
* **`DrugInventory` Class:** The warehouse manager. Handles the logic for data loading, searching, restocking, and saving.
* **Two-Way CSV Persistence:** System memory is not temporary. Changes made in the terminal are actively written back to `drug_stock.csv` using Python's `csv.writer`.
* **Defensive CLI:** Built with a continuous state loop and error handling to prevent systemic crashes from invalid user inputs.

## 🚀 How to Run the Engine

1. Ensure Python 3.x is installed on your machine.
2. Navigate to this specific directory in your terminal.
3. Verify that the `drug_stock.csv` database file is present in the same folder.
4. Boot the system:
   ```bash
   python inventory.py # Or whatever your main script is named