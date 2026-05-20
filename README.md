# Name: Yash Amol Mulay
# Class: TY AIML A
# Rollno: 02

## Assignment Title

Implementation of Simple Use Cases using Flask, FastAPI, Jenkins, AutoML, BentoML, MLflow, GitHub, and Docker

## Objective

The objective of this assignment is to install, configure, and demonstrate different tools used in Machine Learning and REST API development.

Each tool is implemented using a simple individual use case instead of integrating all tools into one project.

## Tools Implemented

| Sr. No. | Tool | Use Case |
|---|---|---|
| 1 | Flask | Student Marks Result Web App |
| 2 | FastAPI | Student Information REST API |
| 3 | Jenkins | Automated Python Script Testing |
| 4 | AutoML | Iris Classification using PyCaret |
| 5 | MLflow | ML Experiment Tracking |
| 6 | BentoML | Iris Model Serving API |
| 7 | GitHub | Version Control |
| 8 | Docker | Dockerized Flask Application |

## Folder Structure

```text
mlops-tools-assignment/
│
├── 01_flask_student_result/
├── 02_fastapi_student_api/
├── 03_jenkins_python_automation/
├── 04_automl_iris_classification/
├── 05_mlflow_experiment_tracking/
├── 06_bentoml_model_serving/
├── 07_github_version_control/
├── 08_docker_flask_app/
└── README.md


# Flask Use Case: Student Marks Result Web Application

## Objective

To create a simple web application using Flask that accepts marks of three subjects and calculates total marks, percentage, grade, and pass/fail status.

## Tool Used

Flask

## Files

- app.py
- templates/index.html
- requirements.txt

## Installation Command

```bash
pip install flask


Execution Command
python app.py
Testing URL
http://127.0.0.1:5000
Sample Input
Student Name: Yash
Subject 1: 85
Subject 2: 78
Subject 3: 90
Sample Output
Total: 253/300
Percentage: 84.33%
Status: Pass
Grade: A


# FastAPI Use Case: Student Information REST API

## Objective

To create a simple REST API using FastAPI for managing student information.

## Tool Used

FastAPI

## Files

- main.py
- requirements.txt

## Installation Command

```bash
pip install fastapi uvicorn
```

## Execution Command

```bash
uvicorn main:app --reload
```

## Testing URLs

### Home API

```text
http://127.0.0.1:8000
```

### Get All Students

```text
http://127.0.0.1:8000/students
```

### Get Student by ID

```text
http://127.0.0.1:8000/students/1
```

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

## Sample POST JSON

```json
{
  "id": 3,
  "name": "Amit",
  "course": "Data Science",
  "year": "Second Year",
  "marks": 88.5
}
```

## Sample POST Output

```json
{
  "message": "Student added successfully",
  "student": {
    "id": 3,
    "name": "Amit",
    "course": "Data Science",
    "year": "Second Year",
    "marks": 88.5
  }
}
```

## Conclusion

This use case demonstrates how FastAPI can be used to create REST APIs with automatic Swagger documentation.


# Jenkins Use Case: Automated Python Calculator Testing

## Objective

To demonstrate Jenkins automation by running a simple Python calculator program and executing test cases automatically.

## Tool Used

Jenkins

## Files

- calculator.py
- test_calculator.py
- requirements.txt
- Jenkinsfile

## Installation Requirement

- Jenkins
- Java JDK
- Python
- pytest

## Local Execution Commands

```bash
python calculator.py
pytest
```

## Jenkins Pipeline Stages

1. Check Python Version
2. Install Dependencies
3. Run Calculator Program
4. Run Test Cases

## Jenkinsfile

```groovy
pipeline {
    agent any

    stages {
        stage('Check Python Version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Calculator Program') {
            steps {
                bat 'python calculator.py'
            }
        }

        stage('Run Test Cases') {
            steps {
                bat 'pytest'
            }
        }
    }

    post {
        success {
            echo 'Jenkins Pipeline Completed Successfully!'
        }

        failure {
            echo 'Jenkins Pipeline Failed!'
        }
    }
}
```

## Expected Output

```text
Calculator Program
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
5 passed
Finished: SUCCESS
```

## Conclusion

This use case demonstrates how Jenkins can automate the execution and testing of a Python application.