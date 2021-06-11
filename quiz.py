'''quiz
for computer
    enthusiasts'''

print("welcome to my quizzo !!!")

playing = input("do you wanna play ? ") #add space after question mark to not make a mess

if playing != "yes":
    quit()

print("Okay ! lets play : ")
score = 0

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("correct !")
    score += 1
else:
    print("incorrect")

answer = input("In computer world, Trojan refer to? ")
if answer == "malware":
    print("correct !")
    score += 1
else:
    print("incorrect")

answer = input("In which year '@' sign was first chosen for its use in e-mail address? ")
if answer == "1972":
    print("correct !")
    score += 1
else:
    print("incorrect")

answer = input("The first computer was programmed using ")
if answer == "machine language":
    print("correct !")
    score += 1
else:
    print("incorrect")

answer = input("A web address is also called a  ")
if answer == "url":
    print("correct !")
    score += 1
else:
    print("incorrect")

print ("congratulations you aced the quiz with " + str(score) + " points ! ")

