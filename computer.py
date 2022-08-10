from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ( Column, String, BigInteger)

Base = declarative_base()

class Computer(Base):

    __tablename__ = "computer"
    
    computer_id = Column(BigInteger , nullable = False, unique = True, primary_key = True)
    harddrive_type = Column(String(55), nullable = False)
    processor = Column(String(55), nullable=False)
    ram_amount = Column(String(55), nullable = False)
    max_ram = Column(String(55) , nullable = False)
    harddrive_space = Column(String(55), nullable = False)
    form_factor = Column(String(55))

    def __init__(self, harddrive_type, processor, ram_amount, max_ram, harddrive_space, form_factor):

        self.harddrive_type = harddrive_type
        self.processor = processor
        self.ram_amount = ram_amount
        self.max_ram = max_ram
        self.harddrive_space = harddrive_space
        self.form_factor = form_factor
   
    