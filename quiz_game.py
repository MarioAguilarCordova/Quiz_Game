print("Welcome to my Computer Quiz!")


playing = input("Do you want to play? ")

score = 0

if playing.lower() != "yes":
    quit()



print("Okay! Let's play : ) ")
print("Answer 3 or more questions correctly to win!")


answer = input("Question 1: What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print(answer)
    print('That is incorrect :( ')
    reveal = input("Would you like to know the answer? ")
    if reveal.lower() == "yes":
        print('The answer is: central processing unit')


answer = input("Question 2: What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('That is incorrect :( ')
    reveal = input("Would you like to know the answer? ")
    if reveal.lower() == "yes":
        print('The answer is: graphics processing unit')

answer = input("Question 3: What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('That is incorrect :( ')
    reveal = input("Would you like to know the answer? ")
    if reveal.lower() == "yes":
        print('The answer is: random access memory')

answer = input("Question 4: What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print('That is incorrect :( ')
    reveal = input("Would you like to know the answer? ")
    if reveal.lower() == "yes":
        print('The answer is: power supply unit')

if score > 1:
    print("You got " + str(score) + " questions correct!")
else:
    print("You got " + str(score) + " question correct!")

if score >= 3:
    print("You Win! :)")
else:
    print("You Lose :(")