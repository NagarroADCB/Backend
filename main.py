from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to the specific origin you want to allow
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/eligibility-check")
async def eligibility_check():
    # Simple example logic for eligibility check
    # Replace this with your actual business logic
    is_eligible = True  # or False, depending on your conditions
    
    return is_eligible