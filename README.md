# 📚 Library Management System API

A comprehensive Library Management System API built with Django REST Framework (DRF) that provides complete functionality for managing library operations including user authentication, book management, and book issuing system with role-based access control.

## ✨ Features

### 🔐 **Authentication & Authorization**
- **Token-based Authentication** using DRF's built-in token system
- User Registration and Login functionality
- Role-based Access Control (Admin/Member permissions)
- Auto Member Creation on User Registration (via Django Signals)

### 📘 **Book Management**
- ✅ **Admin-only Book Operations**: Add, Edit, Delete books (Admin privileges required)
- 👁️ **Public Book Viewing**: Authenticated users can view all available books
- 📊 **Book Information Tracking**: Complete book details with availability status

### 📦 **Book Issuing System**
- 📅 **Date Tracking**: Automatic tracking of issue date and return date
- 🧾 **Issue History**: View issued books (own books for members, all books for admin)
- ⏰ **Overdue Management**: View overdue books with automated tracking
- 🔄 **Return System**: Seamless book return functionality

## Tech stack used:

![Django](https://img.shields.io/badge/DJANGO-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST](https://img.shields.io/badge/DJANGO%20REST-FF0000?style=for-the-badge&logo=django&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

---

## Tools used

![Postman](https://img.shields.io/badge/POSTMAN-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![VS Code](https://img.shields.io/badge/VISUAL%20STUDIO%20CODE-0078d7?style=for-the-badge&logo=visual-studio-code&logoColor=white)


## 🚀 Setup and Installation Instructions

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package manager)
- Git

### **1. Clone the Repository**
```bash
git clone https://github.com/anurag433/Library-Management-System.git
cd library_project
```

### **2. Create Virtual Environment**
```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Database Setup**
```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### **5. Create Superuser (Admin)**
```bash
python manage.py createsuperuser
```

### **6. Run Development Server**
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## 📖 API Documentation

### **Base URL**
```
http://127.0.0.1:8000/api/
```

### **Authentication Endpoints**

#### **User Registration**
```http
POST /api/register/
Content-Type: application/json

{
    "first_name": "This field is required.",
    "username":  "This field is required.",
    "email":  "This field is required.",
    "password": "This field is required."
}
```

**Response:**
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### **Book Management Endpoints**

#### **Get All Books**
```http
GET /api/books/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response:**
```json
{
    {
        "id": 8,
        "title": "Data Stucture",
        "author": "N.P Bali",
        "edition": 13,
        "available": true,
        "cover_image": null
    }
}
```

#### **Add New Book (Admin Only)**
```http
POST /api/books/
Authorization: Token admin-token-here
Content-Type: application/json

{
    "title":  "This field is required.",
    "author":  "This field is required.",
    "edition":  "This field is required." 
}
```

#### **Update Book (Admin Only)**
```http
PUT /api/books/{book_id}/
Authorization: Token admin-token-here
Content-Type: application/json
{
        "id": 8,
        "title": "Data Stucture",
        "author": "N.P Bali",
        "edition": 15,     
        "available": true,
        "cover_image": null
    },
```

#### **Delete Book (Admin Only)**
```http
DELETE /api/books/{book_id}/
Authorization: Token admin-token-here
```

### **Book Issuing Endpoints**

#### **Issue Book**
```http
POST /api/issued/
Authorization: Token user-token-here
Content-Type: application/json

{
    "book_id":  "This field is required."
}
```

**Response:**
```json
{
    "id": 13,
    "issued_date": "2025-09-05",
    "return_date": "2025-09-12",
    "returned": false,
    "book": 8,
    "member": 10
}
```

#### **Return Book**
```http
POST /api/issued/{issue_id}/return/
Authorization: Token user-token-here
```
**Response:**
```json
{
    "status": "Book Succesfully Returned"
}
```

#### **Get User's Issued Books**
```http
GET /api/issued/
Authorization: Token user-token-here
```

**Response:**
```json
{
     {
        "id": 9,
        "issued_date": "2025-09-05",
        "return_date": "2025-09-12",
        "returned": false,
        "book": 9,
        "member": 10
    },
    {
        "id": 10,
        "issued_date": "2025-09-05",
        "return_date": "2025-09-12",
        "returned": true,
        "book": 9,
        "member": 10
    },
    
}
```

#### **Get All Issued Books (Admin Only)**
```http
GET /api/issued/
Authorization: Token admin-token-here
```

#### **Get Overdue Books**
```http
GET /api/issued/overdue/
Authorization: Token user-token-here
```

### **HTTP Status Codes**
- `200 OK` - Request successful
- `201 Created` - Resource created successfully
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## 🎯 Why Django REST Framework?

- **Rapid Development & Scalability**  
  Comes with ORM, Admin Panel, User Authentication, and supports easy scaling.

- **Seamless API Creation**  
  DRF provides Serialization, ViewSets, Authentication/Permissions, and a Browsable API.

- **Perfect for Library Management**  
  Role-based permissions, Token Authentication, Signals for automation, and flexible database relations.

## 🔮 Future Enhancements

- **Email Notifications**: Send reminders for due dates and overdue books
- **Book Cover Image**: Each book contains its cover image

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Anurag Singh**
- GitHub: [@anurag433](https://github.com/anurag433)
- Project Link: [https://github.com/anurag433/Library-Management-System](https://github.com/anurag433/Library-Management-System)



⭐ **Star this repository if you found it helpful!**
