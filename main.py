from agents.product_parser_agent import ProductParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.page_assembly_agent import PageAssemblyAgent


def parse_raw_input(raw_text: str) -> dict:
    parts = [p.strip() for p in raw_text.split(";")]

    if len(parts) != 8:
        raise ValueError("Invalid input format. Expected 8 fields separated by semicolons.")

    return {
        "product_name": parts[0],
        "concentration": parts[1],
        "skin_type": [s.strip() for s in parts[2].split(",")],
        "key_ingredients": [i.strip() for i in parts[3].split(",")],
        "benefits": [b.strip() for b in parts[4].split(",")],
        "how_to_use": parts[5],
        "side_effects": parts[6],
        "price": int(parts[7])
    }


def run_pipeline():
    print("Enter product data in the following format:\n")
    print("Product Name; Concentration; Skin Types; Ingredients; Benefits; How to Use; Side Effects; Price\n")

    raw_text = input("Enter product data:\n")

    raw_product_data = parse_raw_input(raw_text)

    parser = ProductParserAgent()
    product = parser.run(raw_product_data)

    question_agent = QuestionGeneratorAgent()
    questions = question_agent.run(product)

    page_agent = PageAssemblyAgent()
    page_agent.run(product, questions)


if __name__ == "__main__":
    run_pipeline()
