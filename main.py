from crewai import Crew
from tasks.question_task import question_task

def parse_input(raw):
    parts = [p.strip() for p in raw.split(";")]
    return {
        "product_name": parts[0],
        "concentration": parts[1],
        "skin_type": [s.strip() for s in parts[2].split(",")],
        "key_ingredients": [i.strip() for i in parts[3].split(",")],
        "benefits": [b.strip() for b in parts[4].split(",")],
        "how_to_use": parts[5],
        "side_effects": parts[6],
        "price": int(parts[7]),
    }

raw_input_data = input(
    "\nEnter product data in ONE line (semicolon separated):\n\n"
)

product_data = parse_input(raw_input_data)

crew = Crew(
    agents=[question_task.agent],
    tasks=[question_task],
    verbose=True
)

results = crew.kickoff(inputs=product_data)
print("\nFINAL OUTPUT:\n", results)
