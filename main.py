# 1. Import the FastAPI class
from fastapi import FastAPI

# 2. Create an "instance" of the FastAPI application
app = FastAPI()

# 3. Define an endpoint using a "decorator"
@app.get("/")
def read_root():
    # 4. Return a Python dictionary
    return {"message": "Hello, Quantum World!"}

@app.get("/api/v1/key")
def get_quantum_key():
    return {
        "key_id": "c4a7f3e1",
        "key_length": 16,
        "key": "1011010011101101"
    }