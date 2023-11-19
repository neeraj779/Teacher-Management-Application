<div align="center">
<h1 align="center"> TEACHER-MANAGEMENT-APPLICATION</h1>

![banner](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/71e79365-9663-40c1-a0a5-446dcd969a14)

<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Django-092E20.svg?style=flat-square&logo=Django&logoColor=white" alt="Django" />
</p>
<img src="https://img.shields.io/github/license/neeraj779/Teacher-Management-Application?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/neeraj779/Teacher-Management-Application?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/neeraj779/Teacher-Management-Application?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
</div>

---

## 📖 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 repository Structure
- ⚙️ Modules
- 🚀 Getting Started
    - 🔧 Installation
    - 🤖 Running Teacher-Management-Application
- 📷 Screenshots
---


## 📍 Overview

The Teacher Management Application is a comprehensive solution designed for the management of teacher records, providing both console-based and backend functionalities. 

---

## 📦 Features

The application focuses on delivering a user-friendly experience with a range of end-user features. These features include:

***Landing/Home Page:***
<pre>
i) Show all teachers: View a list of all teachers.
ii) Add a teacher: Add a new teacher to the system.
iii) Filter teachers based on criteria: Implement filters to sort teachers based on age and the number of classes.
iv) Search for a teacher: Search for a specific teacher.
v) Update a teacher's record: Modify information for a teacher.
vi) Delete a teacher: Remove a teacher from the system.
</pre>
  

***Teacher’s Record***

<PRE>
Each teacher's record includes:
  
i) Full Name: Complete name of the teacher.
ii) Age: Age of the teacher.
iii) Date of Birth: Birthdate of the teacher.
iv) Number of classes: The count of classes the teacher is responsible for.
</PRE>

***Filter Teachers by Criteria***
<pre>
An additional option-based page is implemented to filter teachers:
  
i) Filter by Age: Categorize teachers based on their age.
ii) Filter by the number of classes: Sort teachers according to the number of classes they teach.
</pre>
***File-Based System***

The application uses an JSON file-based system to store and manage teacher records.

### Bonus/Optional Task

An optional feature has been implemented to calculate and display the average number of classes taken by teachers. Users can also download a JSON file and import it into the system.

---


## 📂 Repository Structure

```sh
└── Teacher-Management-Application/
    ├── .env.example
    ├── .github/
    │   └── ISSUE_TEMPLATE/
    ├── console/
    │   └── main.py
    ├── core/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── templates/
    │   │   └── core/
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── Procfile
    ├── requirements.txt
    └── TeacherManagement/
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                                                             | Summary                   |
| ---                                                                                                                                              | ---                       |
| [.env.example](https://github.com/neeraj779/Teacher-Management-Application/blob/main/.env.example)                                               | Example environment file, providing necessary configurations. |
| [manage.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/manage.py)                                                     | Django management script for various project-related tasks. |
| [Procfile](https://github.com/neeraj779/Teacher-Management-Application/blob/main/Procfile)                                                       | Heroku Procfile specifying the commands to run the application. |
| [requirements.txt](https://github.com/neeraj779/Teacher-Management-Application/blob/main/requirements.txt)                                       | List of Python packages and their versions required for the project. |
| [main.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/console\main.py)                                                 | Main console application file, serving as the entry point for the console-based functionalities. |
| [admin.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\admin.py)                                                  | Django admin configuration for managing app models through the admin interface. |
| [apps.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\apps.py)                                                    | Django application configuration with app-specific settings. |
| [models.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\models.py)                                                | Definition of Django models representing the data structure of the application. |
| [tests.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\tests.py)                                                  | Unit tests for the core application logic. |
| [urls.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\urls.py)                                                    | URL routing configuration for the core application. |
| [views.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\views.py)                                                  | Implementation of views (controllers) handling HTTP requests and responses. |
| [addTeacher.html](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\templates\core\addTeacher.html)                     | HTML template for adding a new teacher to the system. |
| [base.html](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\templates\core\base.html)                                 | Base HTML template providing the common structure for other templates. |
| [deleteTeacherDetails.html](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\templates\core\deleteTeacherDetails.html) | HTML template for deleting a teacher's details from the system. |
| [filterTeachers.html](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\templates\core\filterTeachers.html)             | HTML template for filtering teachers based on criteria. |
| [home.html](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\templates\core\home.html)                                 | HTML template for the home page, displaying various options for end-users. |
| [importJson.html](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\templates\core\importJson.html)                     | HTML template for importing teacher data from a JSON file. |
| [performDetailsUpdate.html](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\templates\core\performDetailsUpdate.html) | HTML template for performing updates to a teacher's details. |
| [searchTeacher.html](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\templates\core\searchTeacher.html)               | HTML template for searching and displaying a specific teacher's details. |
| [showAllTeachers.html](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\templates\core\showAllTeachers.html)           | HTML template for displaying a list of all teachers. |
| [updateTeacherDetails.html](https://github.com/neeraj779/Teacher-Management-Application/blob/main/core\templates\core\updateTeacherDetails.html) | HTML template for updating a teacher's details in the system. |
| [asgi.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/TeacherManagement\asgi.py)                                       | ASGI configuration for Django application. |
| [settings.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/TeacherManagement\settings.py)                               | Django project settings and configurations. |
| [urls.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/TeacherManagement\urls.py)                                       | URL patterns for the Django project. |
| [wsgi.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/TeacherManagement\wsgi.py)                                       | WSGI configuration for Django application. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Python 3.6 or higher`

### 🔧 Installation

1. Clone the Teacher-Management-Application repository:
```sh
git clone https://github.com/neeraj779/Teacher-Management-Application
```

2. Change to the project directory:
```sh
cd Teacher-Management-Application
```

3. Create a virtual environment (optional but recommended):
```sh
python -m venv venv
```

4. Activate the virtual environment: <br>
   ***On Windows:***
  ```sh
.\venv\Scripts\activate
  ```
&nbsp;&nbsp;&nbsp;&nbsp; ***On macOS/Linux:***
  ```sh
source venv/bin/activate
  ```

5. Install the dependencies:
```sh
pip install -r requirements.txt
```

### Env setup
Create a .env file in the root of the project and add the necessary environment variables. You can use the provided .env.example file as a template.


`cp .env.example .env`

#### env File Explanation
Most them are default values, you can change them as per your needs.

- `SECRET_KEY` = Django Secret Key
- `DEBUG` = 'True'
- `ALLOWED_HOSTS` = Domain name of allowed hosts
  

### 🤖 Running Teacher-Management-Application

```sh
python manage.py runserver
```

### 🤖 Running Console-Based Teacher-Management-Application

If you prefer a console-based application you can skip the env setup and run the following command:

```sh
python console/console_app.py
```

## Screenshots of Web Application

1. Home Page
    ![HomePage](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/2d8022ec-8c7c-4432-a6b5-e6c4f42cc63b)

2. Add Teacher
   
    ![addTeacher](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/46f2af24-9131-43f8-b6d5-214e860ae864)

4. Search Teacher

   ![searchTeacher](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/955cbbb1-8233-4a07-9d9e-fceee2a66ba5)


6. Update Teacher

    ![updateTeacherRecord](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/fc35754f-8801-4da0-a061-eba82f0fe522)


8. Delete Teacher
   
    ![deleteTeacherRecord](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/1b039641-fb15-4596-a27e-cbd7a82f9a02)

10. Filter Teacher
    
    ![filterTeacher](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/eeac7a03-d9f1-4515-9ab1-102350ef7551)

11. Import JSON'

    ![importJson](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/7aa8e217-a634-4fa2-8288-fdd9e4ad0bd3)

## Screenshots of Console Application

1. Landing/Home Page

2. Show all teachers

3. Fileter teachers based on criteria

4. Search for a teacher

5. Update a teacher's record

6. Delete a teacher