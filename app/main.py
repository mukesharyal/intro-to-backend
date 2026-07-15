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


# TODO: Add the GET endpoint for /users that also expects an optional ageLimit parameter. When the ageLimit parameter is not present, it returns a list of all the users. When the parameter is present, it only returns the users whose age is less than or equal to the ageLimit

# TODO: Add the GET endpoint for /users/{user_id} that returns the user for that id by doing a lookup in the users list according to the id provided.

# TODO: Add the POST endpoint for /users that accepts the User object, adds the required id to the object, and finally appends the newly created user object to the users list


