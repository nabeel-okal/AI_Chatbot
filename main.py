from transformers import pipeline
import time, os
from datetime import datetime
import re
def get_time_stamp() -> str:
    return datetime.now().strftime("[%H:%M:%S]")


def create_chatbot(choice) -> str:
    valid_choices = ['sentimental', 'conversational']

    try:
        if choice == 'sentimental':
            return pipeline("text-generation", model="gpt2")
        else:
            return pipeline("conversational", model="facebook/blenderbot-400M-distill")
        
    except Exception as e:
        print(f"{get_time_stamp()} Error loading model: {str(e)}")
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
    
def fallback_response(text) -> str:
    # Fallback response system if model fails to load

    text = text.lower()
    if "hello" in text or "hi" in text or "hey" in text:
        return "Hello! If you have any questions, please ask!"
    
    elif "how are you" in text or "how's it going" in text:
        return "I'm doing well, thanks for asking!"
    
    elif "your name" in text or "your name?" in text or "what's your name?" in text or "what's your name" in text:
        return "I am a chatbot, you can call me AI Assistant."
    
    elif "bye" in text or "goodbye" in text:
        return "Goodbye! It was nice chatting with you."
    
    elif 'what are you doing' in text or 'what are you doing?' in text or 'whatcha doing' in text or 'whatcha doing?' in text:
        return "Nothing really, just answering your questions. Feel free to ask anything you want."
    
    elif 'clear' in text:
        os.system('clear')
        return "Clear confirmed! Would you like to ask a question?"
    
    elif re.match(r'^\d+\s*[+\-*/]\s*\d+$', text.strip()):
        return calculate_nums(text)
    else:
        return "I'm not sure how to respond to that. Could you try asking something else?"
    
if __name__ == "__main__":

    choice = 'None'
    while choice not in ("conversational", "sentimental"):
        choice = input(f"{get_time_stamp()} Welcome! Would you like the chatbot to act sentimental or conversational? ").lower()

        if choice not in ("conversational", "sentimental"):
            print('Sorry, Invalid Input. Want to try again?')


    # 1) Trying to load the model 
    chatbot = create_chatbot(choice)

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