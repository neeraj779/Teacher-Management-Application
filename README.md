<div align="center">
<h1 align="center"> TEACHER MANAGEMENT APPLICATION</h1>
    
![banner](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/242f95d3-3239-4e2e-a2c7-04414ef43cbd)


<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Django-092E20.svg?style=flat-square&logo=Django&logoColor=white" alt="Django" />
</p>
<img src="https://img.shields.io/github/last-commit/neeraj779/Teacher-Management-Application?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/neeraj779/Teacher-Management-Application?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
</div>

---

You can view the live version of this project at below link ⬇️

[https://tma-by-neeraj-3a3bd31fae0a.herokuapp.com/](https://tma-by-neeraj-3a3bd31fae0a.herokuapp.com/)

---

## 📖 Table of Contents
- 📍 Overview
- 📦 Features
- Demo Videos
- 📂 repository Structure
- ⚙️ Modules
- 🚀 Getting Started
    - 🔧 Installation
    - 🤖 Running Teacher Management Web Application
    - 🤖 Running Teacher Management Console Application
- 📷 Screenshots
---


## 📍 Overview

The Teacher Management Application is a solution designed for the management of teacher records, providing both console-based and web-based functionalities. 

---

## 📦 Features

***Landing/Home Page:***
- Show all teachers: View a list of all teachers.
- Add a teacher: Add a new teacher to the system.
- Filter teachers based on criteria: Implement filters to sort teachers based on age and the number of classes.
- Search for a teacher: Search for a specific teacher.
- Update a teacher's record: Modify information for a teacher.
- Delete a teacher: Remove a teacher from the system.
  

***Teacher’s Record***

Each teacher's record includes:
  
- Full Name: Complete name of the teacher.
- Age: Age of the teacher.
- Date of Birth: Date of Birth of the teacher in dd-mm-yyyy format.
- Number of classes: The count of classes the teacher is responsible for.

***Filter Teachers by Criteria***

An additional option-based page is implemented to filter teachers:
  
- Filter by Age: Categorize teachers based on their age.
- Filter by the number of classes: Sort teachers according to the number of classes they teach.
***File-Based System***

The application uses an JSON file-based system to store and manage teacher records.

### Additional Features

- User can calculate the average number of classes taken by teachers.
- Users can also download a JSON file.
- Users can import JSON file into the system.

---


### Demo Video

***Teacher Management Web Application Demo Video***

https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/230f77b0-28e8-480e-87a8-31468c18c485

***Teacher Management Console Application Demo Video***

https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/103d07b3-2741-4be2-b4eb-894172bde9d7


## 📂 Repository Structure

```sh
└── Teacher-Management-Application/
    ├── .env.example
    ├── .github/
    │   └── ISSUE_TEMPLATE/
    ├── console/
    │   └── console_app.py
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
| [console_app.py](https://github.com/neeraj779/Teacher-Management-Application/blob/main/console\console_app.py)                                                 | Main console application file, serving as the entry point for the console-based functionalities. |
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
Create a .env file in the root directory of the project and copy the contents of .env.example to it.

You can do this by running the following command in the root directory of the project:

- `cp .env.example .env`

#### Environment Variables 

Most of the environment variables are already set in the .env.example file. You can change them according to your needs.

- `SECRET_KEY` = Django Secret Key (Set to a random string of characters for development)
- `DEBUG` = True or False (Set True for development and False for production)
- `ALLOWED_HOSTS` = Allowed Hosts (Set to * for development)
  

### 🤖 Running Teacher Management Web  Application

```sh
python manage.py runserver
```

### 🤖 Running Teacher Management Console Application

If you prefer a console-based application you can skip the env setup and run the following command:

```sh
python console/console_app.py
```

## Screenshots of Web Application

1. Home Page

    ![HomePage](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/9b89d3e9-7620-4498-8229-cad1e6678f49)

3. Add Teacher
   
    ![addTeacher](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/c4dccb41-74cd-4d26-865d-ba9a2cede98f)

5. Search Teacher
   
    ![searchTeacher](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/8d72b6b0-6e91-4866-84d0-412b93c6d92b)


7. Update Teacher
   
    ![updateTeacherRecord](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/61aa18d1-fdad-4213-a25c-1aebb2a25fd7)

9. Delete Teacher
    
    ![deleteTeacherRecord](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/e0957c78-fe22-4f48-92cf-0446a50f2cdb)

11. Filter Teacher
    
    ![filterTeacher](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/29aea49f-4ae5-460c-bef0-17852596bff7)


13. Import JSON
    
    ![importJson](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/20bc4e9e-e574-4160-9ddc-b90eb4a03d10)


## Screenshots of Console Application

1. Landing/Home Page

   ![consoleHomePage](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/65a62ca5-a45e-427d-9738-29a79bc22b68)


3. Show all teachers
   
    ![consoleShowAllTeacher](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/3d0ba47e-fbc0-4159-b2ed-bd1777c898d0)

    
5. Add a teacher
   
   ![consoleAddTeacher](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/c5842d8f-c21e-491e-80f9-44ff0fce284d)

3. Filter teachers based on criteria
   
    ![consoleFilterTeacher](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/063895da-b3ed-47e4-8cd8-0a95efcd040d)

5. Search for a teacher
   
   ![consoleSearchTeacher](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/23f4874e-a61a-449d-8fa8-75f3e28ff30b)

7. Update a teacher's record
   
   ![consoleUpdateTeacherRecord](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/c95428ac-a653-48f5-88bf-8149b65feb4c)

9. Delete a teacher
    
    ![consoleDeleteTeacherRecord](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/67acc8ee-b16d-4de3-9c96-c3668380a139)

11. Calculate the average number of classes taken by teachers
    
    ![consoleAverage](https://github.com/neeraj779/Teacher-Management-Application/assets/85169876/7ff50f35-03dc-4eac-aaba-6370f20ec56e)
