def faq_template(product, questions):
    faqs = []

    for category, qs in questions.items():
        for q in qs:
            faqs.append({
                "question": q,
                "answer": "Answer derived from product information"
            })

    return {
        "page_type": "FAQ",
        "product_name": product.name,
        "faqs": faqs[:5]
    }
