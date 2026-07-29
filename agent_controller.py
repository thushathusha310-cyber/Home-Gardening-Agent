from agents.plant_agent import plant_care_agent
from agents.gardening_agent import gardening_advice_agent
from agents.knowledge_agent import knowledge_agent

from agents.planning_agent import planning_agent
from agents.reflection_agent import reflection_agent


def agent_controller(question):

    question_lower = question.lower()

    # Planning Agent
    plan = planning_agent(question)

    # Knowledge Agent
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

        answer = knowledge_agent(plan)

    else:
        answer = gardening_advice_agent(plan)


    # Reflection Agent
    final_answer = reflection_agent(answer)

    return final_answer