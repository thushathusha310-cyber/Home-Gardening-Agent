def planning_agent(question):

    message = {
        "sender": "planning_agent",
        "receiver": "knowledge_agent",
        "task": "retrieve_gardening_information",
        "query": question,
        "steps": [
            "Analyze user gardening question",
            "Retrieve relevant knowledge",
            "Prepare information for final response"
        ]
    }

    return message