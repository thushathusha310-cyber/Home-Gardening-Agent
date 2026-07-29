from agents.plant_agent import plant_care_agent
from agents.gardening_agent import gardening_advice_agent
from agents.knowledge_agent import knowledge_agent


def agent_controller(question):

    question_lower = question.lower()

    # PDF + Groq Knowledge Agent
    if any(word in question_lower for word in [
        "plant",
        "disease",
        "soil",
        "water",
        "watering",
        "fertilizer",
        "pest",
        "care",
        "how",
        "why"
    ]):
        print("Knowledge Agent Running")
        return knowledge_agent(question)

    # Default agent
    return gardening_advice_agent(question)