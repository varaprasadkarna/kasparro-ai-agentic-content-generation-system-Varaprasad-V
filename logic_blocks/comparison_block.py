from agents.product_parser_agent import Product


def generate_comparison_block(product: Product, competitor: dict) -> dict:
    return {
        "product_a": {
            "name": product.name,
            "ingredients": product.key_ingredients,
            "benefits": product.benefits,
            "price": product.price
        },
        "product_b": competitor
    }
