from maslib.agent.baseagent import BaseAgent
from maslib.messages.user import UserMessage
from maslib.messages.system import SystemMessage
from maslib.messages.base import BaseMessage

class Agent(BaseAgent):
    def __init__(self, **kwargs):
        """
        Initializes the Agent with custom properties.

        Parameters:
        - **kwargs: Arbitrary keyword arguments containing the attributes such as `name`, `role`, `goal`, and `backstory`.

        This method sets up the agent by defining its context and initializing a system message
        to provide a backstory and a defined role for the agent.
        """
        super().__init__(**kwargs)
        SystemMessage(content=f"""You are a {self.name} agent with your task as {self.role} with a goal of:{self.goal} and with a backstory of {self.backstory}""")

    def invoke(self, query: str) -> str:
        """
        Processes a user query and generates a response.

        Parameters:
        - query (str): The input query from the user to be processed by the agent.

        Returns:
        - str: The response generated by the agent's language model (LLM).

        This method creates a user message based on the input query, passes it to the
        language model for processing, and returns the generated response.
        """
        UserMessage(content=query)
        
        response = self.llm.invoke(BaseMessage.messages)
        return response
