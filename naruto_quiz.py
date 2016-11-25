print("\nHere is a quiz to determine which Naruto character you are")

    
sakura_points = 0
sakura_points = int(sakura_points)

naruto_points = 0
naruto_points = int(naruto_points)

kakashi_points = 0
kakashi_points = int(kakashi_points)

shikamaru_points = 0
shikamaru_points = int(shikamaru_points)

sasuke_points = 0
sasuke_points = int(sasuke_points)

"-----------------------------------------------------------------"

def qstn1():
    
    print \
        """1) How do you manage your anger?
              1) Physically exert your rage
              2) Talk it out/vent
              3) Bottle it up inside
              4) Confront who/what is angering you
              5) Analyze it and think it out """

    q1 = raw_input("\n Answer: ")

    if q1 == "1":
        global sakura_points
        sakura_points += 1
    elif q1 == "2":
        global naruto_points
        naruto_points += 1
    elif q1 == "3":
        global sasuke_points
        sasuke_points += 1
    elif q1 == "4":
        global shikamaru_points
        shikamaru_points += 1
    elif q1 == "5":
        global kakashi_points
        kakashi_points += 1
    else:
        print("\n Please choose answer choices 1-5")
        qstn1()
qstn1()

"----------------------------------------------------------------------------"
def qstn2():

    print \
        """2) How would you approach an opponent in a fight?
              1)Study their movements, strike once you see their weakness
              2)Come at them like an uncontrollable barrage of force
              3)Move quickly, like a blur
              4)Allow them to exhaust themselves
              5)Work with a partner to defeat the adversary """
        
    q2 = raw_input("\n Answer: ")

    if q2 == "1":
        global shikamaru_points
        shikamaru_points += 1
    elif q2 == "2":
        global naruto_points
        naruto_points += 1
    elif q2 == "3":
        global sasuke_points
        sasuke_points += 1
    elif q2 == "4":
        global kakashi_points
        kakashi_points += 1
    elif q2 == "5":
        global sakura_points
        sakura_points += 1
    else:
        print("\n Please choose answer choices 1-5")
        qstn2()

qstn2()

"---------------------------------------------------------------------------"
def qstn3():

    print \
        """3) What animal do you identify with most?
              1)Rabbit
              2)Crow
              3)Tiger
              4)Hawk
              5)Snake """
    q3 = raw_input("\n Answer: ")

    if q3 == "1":
        global sakura_points
        sakura_points += 1
    elif q3 == "2":
        global shikamaru_points
        shikamaru_points += 1
    elif q3 == "3":
        global naruto_points
        naruto_points += 1
    elif q3 == "4":
        global kakashi_points
        kakashi_points += 1
    elif q3 == "5":
        global sasuke_points
        sasuke_points += 1
    else:
        print("\n Please choose answer choices 1-5")
        qstn3()

qstn3()

"---------------------------------------------------------------------------"
def qstn4():
    print \
        """4) What element describes you best?
              1)Earth
              2)Wind
              3)Fire
              4)Water
              5)Lightening"""
    q4 = raw_input("\n Answer: ")

    if q4 == "1":
        global naruto_points
        naruto_points += 1
    elif q4 == "2":
        global shikamaru_points
        shikamaru_points += 1
    elif q4 == "3":
        global sasuke_points
        sasuke_points += 1
    elif q4 == "4":
        global sakura_points
        sakura_points += 1
    elif q4 == "5":
        global kakashi_points
        kakashi_points += 1
    else:
        print("\n Please choose answer choices 1-5")
        qstn4()

qstn4()
    

"-----------------------------------------------------------------"

def qstn5():
    print \
        """5) Which pair of words describes you best?
              1)Serious and hardworking
              2)Introverted and kind
              3)Independent and blunt
              4)Outgoing and energetic
              5)Smart and lazy"""
    q5 = raw_input("\n Answer: ")

    
    if q5 == "1":
        global sasuke_points
        sasuke_points += 1
    elif q5 == "2":
        global sakura_points
        sakura_points += 1
    elif q5 == "3":
        global kakashi_points
        kakashi_points += 1
    elif q5 == "4":
        global naruto_points
        naruto_points += 1
    elif q5 == "5":
        global shikamaru_points
        shikamaru_points += 1
    else:
        print("\n Please choose answer choices 1-5")
        qstn5()
        
qstn5()

"-------------------------------------------------------------------"

def qstn6():
    print \
        """6) Do you (or did you) like going to school?
                1)Fuck no. I am too energetic to sit that long!
                2)It's okay, but I like learning practical things
                3)Yes! I love learning
                4)It's okay, but it's hard to interact with so many people
                5)No, I prefer to skip class"""
    
    q6 = raw_input("\n Answer: ")

    if q6 == "1":
        global naruto_points
        naruto_points += 3
    elif q6 == "2":
        global kakashi_points
        kakashi_points += 3
    elif q6 == "3":
        global sakura_points
        sakura_points += 3
    elif q6 == "4":
        global sasuke_points
        sasuke_points += 3
    elif q6 == "5":
        global shikamaru_points
        shikamaru_points += 3
    else:
        print("\n Please choose answer choices 1-5")
        qstn6()
"----------------------------------------------------------------------"

if sakura_points >= 3:
    print("You are Sakura!")
    exit(0)
elif sasuke_points >= 3:
    print("You are Sasuke!")
    exit(0)
elif kakashi_points >= 3:
    print("You are Kakashi!")
    exit(0)
elif naruto_points >= 3:
    print("You are Naruto!")
    exit(0)
elif shikamaru_points >= 3:
    print("You are Shikamaru!")
    exit(0)
else:                           # If none of the above characters are selected because they didnt get enough points
	print sakura_points
                              # Prints out the number of points of each character
        print sasuke_points
	print kakashi_points
	print naruto_points
	print shikamaru_points
	qstn6()

if sakura_points >= 3:
    print("You are Sakura!")
    
elif sasuke_points >= 3:
    print("You are Sasuke!")
    
elif kakashi_points >= 3:
    print("You are Kakashi!")
    
elif naruto_points >= 3:
    print("You are Naruto!")
    
elif shikamaru_points >= 3:
    print("You are Shikamaru!")
    
else:
    print("You are no one!")


