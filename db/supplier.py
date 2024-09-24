from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
import re

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    _email = Column(String, unique=True)
    _phone = Column(String, unique=True)
    address = Column(String)

    inventories = relationship('Inventory', back_populates='supplier')

    def __repr__(self):
        return f'<Supplier(id={self.id}, name={self.name})>'
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Supplier email cannot be empty")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email format")
        self._email = value.lower().strip()

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        if not value:
            raise ValueError("Supplier phone number cannot be empty")
        cleaned_number = re.sub(r'\D', '', value)
        if cleaned_number.startswith('254'):
            if len(cleaned_number) != 12:
                raise ValueError("Invalid phone number length for numbers starting with 254")
            formatted_number = f"+{cleaned_number[:3]} {cleaned_number[3:6]} {cleaned_number[6:9]} {cleaned_number[9:]}"
        elif cleaned_number.startswith('0'):
            if len(cleaned_number) != 10:
                raise ValueError("Invalid phone number length for numbers starting with 0")
            formatted_number = f"+254 {cleaned_number[1:4]} {cleaned_number[4:7]} {cleaned_number[7:]}"
        else:
            raise ValueError("Phone number must start with '254' or '0'")
        self._phone = formatted_number