from agents.product_parser_agent import Product


def generate_faq_answer(question: str, product: Product) -> str:
    q = question.lower()

    if "what is" in q:
        return f"{product.name} is a skincare serum formulated with {', '.join(product.key_ingredients)}."

    if "concentration" in q:
        return f"It contains {product.concentration}."

    if "key ingredients" in q:
        return f"The key ingredients are {', '.join(product.key_ingredients)}."

    if "how should" in q or "how many drops" in q:
        return product.how_to_use

    if "side effects" in q or "sensitive skin" in q:
        return product.side_effects

    if "price" in q:
        return f"The product is priced at ₹{product.price}."

    if "skin" in q:
        return f"This product is suitable for {', '.join(product.skin_type)} skin types."

    return "Please refer to the product details for more information."
