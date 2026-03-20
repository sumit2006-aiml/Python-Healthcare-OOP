# Clinical Trial & Patient Management (CTPM)
**Module Lead:** Sumit  
**Category:** Clinical Research Informatics / Healthcare Data

## 🏥 Overview
The **CTPM Module** is a robust Python-based engine designed to manage participant data in a clinical trial environment. It prioritizes **Data Encapsulation** to ensure that sensitive patient information is handled through secure object-oriented methods rather than direct variable manipulation.



## 🛠️ Logic & Architecture
This module follows a strict **Participant-Object** model where each patient is an instance of a class, ensuring data integrity across the trial lifecycle.

### Core Features:
* **Medical History Tracking:** Automated storage and retrieval of past patient conditions.
* **Enrollment Logic:** Status-based filtering (Active, Completed, Withdrawn).
* **Demographic Encapsulation:** Safe handling of patient-specific attributes (Age, Gender, Trial ID).
* **Audit Ready:** Clean string representation (`__str__`) for rapid status reporting during trial reviews.

## 💻 Technical Implementation
* **Class Structure:** `Patient` class architecture.
* **Data Storage:** Dynamic list-based participant registry (Structured for future SQL migration).
* **Interface:** Command-line based status reporting and participant adding.

---

## 🧪 Quick Start (Developer Use)
To run the clinical trial simulation:
```bash
python patient_trial.py