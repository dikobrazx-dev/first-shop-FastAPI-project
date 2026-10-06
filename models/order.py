from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base
from .user import User
from .order_item import OrderItem
from typing import List

class Order(Base):
    __tablename__="orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship(back_populates = "orders")
    items: Mapped[List["OrderItem"]] = relationship(back_populates = "order")
