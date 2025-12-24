from logic_blocks.comparison_block import generate_comparison_block


def comparison_page_template(product):
    fictional_product_b = {
        "name": "RadiantGlow Serum",
        "ingredients": ["Vitamin C"],
        "benefits": ["Skin brightening"],
        "price": 899
    }

    return {
        "page_type": "Comparison Page",
        "comparison": generate_comparison_block(product, fictional_product_b)
    }
