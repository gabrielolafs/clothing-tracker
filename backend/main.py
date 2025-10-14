from fastapi.middleware.cors import CORSMiddleware  # ADD THIS IMPORT
from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from schemas import GarmentResponse, GarmentCreate
from database import get_db
from models import Garment

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
def get_garments(db: Session = Depends(get_db)):
    garments = db.query(Garment).all()
    return garments

@app.post("/garments", response_model=GarmentResponse, status_code=status.HTTP_201_CREATED)
def create_garment(garment: GarmentCreate, db: Session = Depends(get_db)):
    # Create new Garment instance from the incoming data
    db_garment = Garment(**garment.dict())

    # Add to database
    db.add(db_garment)
    db.commit()
    db.refresh(db_garment)  # Get the id and created_at back

    return db_garment

