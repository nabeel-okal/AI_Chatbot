from transformers import pipeline
import time, os
from datetime import datetime

# Adding Timestamps to Messages (User & Chatbot)
timestamp = datetime.now().strftime("[%H:%M:%S]")

def create_chatbot(choice):
    try:
        print(f"{timestamp} Loading model, please wait...")
        return pipeline(choice, model="facebook/blenderbot-400M-distill")
    except Exception as e:
        print(f"{timestamp} Error loading model: {str(e)}")
        print(f"{timestamp} Falling back to default conversation handling...")
        return None
    
def fallback_response(text):
    """Fallback response system if model fails to load"""
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
    else:
        return "I'm not sure how to respond to that. Could you try asking something else?"
    
if __name__ == "__main__":

    # I must add here a restriction for these 2 choices

    choice = input(f"{timestamp} Welcome! Would you like the chatbot to act sentimental or conversational? ")

    # 1) Trying to load the model 
    chatbot = create_chatbot(choice)

    # Initialize conversation history
    conversation_history = []

    print(f"{timestamp} Chatbot: Hello, how can I assist you today?")

    while True:
        user_input = input(f"{timestamp} You: ").strip()

        if user_input.lower() in ['exit', 'quit', "bye", "goodbye"]:
            print('Chatbot: Goodbye! Have a great day!')
            break

        if chatbot:
            conversation_history.append(f"{timestamp} User: {user_input}")

            # Generate response using the model
            bot_response = chatbot("\n".join(conversation_history))

            # Extract response text
            response_text = bot_response[0]['generated_text']
            print('Beware response message below: \n')          # These 2 lines are for testing only 
            print(bot_response)

            # Append bot response to history
            conversation_history.append(f"Chatbot: {response_text}")

            print(f"{timestamp} Chatbot: {response_text}")
        else:
            # Use fallback responses when model is not available
            response = fallback_response(user_input)
            print(f"{timestamp} Chatbot: {response}")