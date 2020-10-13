import random
randomnumber=random.randint(1, 10)

guess=3
while guess>0:
    guess=int(input("Please enter a number"))
    if randomnumber==guess:
      print("You win")
      break

    else:
     print("You lose")
     guess==guess-1




