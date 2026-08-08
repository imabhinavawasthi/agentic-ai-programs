from dataclasses import asdict, dataclass

@dataclass
class UserDetails:
    name: str
    age: int
    height: float

def print_user_details(user: UserDetails):
    print(f"User Name: {user.name}")
    print(f"User Age: {user.age}")
    print(f"User Height: {user.height}")


user_1 = UserDetails(name="Abhinav", age=30, height=5.5)
print_user_details(user_1)

print(asdict(user_1))
