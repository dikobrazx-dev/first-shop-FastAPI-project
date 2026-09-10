from dataclasses import dataclass
@dataclass
class OrderItem:
    order_id: int
    product_id: int
    quantity: int