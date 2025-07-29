from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content : str


app = FastAPI()

@app.get("/")  # Decorator
async def root():
    return {"message" : "Welcome to my api"}

@app.get("/posts")
def get_post():
    return {"data" : "This is your post"} 

@app.post("/createposts")
def create_post(new_post: Post):

    
    print(new_post)
    return {"data" : "new_post"}
