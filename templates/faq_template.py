from logic_blocks.faq_answer_block import generate_faq_answer


def faq_template(product, questions):
    faqs = []

    for category, qs in questions.items():
        for q in qs:
            faqs.append({
                "question": q,
                "answer": generate_faq_answer(q, product)
            })

    return {
        "page_type": "FAQ",
        "product_name": product.name,
        "faqs": faqs[:5]
    }
