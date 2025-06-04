import re

def calculate_nums(text) -> int:
    match = re.match(r'(\d+)\s*([+\-*/])\s*(\d+)', text)
    arg1 = int(match.group(1))
    op = match.group(2)
    arg2 = int(match.group(3))
    
    if op == '+':
        return arg1 + arg2
    elif op == '-':
        return arg1 - arg2
    elif op == '*':
        return arg1 * arg2
    elif op == '/':
        return arg1 / arg2
    else:
        return "I didn't understand. Could you provide a valid calculation prompt?"

print(calculate_nums("2 + num"))