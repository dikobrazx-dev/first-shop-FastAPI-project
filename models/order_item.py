from dataclasses import dataclass
@dataclass
class Order:
    order_id: int
    product_id: int
    quantity: int