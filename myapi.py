from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# amazon.com/create-user
# GET - get all users
# POST - create a user
# PUT - update a user
# DELETE - delete a user

students = {
    1: {
        "name": "sandalika",
        "age": 25,
        "year": "A"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/get-all-students")
def get_all_students():
    return students


@app.get("/")
def index():
    return {"name": "sandalika"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]

@app.get("/get-student-by-name/{student_id}")
def get_student_by_name(*, student_id: int, name: Optional[str] = None, test = int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student Exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    del students[student_id]
    return {"Message": "Student Deleted Successfully"}

