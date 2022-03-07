print("""\nPlease answer each question truthfully with one of the following:\n
Strongly agree (A)
Agree (a)
Disagree (d)
Strongly disagree (D)\n""")

question_1 = input("1. I feel that I am a person of worth, at least on an equal plane with others. ")
question_2 = input("2. I feel that I have a number of good qualities. ")
question_3 = input("3. All in all, I am inclined to feel that I am a failure. ")
question_4 = input("4. I am able to do things as well as most other people. ")
question_5 = input("5. I feel I do not have much to be proud of. ")
question_6 = input("6. I take a positive attitude toward myself. ")
question_7 = input("7. On the whole, I am satisfied with myself. ")
question_8 = input("8. I wish I could have more respect for myself. ")
question_9 = input("9. I certainly feel useless at times. ")
question_10 = input("10. At times I think I am no good at all. ")

total = 0
positive_total = 0
negative_total = 0
new_total = 0

positive = [question_1 or question_2 or question_4 or question_6 or question_7]
negative = [question_3 or question_5 or question_8 or question_9 or question_10]

def positive_function():
    if positive == "A":
        positive_total = total + 3
    elif positive == "a":
        positive_total = total + 2 
    elif positive == "d":
        positive_total = total + 1
    elif positive == "D":
        positive_total = total + 0

    return positive_total

def negative_function():
    if negative == "A":
        negative_total = total + 0
    elif negative == "a":
        negative_total = total + 1
    elif negative == "d":
        negative_total = total + 2
    elif negative == "D":
        negative_total = total + 3
    
    return negative_total


new_total = positive_total + negative_total
print(f"Your total score is {new_total}")
