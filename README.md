Project 5: Flask-Based Student Registration Web Application deployed using Jenkins

## Objective

This project is a Flask-based web application that allows users to register student details and store them in a MySQL database. The app is containerized using Docker and deployed using Jenkins on an AWS EC2 instance.

---

## 🚀 Features

- Student registration via web form
- Stores data in MySQL database
- Displays list of registered students
- Containerized with Docker
- Deployed with Jenkins and GitHub
- Hosted on AWS EC2

---

## 🛠️ Technologies Used

- Python 3
- Flask
- MySQL
- HTML / Jinja2 Templates
- Docker
- Jenkins (CI/CD)
- Git & GitHub
- AWS EC2 (Ubuntu)

---

## 🏗️ Project Structure

Flask-BasedStudentRegistration/
├── app.py
├── config.py
├── requirements.txt
├── schema.sql
├── Jenkinsfile
├── templates/
│ ├── form.html
│ └── students.html
├── screenshots/
│ ├── form-page.png
│ └── students-page.png
└── README.md


## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone git@github.com:Awaish05/student-registration-project.git
cd student-registration-project

2. Set up MySQL

CREATE DATABASE student_db;
USE student_db;
CREATE TABLE student (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  phone VARCHAR(15),
  course VARCHAR(100),
  address TEXT
);

3. Create virtual environment and install dependencies

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

4. Run the app

python3 app.py

Open in browser:
http://<EC2-IP>:5000
📦 Deployment

This app was deployed using:

    Jenkins Pipeline (via Jenkinsfile)

    Dockerized container

    AWS EC2 instance (Ubuntu)
