from transformers import pipeline
import time, os
from datetime import datetime

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
    
def calculate_nums(n1, n2, op) -> int:
    n1, n2 = int(n1), int(n2)

    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2

    
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
    
    elif 'clear' in text:
        os.system('clear')
        return "Clear confirmed! Would you like to ask a question?"
    
    elif "calculate" in text or "what is" in text or '+' in text or '-' in text or '*' in text or '/' in text:
        word = text.split()
        arg1 = 0
        arg2 = 0
        arg3 = ''

        for i in range(0, len(text) + 1):
            if word[i].isdigit():        # Limited range of numbers for now
                arg1 = word[i]
            if word[i].isdigit():        # Limited range of numbers for now
                arg2 = word[i]
            if(word[i] in ['+', '-', '/', '*']):
                arg3 = word[i]
        return calculate_nums(arg1, arg2, arg3)
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