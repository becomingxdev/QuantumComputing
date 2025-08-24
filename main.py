from fastapi import FastAPI
from bb84 import simulate_bb84

# Create the FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Quantum Key Distribution (QKD) Service"}

@app.get("/api/v1/key")
def get_quantum_key():
    print("Request received: Running BB84 protocol simulation...")
    
    # Call the simulation function to get a key
    secure_key = simulate_bb84()
    
    if secure_key is not None:
        # If a key was generated, return it as a string
        return {
            "status": "success",
            "key_length": len(secure_key),
            "key": "".join(map(str, secure_key)) # Converts [1,0,1] to "101"
        }
    else:
        # If the key is None, it means a spy was detected
        return {
            "status": "error",
            "message": "Eavesdropper detected! Key generation aborted."
        }