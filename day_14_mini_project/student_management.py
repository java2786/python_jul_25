""" 
app start
-> enter your name: Ramesh

-> enter subject name: Math
-> enter subject score: 67
press 1 to enter more subject and score
press 2 to exit

-> enter subject name: English
-> enter subject score: 87
press 1 to enter more subject and score
press 2 to exit


Hi Ramesh, your total marks are total marks.

"""

name = input("Enter your name: ")

scores = {} # Dictionary
while True:
    sub = input("Enter subject: ")
    marks = int(input("Enter marks: "))
    
    scores[sub] = marks 
    print(scores,"\n")
    
    choice = input("press 0 to exit")
    if(choice=='0'):
        break

print(scores.items())