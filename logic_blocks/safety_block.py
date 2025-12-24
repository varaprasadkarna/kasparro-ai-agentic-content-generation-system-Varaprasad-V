from agents.product_parser_agent import Product


def generate_safety_block(product: Product) -> dict:
    return {
        "title": "Safety Information",
        "side_effects": product.side_effects
    }
