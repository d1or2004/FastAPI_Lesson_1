# Download and Install FASTAPI
"""pip install fastapi uvicorn """
from fastapi import FastAPI
from auth import model_auth

# run fastapi
"""uvicorn main:app --reload"""


app = FastAPI()
app.include_router(model_auth)


@app.get("/")
async def intro():
    return {
        "message": "This is landing page!"
    }


@app.get("/test")
async def test1():
    return {
        "message": "Hello! "
    }


@app.get("/test2")
async def test2():
    return {
        "message": "Group -> N37. Hello"
    }
