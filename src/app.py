from dotenv import load_dotenv
from agents import ConversationAgent, SmartChatAgent

load_dotenv()

from interface import AudioInterface

interface = AudioInterface()
# agent = ConversationAgent()
agent = SmartChatAgent()

while True:
    text = interface.listen()
    response = agent.run(text)

    print(response)
    print(type(response))

    interface.speak(response['output'])