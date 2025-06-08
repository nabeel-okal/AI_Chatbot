import pandas as pd
import random
import re
from datetime import datetime

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

intro = [
    
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