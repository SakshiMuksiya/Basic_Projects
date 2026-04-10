print("Welcome to my computer quiz!!!")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print("Let's play: ")

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct !")
    score +=1
else:
    print("Not correct !")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct !")
    score +=1
else:
    print("Not correct !")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct !")
    score +=1
else:
    print("Not correct !")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("Correct !")
    score +=1
else:
    print("Not correct !")

print("You got "+ str(score) +" questions correct !")
print("You got "+ str((score/4)*100) +" %")