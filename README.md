# 📚 Library Management System API (Django REST Framework)

A fully functional **Library Management System API** built with Django REST Framework (DRF).  
This project supports user registration, login, book management, and book issuing for members, with role-based permissions (admin/member).

---

## 🚀 Features

- 🔐 **Token-based Authentication**
- 👤 **User Registration/Login**
- 👥 **Auto Member Creation on Register (via Django Signals)**
- 📘 **Admin-only Book Add/Edit/Delete**
- 👁️ **Authenticated Users Can View Books**
- 📦 **Issue Book (Only Once Per Book Until Returned)**
- 📅 **Track Issue Date and Return Date**
- 🧾 **View Issued Books (Own or All for Admin)**
- 🧾 **View Overdue Books (Own or All for Admin)**
- 🧠 **Role-Based Access Control**

---

## 🏗️ Tech Stack

- Python 
- Django 
- Django REST Framework
- SQLite 
- Postman for API testing

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/library-management-api.git
cd library-management-api
