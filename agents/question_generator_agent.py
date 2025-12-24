from typing import Dict, List
from agents.product_parser_agent import Product


class QuestionGeneratorAgent:
    def run(self, product: Product) -> Dict[str, List[str]]:
        questions = {
            "Informational": [
                f"What is {product.name}?",
                f"What is the concentration of Vitamin C in {product.name}?",
                "What are the key ingredients of this serum?"
            ],
            "Usage": [
                "How should this serum be applied?",
                "How many drops should be used per application?",
                "Can this serum be used daily?"
            ],
            "Safety": [
                "Does this serum cause any side effects?",
                "Is this product suitable for sensitive skin?",
                "Who should avoid using this serum?"
            ],
            "Skin Type": [
                "Is this serum suitable for oily skin?",
                "Can people with combination skin use this serum?",
                "Is this serum suitable for dry skin?"
            ],
            "Purchase": [
                "What is the price of this serum?",
                "Is this product worth the price?",
                "Where can this serum be purchased?"
            ]
        }
        return questions
