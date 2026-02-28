# Blood Donation Management System

This project presents the relational database design and SQL implementation of a **Blood Donation Management System (BDMS)**.

It models donors, recipients, blood donations, medical tests, staff members, and donation centers while ensuring referential integrity and normalized schema structure.

---

## Project Objectives

- Design a normalized relational database (up to 3NF)
- Model real-world blood donation operations
- Enforce data integrity using primary and foreign keys
- Implement constraints and relationships in SQL

---

## Database Design

### Conceptual Design
- Entity Relationship Diagram (ERD)

### Logical Design
- Relational Schema Mapping
- Primary Keys
- Foreign Keys
- Constraints (NOT NULL, UNIQUE, CHECK)

---

## Main Entities

- **Donor**
- **Recipient**
- **Blood Donation**
- **Blood Test**
- **Medical History**
- **Health Condition**
- **Staff Member**
- **Phlebotomist**
- **Blood Donation Center**

---

## Technologies Used

- SQL
- Relational Database Modeling
- ER Modeling
- Normalization Techniques

---

## Python Integration

This project also includes a Python application that connects to the MariaDB database and performs database operations such as:

- Retrieving donor data
- Executing queries
- Displaying results
- Managing database interaction

The Python application connects to the `bdms` database using MySQL/MariaDB connector.

---

## Project Structure

- `sql/` → Database implementation (CREATE TABLE, constraints)
- `diagrams/` → ERD and relational schema
- `app/` → main.py
- `sample_queries/` → Example SQL queries
- `README.md` → Project documentation
