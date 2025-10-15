from sqlalchemy import Column, Integer, String, DECIMAL, JSON, TIMESTAMP
from database import Base
import datetime

class Garment(Base):
    __tablename__ = "garments"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), nullable=False)
    brand = Column(String(100))
    color = Column(String(7))
    size = Column(String(20))
    price_paid = Column(DECIMAL(10, 2))
    times_worn = Column(Integer, default=0)
    times_since_washed = Column(Integer, default=0)
    times_needed_before_wash = Column(Integer, default=1)
    specific_attributes = Column(JSON)  # Store extra info like {"neckline": "crew", "length_in": 28.5}
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    last_time_worn = Column(TIMESTAMP, nullable=True)