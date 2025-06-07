score = int(input("Enter your score: "))
grade = ''
# This code determines the grade based on the user's score.

if(score < 0 or score > 100):
    print("Invalid score. Please enter a score between 0 and 100.")
    exit()

if score >= 90:
    print(f"Your grade is: A")
elif score >= 80:

    print(f"Your grade is: B")
elif score >= 70:

    print(f"Your grade is: C")
elif score >= 60:
  print(f"Your grade is: D")
else :
    print(f"Your grade is: F")




# Alternative way using match case


score_level_cal = score // 10 

# score_level = 10 if score_level_cal > 10 else score_level_cal

score_level = min(score_level_cal, 10)  # Ensure score_level does not exceed 10

match score_level:
    case 10 | 9 :
        grade = 'A'
    case 8:
        grade = 'B'
    case 7:
        grade = 'C'
    case 6:
        grade = 'D'
    case _:
        grade = 'F'
print(f"Your grade is: {grade} #using match case")



