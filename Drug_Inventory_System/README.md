# Drug Inventory Management System (PIMS)
**Module Lead:** Sumit  
**Category:** Pharmaceutical Supply Chain / Inventory Informatics

## 💊 Overview
The **PIMS Module** is a backend engine designed to automate the tracking and valuation of pharmaceutical stock. In a professional pharmacy setting, accuracy is the difference between life and death. This system ensures that stock levels, expiry dates, and financial assets are tracked with precision.



## 🛠️ Engineering Logic
This system is built using **Object-Oriented Programming (OOP)** to ensure that every drug is treated as a unique entity with its own lifecycle.

### Core Features:
* **Dynamic Valuation:** Real-time calculation of total warehouse value based on unit price and quantity.
* **Low-Stock Alerts:** Automated threshold monitoring to prevent stock-outs of life-saving medications.
* **Expiry Auditing:** Logic designed to flag medications reaching their end-of-life status.
* **Batch Reporting:** Clean string formatting for rapid inventory audits and QC checks.

## 📊 Technical Implementation
* **Class Architecture:** `Drug` object model with encapsulation for price and quantity.
* **Financial Logic:** Total Value = $\sum (Quantity \times Price)$
* **Audit Trail:** Automatic reporting of stock updates and inventory status.

---

## 🧪 Quick Start (Developer Use)
To run the inventory simulation:
```bash
python inventory.py