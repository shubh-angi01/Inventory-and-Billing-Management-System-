# 🧾 Inventory & Billing Management System

A full-stack web application built using **Django** that enables efficient management of inventory and billing operations for small to medium-scale businesses.

---

## 🎯 Project Overview

This system is designed to streamline core business workflows by providing:

* Product and inventory management
* Real-time stock tracking
* Invoice generation and billing
* Sales monitoring

The project demonstrates practical implementation of **full-stack development, CRUD operations, and business logic integration**.

---

## 🚀 Features

### 🔐 User Authentication

* Secure login system
* Role-based access control

### 📦 Inventory Management

* Add, update, and delete products
* Monitor stock levels in real-time

### 🧾 Billing System

* Generate invoices dynamically
* Record sales transactions
* Track customer purchases

---

## 🛠 Technology Stack

### Backend

* Python
* Django

### Frontend

* HTML
* CSS
* JavaScript

### Database

* SQLite / MySQL

### Tools

* Git
* GitHub
* VS Code

---

## 🏗️ System Architecture

The application follows a **three-tier architecture**:

### Presentation Layer

* HTML templates
* CSS styling
* JavaScript interactions

### Application Layer

* Django framework
* Business logic and request handling

### Data Layer

* SQLite / MySQL database
* Data storage and retrieval

---

## 📊 Database Schema

### Products

* id (Primary Key)
* name
* quantity
* price

### Customers

* id
* name
* contact

### Invoices

* id
* product_id
* quantity
* total_price
* created_at

---

## 📁 Project Structure

```
inventory-management-system/
│
├── accounts/                # User authentication
├── billing/                 # Invoice management
├── inventory/               # Product management
│
├── templates/               # HTML templates
│   ├── accounts/
│   ├── billing/
│   └── inventory/
│
├── static/                  # CSS, JavaScript, images
│   ├── css/
│   ├── js/
│   └── images/
│
├── screenshots/             # Application screenshots
│   ├── dashboard.png
│   ├── inventory.png
│   └── invoice.png
│
├── documentation/           # Project documentation
│   ├── API.md
│   ├── SRS.md
│   ├── SDS.md
│   └── TestPlan.md
│
├── manage.py                # Django project runner
├── requirements.txt         # Python dependencies
├── .gitignore               # Ignored files
└── README.md                # Project documentation
```

---

## ⚙️ Installation

### Clone the repository

```
git clone https://github.com/shubh-angi01/Inventory-and-Billing-Management-System-.git

### Navigate to the project

```
cd inventory-management-system-main
```

### Create virtual environment

```
python -m venv venv
```

### Activate environment (Windows)

```
venv\Scripts\activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the server

```
python manage.py runserver
```


---




