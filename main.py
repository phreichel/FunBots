def welcome():
    print("Welcome to the chatter bot.")
    print("Enter a sentence and expect a response.")
    pass

def input_line():
    text = input(">")
    print("You said: " + text)
    return text

def analyse(text):
    pass

welcome()
text = input_line()
analyse(text)