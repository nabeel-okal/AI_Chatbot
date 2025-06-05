import pandas as pd
import random

def get_a_joke():
    jokes = pd.read_csv('funjokes.csv')
    print(jokes["Joke"])
    jokes_list = jokes["Joke"].tolist()
    return jokes_list


for j in get_a_joke():
    print(j)