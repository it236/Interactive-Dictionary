# Importing Libraries
import json
from difflib import get_close_matches

# Loading Data dictionary
data = json.load(open("data.json"))

# Primary Function
def ifalltrue(w):
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.lower() in data:
        return data[w.lower()]
    elif w.upper() in data:
        return data[w.upper()]
    else:
        return translate(w)

# Secondary Function
def translate(w):
    if len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y or N: " % get_close_matches(w, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            newi = input("So what did you mean? Please retype your word: ")
            return ifalltrue(newi)
        else:
            return "We did not understand your entry."
    else:
        return "This word doesn't exist. Please double check it."

word = input("Enter word: ")

output = ifalltrue(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
