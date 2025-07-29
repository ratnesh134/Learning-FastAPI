from fastapi import FastAPI
from fastapi.params import Body
from pydantic import schema

app = FastAPI()

@app.get("/")  # Decorator
async def root():
    return {"message" : "Welcome to my api"}

@app.get("/posts")
def get_post():
    return {"data" : "This is your post"} 

@app.post("/createposts")
def create_post(payLoad: dict=Body(...)):

    print(payLoad)

    return {"new_post" : f"title : {payLoad['Title']} , Content : {payLoad['Content']}"}
