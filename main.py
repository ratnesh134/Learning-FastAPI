from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # Decorator
async def root():
    return {"message" : "Welcome to my api"}

@app.get("/posts")
def get_post():
    return {"data" : "This is your post"}