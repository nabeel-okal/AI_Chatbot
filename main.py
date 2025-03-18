from transformers import pipeline
import time

def create_chatbot():
    try:
        print("Loading model, please wait...")
        return pipeline("conversational", model="facebook/blenderbot-400M-distill")
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        print("Falling back to default conversation handling...")
        return None
    
def fallback_response(text):
    """Fallback response system if model fails to load"""
    text = text.lower()
    if "hello" or "hi" or "hey" in text:
        return "Hello! If you have any questions, please ask!"
    elif "how are you" or"how's it going" in text:
        return "I'm doing well, thanks for asking!"
    elif "your name" or "your name?" or "what's your name?" or "what's your name" in text:
        return "I am a chatbot, you can call me AI Assistant."
    elif "bye" or "goodbye" in text:
        return "Goodbye! It was nice chatting with you."
    else:
        return "I'm not sure how to respond to that. Could you try asking something else?"


if __name__ == "__main__":

    # 1) Trying to load the model 
    chatbot = create_chatbot()

    # Initialize conversation history
    conversation_history = []

    print("Chatbot: Hello, how can I assist you today?")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ['exit', 'quit', "bye", "goodbye"]:
            print('Chatbot: Goodbye! Have a great day!')
            break

        if chatbot:
            conversation_history.append(f"User: {user_input}")

            # Generate response using the model
            bot_response = chatbot("\n".join(conversation_history))

            # Extract response text
            response_text = bot_response.get("generated_text", "I'm not sure how to respond to that.")

            # Append bot response to history
            conversation_history.append(f"Chatbot: {response_text}")

            print(f"Chatbot: {response_text}")
        else:
            # Use fallback responses when model is not available
            response = fallback_response(user_input)
            print(f"Chatbot: {response}")

