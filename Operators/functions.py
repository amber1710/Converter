#Exercise 1:
# grades= [20,10,90,85,40,75,65,64,12,74,71,98,50]
#Task:
#Filter the grades to only display everyone above ( and including ) 70%
grades = [20,10,90,85,40,75,65,64,12,74,71,98,50]
def all_above ():
    if grades > 70:
        return True
    else:
        return False
    print(False)
marks=filter(all_above(),grades)
for grades in marks:
    print(marks )

# Exercise 2 :
#dog_ages = [12,8,4,1,2,6,4,4,5]
#Task:
#Convert the ages into "dog years" (x7)

human_years = input('How old are you? ')
dog_years = human_years * 7
# use the variable name dog_years so that the print statements below will print out the correct values.

print("You are", human_years, "in human years")
print("You are", dog_years, "in dog years")


#Exercise 3:
#transactions = [51.0 , 49.99,80.99,67.99,120.52,23.49]
#Task:
#Conver the transactions to a single total

transactions = [51.0 , 49.99,80.99,67.99,120.52,23.49]
def trans_total():

