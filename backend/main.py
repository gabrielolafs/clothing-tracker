from fastapi.middleware.cors import CORSMiddleware  # ADD THIS IMPORT
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/garments")
def get_garments():
    return [
        {
            "id": 1,
            "type": "shirt",
            "brand": "Nike",
            "color": "#0000FF",
            "size": "L",
            "price_paid": 29.99,
            "times_worn": 5,
            "times_since_washed": 2,
            "times_needed_before_wash": 3,
            "specific_attributes": {"neckline": "crew", "length_in": 28.5},
            "created_at": "2025-10-13T10:00:00"
        },
        {
            "id": 2,
            "type": "shirt",
            "brand": "Nike",
            "color": "#0FF0FF",
            "size": "L",
            "price_paid": 29.99,
            "times_worn": 5,
            "times_since_washed": 2,
            "times_needed_before_wash": 3,
            "specific_attributes": {"neckline": "crew", "length_in": 28.5},
            "created_at": "2025-10-13T10:00:00"
        }
    ]
