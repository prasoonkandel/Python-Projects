import random

hello_replies = [
    "Hello! How can I help you today?",
    "Hi there! What would you like me to do?",
    "Hey! Ready when you are.",
    "Hello, I’m here to assist you.",
    "Hi! I hope you're having a great day.",
    "Hey! What can I do for you?",
    "Hello! Let’s get started.",
    "Hi! How may I assist you today?"
]
whats_up_replies=[
    "All good here! How about you?",
    "Just doing my thing — assisting you!",
    "Nothing much, just waiting for your command.",
    "Everything's running smoothly!",
    "Just chillin’ in the code world.",
    "I'm fine, thanks for asking!",
    "I’m here, alive and coded!",
    "Running on logic and waiting for tasks!"
]
fine_replies = [
    "Glad to hear that!",
    "That's great!",
    "Awesome! How can I assist you today?",
    "Good to know!",
    "Happy to hear you're doing well.",
]

def hello_reply():
    reply = random.choice(hello_replies)
    return reply

def whats_up_reply():
    reply= random.choice(whats_up_replies)
    return reply
    

def fine_reply():
    reply = random.choice(fine_replies)
    return reply