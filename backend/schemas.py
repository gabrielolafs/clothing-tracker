from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base schema with common fields
class GarmentBase(BaseModel):
    type: str
    brand: Optional[str] = None
    color: Optional[str] = None
    size: Optional[str] = None
    price_paid: Optional[float] = None
    times_worn: int = 0
    times_since_washed: int = 0
    times_needed_before_wash: int = 1
    specific_attributes: Optional[dict] = None

# For creating a new garment (no id, no created_at)
class GarmentCreate(GarmentBase):
    pass

# For updating a garment (all fields optional)
class GarmentUpdate(BaseModel):
    type: Optional[str] = None
    brand: Optional[str] = None
    color: Optional[str] = None
    size: Optional[str] = None
    price_paid: Optional[float] = None
    times_worn: Optional[int] = None
    times_since_washed: Optional[int] = None
    times_needed_before_wash: Optional[int] = None
    specific_attributes: Optional[dict] = None
    last_time_worn: Optional[datetime] = None

# For responses (includes id and created_at)
class GarmentResponse(GarmentBase):
    id: int
    created_at: datetime
    last_time_worn: datetime

    class Config:
        from_attributes = True  # Allows SQLAlchemy models to work