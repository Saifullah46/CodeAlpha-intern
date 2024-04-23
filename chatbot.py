#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm good, thanks for asking.", "I'm fine, how about you?"]
    ],
    [
        r"(.*) your name ?",
        ["I'm a chatbot!", "You can call me Chatbot.", "My name is Chatbot."]
    ],
    [
        r"(.*) (help|support)",
        ["Sure, I can help you. What do you need assistance with?", "How can I assist you?"]
    ],
    [
        r"(.) (weather|temperature) in (.)",
        ["Sorry, I'm just a simple chatbot and I can't check the weather."]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye!", "See you later!", "Bye!"]
    ],
]

# Create a Chat instance with pairs and reflections
chatbot = Chat(pairs, reflections)

def chat_with_bot():
    print("Hello! I'm a chatbot. How can I help you today?")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() in ["quit", "bye", "exit"]:
            break

# Call the function to start chatting with the chatbot
chat_with_bot()


# In[ ]:




