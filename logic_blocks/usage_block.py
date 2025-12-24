from agents.product_parser_agent import Product


def generate_usage_block(product: Product) -> dict:
    return {
        "title": "How to Use",
        "instructions": product.how_to_use
    }
