user_input = int(input("TAKE A SHORT TEST TO FIND OUT IF YOUR PERSONALITY TYPE MATCHES WITH BEING A CODER! PRESS 0 TO CONTINUE: "))


n = 0
choices = []
total = 0
question_prompts = [
        "PLEASE ENTER A NUMBER 1-5, 1 BEING LESS LIKELY AND 5 BEING MOST LIKELY!\n    I can solve problems without clear direction: ",
        "    I like to build and create things: ",
        "    I enjoy collaborating as part of a team: ",
        "    Listening and communicating with others is a strength of mine: ",
        "    I like to figure things out: ",
        "    When I interact with technology I like to think about improving the user experience: ",
        "    I am motivated to help others: ",
        "    I enjoy keeping track of details in all that I do: ",
        "    I can quickly see an entire situation, with all its details: ",
        "    I enjoy bringing a team together to solve difficult challenges: ",
        "    If presented with a problem, I can provide many solutions: ",
        "    I can handle many ideas at once: "
]
for q in question_prompts:
    # n = 0
    # choices = []
    choice = input(question_prompts[n])
    choices.append(int(choice))
    n += 1
for numbers in choices:
    total += numbers
if total >=0:
    print("\nYou scored a total of " + str(total) + ".")
if total >= 35:
    print("\nYou're A Good Fit To Become a Coder!\n")
elif total <= 35:
    print("\nPlease Try Something Else!\n")
# print(total)