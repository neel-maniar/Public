import random
m=0
answer = ""
print("Welcome to Mastermind! In this game, the computer randomly generates 4 numbers. You guess the sequence and if a number is in the right place, it will give you a '*'. If a number is in the answer, but in the wrong place, it will give you a 'x'")
while m == 0:
    easy = input("Would you like all 4 numbers to be different or allow doubles? Enter doubles or singles. ")
    if easy == "singles":
        while len(answer)<4:
            ran = str(random.randint(0,9))
            if ran not in answer:
                answer += ran
        m=1
    elif easy == "doubles":
        for x in range(4):
            answer += str(random.randint(0,9))
        m=1
    else:
        print ("You didn't enter 'singles' or 'doubles': try again.")
user_input = ""
while user_input != answer:
    user_input = str(input("Guess the number: "))
    red = 0
    white = 0
    for x in range(4):
        if user_input[x] == answer[x]:
            red += 1
        elif user_input[x] in answer and user_input.count(user_input[x])==1:
            white += 1
        elif user_input[x] in answer and user_input.count(user_input[x])>1 and user_input[x] not in user_input[0:x]:
            white += 1
    print ("*"*red+"x"*white)    
print("Congratulations!")



