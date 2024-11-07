import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Import database session and models
from database1 import SessionLocal, engine
from model1 import CrimeReport, Base

# Create tables in the database (if they don’t exist already)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Pydantic schemas
class CrimeReportBase(BaseModel):
    Category: str
    Subcategory: str
    Crime_discreption: str
    Date: datetime
    Location: Optional[str] = None

    class Config:
        orm_mode = True

class CrimeReportCreate(CrimeReportBase):
    pass

class CrimeReportResponse(CrimeReportBase):
    Crime_id: int

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to create a new crime report
@app.post("/crime_reports/", response_model=CrimeReportResponse)
def create_crime_report(report: CrimeReportCreate, db: Session = Depends(get_db)):
    db_report = CrimeReport(
        Category=report.Category,
        Subcategory=report.Subcategory,
        Crime_discreption=report.Crime_discreption,
        Date=report.Date,
        Location=report.Location
    )
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

# Endpoint to read a specific crime report by ID
@app.get("/crime_reports/{crime_id}", response_model=CrimeReportResponse)
def read_crime_report(crime_id: int, db: Session = Depends(get_db)):
    db_report = db.query(CrimeReport).filter(CrimeReport.Crime_id == crime_id).first()
    if db_report is None:
        raise HTTPException(status_code=404, detail="Crime report not found")
    return db_report

# Endpoint to get a list of all crime reports
@app.get("/crime_reports/", response_model=List[CrimeReportResponse])
def read_crime_reports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reports = db.query(CrimeReport).offset(skip).limit(limit).all()
    return reports
