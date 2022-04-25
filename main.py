from fastapi import FastAPI
app = FastAPI()
"""
this Decorator is used to create a new endpoint 
"""
@app.get("/") # component decorator is used to convert a function to something specialuse
def root(): # component2 function
    return {"message": "Hello World2"} # this data can be sent back

@app.get("/posts")
def read_posts():
    return {"message": "Hello Posts"}


