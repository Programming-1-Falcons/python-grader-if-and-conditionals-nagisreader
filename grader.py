running = True
print("Rubric: ")
print("0 - 50% = F")
print("51% - 60% = D")
print("61% - 75% = C")
print("76% - 88% = B")
print("89% - 100% = A")
while running:
    total_points = float(input("Enter total possible points: "))
    student_points = float(input("Enter points achieved: "))
    score = round(student_points / total_points, 2)
    if (score <= 0.5):
        print("Score - F")
    elif (score >= 0.51 and score <= 0.6):
        print("Score - D")
    elif (score >= 0.61 and score <= 0.75):
        print("Score - C")
    elif (score >= 0.76 and score <= 0.88):
        print("Score - B")
    else:
        print("Score - A")
    user_continue = input("Continue? (y/n) ")
    if user_continue == "n":
        break
    elif user_continue == "y":
        continue
    else:
        print("that's not an option")