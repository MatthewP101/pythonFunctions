def intGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "Failed class Bozo"

listOfScores = [100, 90, 80, 70, 60, 50]

for score in listOfScores:
    print("This score is: " + str(score))
    print(intGrade(score))


#can sort an integer into a gorup and return specific values based on the group it falls into.