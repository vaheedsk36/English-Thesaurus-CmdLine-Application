import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no.\n" % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "We cannot find the word in dictionary"
        else:
            return "Please check the input and try again"

    else:
        return "Please check the input and try again"
word = input("Enter Word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)