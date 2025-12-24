from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    name: str
    concentration: str
    skin_type: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: int


class ProductParserAgent:
    def run(self, raw_data: dict) -> Product:
        product = Product(
            name=raw_data["product_name"],
            concentration=raw_data["concentration"],
            skin_type=raw_data["skin_type"],
            key_ingredients=raw_data["key_ingredients"],
            benefits=raw_data["benefits"],
            how_to_use=raw_data["how_to_use"],
            side_effects=raw_data["side_effects"],
            price=raw_data["price"]
        )
        return product
