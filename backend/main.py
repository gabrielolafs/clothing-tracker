from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, status, HTTPException
from sqlalchemy.orm import Session

from schemas import GarmentResponse, GarmentCreate, GarmentUpdate
from database import get_db
from models import Garment
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/")
def read_root():
    return {"message": "Hello World"}

@app.get("/api/garments")
def get_garments(db: Session = Depends(get_db)):
    garments = db.query(Garment).all()
    return garments

@app.post("/api/garments", response_model=GarmentResponse, status_code=status.HTTP_201_CREATED)
def create_garment(garment: GarmentCreate, db: Session = Depends(get_db)):
    # Create new Garment instance from the incoming data
    db_garment = Garment(**garment.dict())

    # Add to database
    db.add(db_garment)
    db.commit()
    db.refresh(db_garment)  # Get the id and created_at back

    return db_garment

@app.post("/api/garments/{garment_id}/wear", response_model=GarmentResponse)
def wear_garment(garment_id: int, db: Session = Depends(get_db)):
    db_garment = db.query(Garment).filter(Garment.id == garment_id).first()

    if not db_garment:
        raise HTTPException(status_code=404, detail="Garment not found")

    db_garment.times_worn += 1
    db_garment.times_since_washed += 1
    db_garment.last_time_worn = datetime.utcnow()

    db.commit()
    db.refresh(db_garment)

    return db_garment

@app.post("/api/garments/{garment_id}/clean", response_model=GarmentResponse)
def clean_garment(garment_id: int, db: Session = Depends(get_db)):
    db_garment = db.query(Garment).filter(Garment.id == garment_id).first()

    if not db_garment:
        raise HTTPException(status_code=404, detail="Garment not found")

    db_garment.times_since_washed = 0

    db.commit()
    db.refresh(db_garment)

    return db_garment

@app.put("/api/garments/{garment_id}", response_model=GarmentResponse)  # Use PUT, not POST
def edit_garment(garment_id: int, garment_update: GarmentUpdate, db: Session = Depends(get_db)):
    # Find garment
    db_garment = db.query(Garment).filter(Garment.id == garment_id).first()

    if not db_garment:
        raise HTTPException(status_code=404, detail="Garment not found")

    # Update only the fields that were sent
    update_data = garment_update.dict(exclude_unset=True)  # Only fields user provided
    for key, value in update_data.items():
        setattr(db_garment, key, value)  # Set each field

    db.commit()
    db.refresh(db_garment)
    return db_garment

@app.delete("/api/garments/{garment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_garment(garment_id: int, db: Session = Depends(get_db)):
    db_garment = db.query(Garment).filter(Garment.id == garment_id).first()

    if not db_garment:
        raise HTTPException(status_code=404, detail="Garment not found")

    db.delete(db_garment)
    db.commit()

    return