from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database1 import Base
class CrimeReport(Base):
    __tablename__ = 'crime_reports'

    Crime_id = Column(Integer, primary_key=True, index=True)
    Category = Column(String(100), nullable=False, index=True)
    Subcategory = Column(String(100), nullable=False, index=True)
    Crime_discreption = Column(String, nullable=False)
    Date = Column(DateTime, nullable=False)
    Location = Column(String(150), nullable=True)
    
    # Define any relationships here if necessary

    def __repr__(self):
        return f"<CrimeReport(id={self.Crime_id}, category='{self.Category}', subcategory='{self.Subcategory}')>"
