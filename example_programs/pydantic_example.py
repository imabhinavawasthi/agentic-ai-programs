from pydantic import BaseModel, EmailStr, ValidationError

class Student(BaseModel):
    id: int
    name: str
    email: EmailStr

try:
    st1 = Student(id=1, name="Alice", email="alice@gmail.com")
    print(st1)

    st2 = Student(id=2, name="Bob", email="hello@email.com")
    print(st2)
except ValidationError as e:
    print(e)