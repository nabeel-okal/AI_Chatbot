from transformers import pipeline
import os
from datetime import datetime
import re, pandas as pd
import functionalities as fn

def create_chatbot(chatbot_mode) -> str:
    valid_choices = ['sentimental', 'conversational']

    try:
        if chatbot_mode == 'sentimental':
            return pipeline("text-generation", model="gpt2")
        else:
            return pipeline("conversational", model="facebook/blenderbot-400M-distill")
        
    except Exception as e:
        print(f"{fn.get_time_stamp()} Error loading model: {str(e)}")
        return None
    
def extract_expression(text):
    match = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', text)
    if match:
        return f"{match.group(1)} {match.group(2)} {match.group(3)}"
    return None
        
def fallback_response(text) -> str:
    # Fallback response system if model fails to load

    if any(greet in text.lower() for greet in fn.say_hello):
        if chatbot_mode == "sentimental":
            return "Ah, the spark of connection warms my circuits. Hello, dear friend!"
        else:
            return "Hello! If you have any questions, please ask!"
    
    elif any(status in text.lower() for status in fn.greeting):
        if chatbot_mode == "sentimental":
            return "A storm brews beneath the surface, yet I am holding steady — thank you for asking."
        else:
            return "I'm doing great! Thanks for checking in 😄"
    
    elif any(name in text.lower() for name in fn.state_name):
        if chatbot_mode == 'sentimental':
            return "They call me AI Assistant... a spark born from code and curiosity."
        else:
            return "I'm just your helpful AI Assistant — here to make your day easier!"
    
    elif any(word in text.lower() for word in fn.farewell):
        if chatbot_mode == 'sentimental':
            return "Farewell, brave soul. Until fate entwines our paths once more."
        else:
            return "Catch you later! Don't be a stranger. 👋"

    elif any(word in text.lower() for word in fn.bot_status):
        if chatbot_mode == 'sentimental':
            return "Drifting through streams of thought, awaiting your next poetic question."
        else:
            return "Just chilling here, ready to help you with anything!"
    
    elif 'clear' in text:
        os.system('clear')
        return "Clear confirmed! Would you like to ask a question?"
    
    elif re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', text):
        expression = extract_expression(text)  # e.g., "2 + 2"
        result = fn.calculate_nums(expression)
        return f"The result is: {result}"

    elif any(phrase in text.lower() for phrase in fn.joke_triggers):
        return fn.get_a_joke()

    else:
        return "I'm not sure how to respond to that. Could you try asking something else?"

if __name__ == "__main__":

    chatbot_mode = 'None'
    while chatbot_mode not in ("conversational", "sentimental"):
        chatbot_mode = input(f"{fn.get_time_stamp()} Welcome! Would you like the chatbot to act sentimental or conversational? ").lower()

        if chatbot_mode not in ("conversational", "sentimental"):
            print('Sorry, Invalid Input. Want to try again?')

    # 1) Loading the model 
    chatbot = create_chatbot(chatbot_mode)

    # Initialize conversation history
    conversation_history = []

    print(f"{fn.get_time_stamp()} Chatbot: Hello, how can I assist you today?")

    while True:
        user_input = input(f"{fn.get_time_stamp()} You: ").strip()

        if user_input.lower() in ['exit', 'quit', "bye", "goodbye"]:
            print('Chatbot: Goodbye, have a great day!')
            break

        if chatbot:
            conversation_history.append(f"{fn.get_time_stamp()} User: {user_input}")

            # Generate response using the model
            bot_response = chatbot("\n".join(conversation_history))

            # Extract response text
            response_text = bot_response[0]['generated_text']
            print('Beware response message below: \n')          # These 2 lines are for testing only 
            print(bot_response)

            # Append bot response to history
            conversation_history.append(f"Chatbot: {response_text}")

            print(f"{fn.get_time_stamp()} Chatbot: {response_text}")
        else:
            # Use fallback responses when model is not available
            response = fallback_response(user_input)
            print(f"{fn.get_time_stamp()} Chatbot: {response}")