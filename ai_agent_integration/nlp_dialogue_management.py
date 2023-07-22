```python
class NLPDialogueManagement:
    def __init__(self, ai_agents):
        self.ai_agents = ai_agents

    def handle_query(self, query):
        intent = self.extract_intent(query)
        if intent in self.ai_agents:
            return self.ai_agents[intent].generate_response(query)
        else:
            return "Sorry, I couldn't understand your query."

    def extract_intent(self, query):
        # Use NLU technology to extract intent from the query
        intent = "unknown"
        # Logic to extract intent from the query
        return intent


class AIAgents:
    def __init__(self):
        self.agents = {}

    def add_agent(self, intent, agent):
        self.agents[intent] = agent

    def generate_response(self, query):
        # Logic to generate response based on the query
        response = "This is the response for the query: " + query
        return response


# Create an instance of AI agents
ai_agents = AIAgents()

# Create and add AI agents to the dialogue management
ai_agent_1 = AIChatbotAgent()
ai_agents.add_agent("greeting", ai_agent_1)

ai_agent_2 = AIVoicebotAgent()
ai_agents.add_agent("order_status", ai_agent_2)

# Create an instance of NLP dialogue management
nlp_dialogue_management = NLPDialogueManagement(ai_agents)

# Handle user queries
query = "Hello, how can I help you?"
response = nlp_dialogue_management.handle_query(query)
print(response)
```

In the code above, we have defined the `NLPDialogueManagement` class that handles the dialogue management for the AI agents. It takes an instance of `AIAgents` as a parameter, which contains the different AI agents mapped to their respective intents. The `handle_query` method extracts the intent from the query using NLU technology and then uses the intent to determine which AI agent to use for generating the response.

The `AIAgents` class is responsible for managing the different AI agents. It has a `add_agent` method to add AI agents to the collection and a `generate_response` method to generate a response based on the query.

In the example code, we create an instance of `AIAgents` and add two AI agents (`AIChatbotAgent` and `AIVoicebotAgent`) to it. We then create an instance of `NLPDialogueManagement` and pass the `AIAgents` instance to it. Finally, we handle a user query by calling the `handle_query` method of `NLPDialogueManagement` and print the response.

Please note that the code provided is a simplified example and may need to be adapted to your specific implementation and requirements.