from pydantic import BaseModel

class User (BaseModel):
    id: int
    name: str
    is_active: bool = True

input_data = {'id': 101, 'name': "Nazmul", 'is_active':True}


user = User(**input_data)

print(user)