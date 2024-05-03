import nltk
import random
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi, how can I help you?"]
    ],
    [
        r"how are you?",
        ["I'm good, thank you!", "I'm doing well, thanks for asking and you sir?", "All good! How about you?"]
    ],
    [
        r"what is your name?",
        ["You can call me ChatBot.", "I'm ChatBot.", "I go by the name ChatBot."]
    ],
    [
        r"I am fine",
        ["Great to hear, So what do you wanna talk about?"]
    ],
    [
        r"Do you know what am I doing right now?",
        ["You are having conversation with me sir, haha"]
    ],
    [
        r"quit|bye|goodbye|see ya",
        ["Bye! Take care.", "Goodbye! Have a great day.", "See you later!"]
    ],
    [
        r"(.*) your name?",
        ["My name is ChatBot.", "I'm ChatBot, nice to meet you!"]
    ],
    [
        r"jokes aside",
        ["You are making an explanation video of this project and will be posting on LinkedIn soon enough."]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you with various topics. Just ask me anything!", "Sure, I'm here to help. What do you need assistance with?"]
    ],
    
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual assistant, so I don't have a physical location. But I'm here to assist you wherever you are."]
    ],
    [
        r"(.*) (created|made) you ?",
        ["I was created by an awesome developer using Python and NLTK library."]
    ],
    [
        r"(.*) (weather|temperature) ?",
        ["I'm sorry, I don't have access to real-time weather data at the moment."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't quite understand that. Could you please rephrase or ask something else?"]
    ]
]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm a simple chatbot. You can start chatting with me. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    chat()
