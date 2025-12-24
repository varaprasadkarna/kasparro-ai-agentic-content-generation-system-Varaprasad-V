from agents.product_parser_agent import Product


def generate_benefits_block(product: Product) -> dict:
    return {
        "title": "Key Benefits",
        "items": product.benefits
    }
