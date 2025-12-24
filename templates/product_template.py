from logic_blocks.benefits_block import generate_benefits_block
from logic_blocks.usage_block import generate_usage_block
from logic_blocks.safety_block import generate_safety_block


def product_page_template(product):
    return {
        "page_type": "Product Page",
        "product_name": product.name,
        "concentration": product.concentration,
        "skin_type": product.skin_type,
        "ingredients": product.key_ingredients,
        "benefits": generate_benefits_block(product),
        "usage": generate_usage_block(product),
        "safety": generate_safety_block(product),
        "price": product.price
    }
