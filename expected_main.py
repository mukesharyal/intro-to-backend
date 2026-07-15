# Import the various objects from the FastAPI library
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Utility library for type information
from typing import Optional, List

# Import the json standard library
import json

# Import the BaseModel class for JSON support
from pydantic import BaseModel

# This class User will tell us the structure in which the POST request data will be accepted
class User(BaseModel):
    name: str
    age: int
    address: str
    hobbies: List[str]

# Open the file in read mode, and store the contents in the variable users
with open("./data.json", "r") as file:
    users = json.load(file)

# Create an instance of the FastAPI app
app = FastAPI()

# Mount the app with the configuration to serve the static assets from the serve directory
app.mount("/static", StaticFiles(directory="serve"), name="static")

# The / route specifies the root address of the URL
# The GET method means that this request can also be analysed by entering the address on the browser address bar
@app.get("/")
async def root():
    return FileResponse("serve/index.html")


@app.get("/users")
def get_users(ageLimit: Optional[int] = None):

    if ageLimit is None:
        return users

    return [user for user in users if user["age"] <= ageLimit]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    return {}


@app.post("/users")
def add_user(user: User):

    new_user_id = len(users) + 1

    new_user = {
        "id": new_user_id,
        **user.dict()
    }

    users.append(new_user)

    return {
        "id": new_user_id
    }


