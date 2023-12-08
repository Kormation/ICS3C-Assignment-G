# Programmer : Alexander Walker
# Description : This program asks for a percent grade, if it's invalid the user will be given an error message
#and will e prompted to try again

grade = int(input("Please enter a grade % : "))

while (grade < 0) or (grade > 100):
    print("Invalid grade, must be between 0, 100")
    grade = int(input("Please enter a grade % : "))
    
if (grade >= 80):
    print("Grade : A")
    
elif (grade >= 70):
    print("Grade : B")
    
elif (grade >= 60):
    print("Grade : C")
    
elif (grade >= 50):
    print("Grade : D")
    
else:
    print("Grade : F")


    
