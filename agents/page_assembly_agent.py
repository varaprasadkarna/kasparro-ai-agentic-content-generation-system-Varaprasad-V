import json
from templates.faq_template import faq_template
from templates.product_template import product_page_template
from templates.comparison_template import comparison_page_template


class PageAssemblyAgent:
    def run(self, product, questions):
        faq_page = faq_template(product, questions)
        product_page = product_page_template(product)
        comparison_page = comparison_page_template(product)

        with open("outputs/faq.json", "w") as f:
            json.dump(faq_page, f, indent=2)

        with open("outputs/product_page.json", "w") as f:
            json.dump(product_page, f, indent=2)

        with open("outputs/comparison_page.json", "w") as f:
            json.dump(comparison_page, f, indent=2)
