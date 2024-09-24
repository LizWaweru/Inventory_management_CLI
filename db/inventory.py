from sqlalchemy import Column, Integer, String, Float, func, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Inventory(Base):
    __tablename__ = 'inventories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)
    _unit_price = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    category_id = Column(Integer, ForeignKey('categories.id'))
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    category = relationship('Category', back_populates='inventories')
    supplier = relationship('Supplier', back_populates='inventories')
    transactions = relationship('Transaction', back_populates='inventory')

    def __repr__(self):
        return f'<Inventory(id={self.id}, name={self.name})>'
    
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        if value <= 0:
            raise ValueError("Unit price must be greater than zero")
        self._unit_price = value