from agents.product_parser_agent import ProductParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.page_assembly_agent import PageAssemblyAgent

raw_product_data = {
    "product_name": "GlowBoost Vitamin C Serum",
    "concentration": "10% Vitamin C",
    "skin_type": ["Oily", "Combination"],
    "key_ingredients": ["Vitamin C", "Hyaluronic Acid"],
    "benefits": ["Brightening", "Fades dark spots"],
    "how_to_use": "Apply 2–3 drops in the morning before sunscreen",
    "side_effects": "Mild tingling for sensitive skin",
    "price": 699
}

parser = ProductParserAgent()
product = parser.run(raw_product_data)

question_agent = QuestionGeneratorAgent()
questions = question_agent.run(product)

page_agent = PageAssemblyAgent()
page_agent.run(product, questions)
