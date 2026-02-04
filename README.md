# 🎓 Campus Flow – College Management System

Campus Flow is a web-based College Management System developed using Django.  
It helps manage colleges, departments, students, faculty, and staff in a structured and digital manner.

This project is designed for academic and learning purposes and demonstrates practical usage of Django MVC architecture, ORM, forms, and media handling.

---

## 🚀 Features

- 🏫 College Registration & Management  
- 🏢 Department Management  
- 👨‍🎓 Student Registration System  
- 🖼️ Profile & Logo Upload  
- 🔗 Dynamic URL Navigation  
- 📋 Form Validation  
- 🔐 CSRF Protection  

### 🔧 Partially Implemented
- 👩‍🏫 Faculty Model (Backend Only)  
- 👨‍💼 Staff Model (Backend Only)  
---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Django | Web Framework |
| HTML / CSS | Frontend |
| SQLite | Database |
| Django ORM | Database Handling |
| Django Forms | User Input |
| Media Storage | Image Upload |

---

## 📂 Project Structure

```bash
campus-flow/
│
├── app/
│ ├── models.py
│ ├── forms.py
│ ├── views.py
│ ├── urls.py
│
├── templates/
│ ├── index.html
│ ├── college.html
│ ├── department.html
│
├── static/
│ └── style.css
│
├── media/
│
├── manage.py
└── README.md
```


---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/campus-flow.git
cd campus-flow
```

### Create Virtual Environment
```bash
python -m venv venv
```
### Activate
```bash
venv\Scripts\activate
```
### Install Dependencies 
```bash
pip install django pillow 
```

### Make Migrations and Migrate
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Server
```bash
python manage.py runserver
```

## ⚠️ Limitations

- No authentication system
- No role-based permissions
- Faculty & Staff management not implemented in UI
- No reporting module
