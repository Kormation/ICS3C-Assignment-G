# Programmer : Alexander Walker
# Description : This program asks the user for an multiplicand and the number of multiplication facts they want

#Set the first multiplication fact number to 1
fact_num = 1

#User puts in there multiplicand and multiplication fact number here.
integar = int(input("Enter an integar: "))
facts = int(input("How many facts do you want? "))

#While fact_num is less then or equal too facts the following will occur.
while (fact_num <= facts):
    total = integar * fact_num
    print(f"\n{integar} x {fact_num} = {total}")
    
    #Adds 1 until fact_num is > than facts
    fact_num += 1
    