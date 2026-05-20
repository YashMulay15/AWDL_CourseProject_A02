from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student Information API")

class Student(BaseModel):
    id: int
    name: str
    course: str
    year: str
    marks: float

students = [
    {
        "id": 1,
        "name": "Yash",
        "course": "AIML",
        "year": "Third Year",
        "marks": 85.5
    },
    {
        "id": 2,
        "name": "Rahul",
        "course": "Computer Engineering",
        "year": "Third Year",
        "marks": 78.0
    }
]

@app.get("/")
def home():
    return {
        "message": "Welcome to Student Information REST API"
    }

@app.get("/students")
def get_students():
    return {
        "total_students": len(students),
        "students": students
    }

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students")
def add_student(student: Student):
    for existing_student in students:
        if existing_student["id"] == student.id:
            raise HTTPException(status_code=400, detail="Student ID already exists")

    students.append(student.dict())

    return {
        "message": "Student added successfully",
        "student": student
    }

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {
                "message": "Student deleted successfully",
                "deleted_student": student
            }

    raise HTTPException(status_code=404, detail="Student not found")