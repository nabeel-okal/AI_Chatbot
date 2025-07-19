import pandas as pd
import random
import re
from datetime import datetime

joke_triggers = [
    "tell me a joke", "tell me a joke.", "tell me a joke!",
    "say a joke", "say something funny", "tell something funny",
    "make me laugh", "give me a laugh", "cheer me up", "make me smile",
    "i want to hear a joke", "can you make me laugh?", "another joke please",
    "got any jokes?", "another one", "another one?", "one more joke",
    "one more, please", "funny time", "got something funny?", "make me giggle",
    "humor me", "i need a laugh", "any good jokes?", "can you joke?",
    "joke?", "a joke?", "i want a joke", "joke time!", "anything funny?",
    "anything to laugh about?", "laugh please", "funny stuff please",
    "you're funny, say another", "haha say more", "keep going with the jokes",
    "say one more", "i liked that one, another?", "your best joke!",
    "a funny one please", "your funniest", "say your favorite joke",
    "impress me with a joke", "try to be funny", "humorous stuff please",
    "you know any jokes?", "speak a joke", "throw a joke", "joke me",
    "another funny line"
]

bot_status = [
    "what are you doing", "what are you doing?", "whatcha doing",
    "whatcha doing?", "what's up?", "what you up to?", "what r u doing",
    "what r u up to", "how's it going?", "how are things?", "how’s life?",
    "what's going on?", "yo, busy?", "you there?", "you online?",
    "you working?", "are you doing anything?", "what’s happening?",
    "tell me what you're doing", "are you active?", "u active?",
    "status update", "give me your status", "current task?",
    "what are you doing right now?", "doing something?", "are you alive?",
    "report your activity", "bot, status?", "bot status?"
]

farewell = [
    "bye", "bye!", "goodbye", "goodbye!", "see you later", "see ya",
    "talk to you later", "ttyl", "peace out", "g2g", "gtg", "im out",
    "leaving now", "gotta go", "see ya later", "later!", "farewell",
    "catch you later", "until next time", "bye for now", "ok bye",
    "have a good one", "take care", "adios", "ciao", "bye-bye",
    "i'll see you soon", "see u", "okay later", "i’m off", "im gone",
    "talk soon", "logging off", "signing off", "off for now", "chat later",
    "disconnecting", "closing chat", "exit", "quitting now"
]

greeting = [
    "how are you", "how are you?", "how are you doing", "how are you doing?",
    "how's it going", "how’s it going?", "what’s up?", "what's good?",
    "how do you do?", "everything okay?", "how’s everything?", "how you been?",
    "what’s new?", "what’s going on?", "how are things?", "how’s life?",
    "are you okay?", "you doing well?", "you good?", "you fine?",
    "what’s up with you?", "how’s stuff?", "how’s today?", "how u doing?",
    "how are you today?", "how you feeling?", "how’s your day?",
    "how’s your night?", "you all right?", "how r u", "you okay?",
    "what you up to?", "doing okay?", "feeling good?", "everything all right?",
    "howdy", "hey, how are you?", "what’s up my bot?", "hi there, how are ya?"
]

say_hello = [
    "hello", "hello!", "hi", "hi!", "hey", "hey!", "yo", "hey there",
    "hi there", "hiya", "what's up", "good morning", "good afternoon",
    "good evening", "greetings", "sup", "howdy", "hi bot", "hello bot",
    "bot, hello", "heya", "hey hey", "yo yo", "yo!", "hello chatbot",
    "hello ai", "hi again", "hello again", "i’m back", "anyone there?",
    "bot are you there?", "bot hello", "hey assistant", "hi assistant",
    "hello friend", "hello robot", "yo assistant", "sup bot", "g’day",
    "bonjour", "hola"
]

state_name = [
    "your name", "your name?", "what's your name", "what's your name?",
    "do you have a name?", "what should I call you?", "who are you?",
    "tell me your name", "may i know your name?", "what's your id?",
    "bot, what's your name?", "do bots have names?", "what's your title?",
    "how do i call you?", "what name do you go by?", "you got a name?",
    "i want to know your name", "give me your name", "your identity?",
    "who am I talking to?", "name?", "your bot name?", "assistant name?",
    "is your name AI?", "what do people call you?", "what's your alias?",
    "nickname?", "label yourself", "do you have a title?", "who is this?"
]

intro_list = [
    "who are you?", "what's your name?", "may i know who i'm chatting with?",
    "tell me about yourself.", "are you a robot?", "what kind of bot are you?",
    "are you human?", "describe yourself", "who am i talking to?",
    "who is this?", "who are you talking to me?", "identify yourself",
    "what are you?", "can you explain what you are?", "what are you made of?",
    "what do you do?", "what is your purpose?", "introduce yourself",
    "what kind of assistant are you?", "are you AI?", "are you sentient?",
    "do you think like a human?", "are you alive?", "what is your job?",
    "do you understand me?", "how do you work?", "what’s your deal?",
    "what are you here for?", "are you a chatbot?", "what are you built for?",
    "what are your functions?", "what do you mean by chatbot?",
    "are you like siri?", "do you have feelings?", "do you know yourself?",
    "bot, explain yourself", "say something about yourself",
    "i want to know about you", "what's your role?"
]

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

def get_time_stamp() -> str:
    return datetime.now().strftime("[%H:%M:%S]")

def who_are_you() -> str: return "I am an AI Assistant Chat Bot, you could call me Sam."