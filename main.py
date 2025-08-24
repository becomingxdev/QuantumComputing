# 1. Import the FastAPI class
from fastapi import FastAPI

# 2. Create an "instance" of the FastAPI application
app = FastAPI()

# 3. Define an endpoint using a "decorator"
@app.get("/")
def read_root():
    # 4. Return a Python dictionary
    return {"message": "Hello, Quantum World!"}