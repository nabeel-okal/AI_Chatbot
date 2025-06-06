from transformers import pipeline
import time, os
from datetime import datetime
import re, pandas as pd
import random

def get_time_stamp() -> str:
    return datetime.now().strftime("[%H:%M:%S]")


def create_chatbot(chatbot_mode) -> str:
    valid_choices = ['sentimental', 'conversational']

    try:
        if chatbot_mode == 'sentimental':
            return pipeline("text-generation", model="gpt2")
        else:
            return pipeline("conversational", model="facebook/blenderbot-400M-distill")
        
    except Exception as e:
        print(f"{get_time_stamp()} Error loading model: {str(e)}")
        return None
    
def extract_expression(text):
    match = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', text)
    if match:
        return f"{match.group(1)} {match.group(2)} {match.group(3)}"
    return None

def calculate_nums(text):
    match = re.search(r'^(\d+)\s*([+\-*/])\s*(\d+)$', text.strip())
    arg1 = int(match.group(1))
    op = match.group(2)
    arg2 = int(match.group(3))
    
    if not match:
        return "I didn't understand. Could you provide a valid calculation prompt?"

    try:
        arg1 = int(match.group(1))
        op = match.group(2)
        arg2 = int(match.group(3))
        
        if op == '+':
            r = arg1 + arg2
            return str(r)
        elif op == '-':
            r = arg1 - arg2
            return str(r)
        elif op == '*':
            r = arg1 * arg2
            return str(r)
        elif op == '/':
            r = arg1 / arg2
            if arg2 == 0:
                return "Division by zero is not allowed."
            return str(r)
        else:
            return "I didn't understand. Could you provide a valid calculation prompt?"
    except Exception as e:
        return f"Error in calculation: {str(e)}"
        
def get_a_joke():
    jokes = pd.read_csv('funjokes.csv')
    jokes_list = jokes["Joke"].tolist()
    random_index = random.randint(0, len(jokes_list) - 1)
    return jokes_list[random_index]
        
def fallback_response(text) -> str:
    # Fallback response system if model fails to load

    joke_triggers = [
        "tell me a joke",
        "tell me a joke.",
        "a joke",
        "a joke?",
        "another one",
        "another one.",
        "another one?"
    ]
    
    bot_status = [
        'what are you doing',
        'what are you doing?',
        'whatcha doing',
        'whatcha doing?'
    ]

    farewell = [
        'bye',
        'goodbye',
        'gtg',
        'g2g'
    ]

    greeting = [
        'how are you',
        'how are you?',
        'how are you doing',
        'how are you doing?',
        "how's it going",
        "how's it going?" 
    ]

    say_hello = [
        'hello',
        'hello?',
        'hi',
        'hi?',
        'hey',
        'hey!'
    ]

    state_name = [
        'your name',
        'your name?',
        "what's your name",
        "what's your name?"
    ]

    if any(greet in text.lower() for greet in say_hello):
        if chatbot_mode == "sentimental":
            return "Ah, the spark of connection warms my circuits. Hello, dear friend!"
        else:
            return "Hello! If you have any questions, please ask!"
    
    elif any(status in text.lower() for status in greeting):
        if chatbot_mode == "sentimental":
            return "A storm brews beneath the surface, yet I am holding steady — thank you for asking."
        else:
            return "I'm doing great! Thanks for checking in 😄"
    
    elif any(name in text.lower() for name in state_name):
        if chatbot_mode == 'sentimental':
            return "They call me AI Assistant... a spark born from code and curiosity."
        else:
            return "I'm just your helpful AI Assistant — here to make your day easier!"
    
    elif any(word in text.lower() for word in farewell):
        if chatbot_mode == 'sentimental':
            return "Farewell, brave soul. Until fate entwines our paths once more."
        else:
            return "Catch you later! Don't be a stranger. 👋"

    elif any(word in text.lower() for word in bot_status):
        if chatbot_mode == 'sentimental':
            return "Drifting through streams of thought, awaiting your next poetic question."
        else:
            return "Just chilling here, ready to help you with anything!"
    
    elif 'clear' in text:
        os.system('clear')
        return "Clear confirmed! Would you like to ask a question?"
    
    elif re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', text):
        expression = extract_expression(text)  # e.g., "2 + 2"
        result = calculate_nums(expression)
        return f"The result is: {result}"

    elif any(phrase in text.lower() for phrase in joke_triggers):
        return get_a_joke()

    else:
        return "I'm not sure how to respond to that. Could you try asking something else?"

if __name__ == "__main__":

    chatbot_mode = 'None'
    while chatbot_mode not in ("conversational", "sentimental"):
        chatbot_mode = input(f"{get_time_stamp()} Welcome! Would you like the chatbot to act sentimental or conversational? ").lower()

        if chatbot_mode not in ("conversational", "sentimental"):
            print('Sorry, Invalid Input. Want to try again?')

    # 1) Loading the model 
    chatbot = create_chatbot(chatbot_mode)

    # Initialize conversation history
    conversation_history = []

    print(f"{get_time_stamp()} Chatbot: Hello, how can I assist you today?")

    while True:
        user_input = input(f"{get_time_stamp()} You: ").strip()

        if user_input.lower() in ['exit', 'quit', "bye", "goodbye"]:
            print('Chatbot: Goodbye, have a great day!')
            break

        if chatbot:
            conversation_history.append(f"{get_time_stamp()} User: {user_input}")

            # Generate response using the model
            bot_response = chatbot("\n".join(conversation_history))

            # Extract response text
            response_text = bot_response[0]['generated_text']
            print('Beware response message below: \n')          # These 2 lines are for testing only 
            print(bot_response)

            # Append bot response to history
            conversation_history.append(f"Chatbot: {response_text}")

            print(f"{get_time_stamp()} Chatbot: {response_text}")
        else:
            # Use fallback responses when model is not available
            response = fallback_response(user_input)
            print(f"{get_time_stamp()} Chatbot: {response}")