from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .order_item import OrderItem
class Product(Base):
    __tablename__="products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float]
    
    items: Mapped["OrderItem"] = relationship(back_populates = "product")