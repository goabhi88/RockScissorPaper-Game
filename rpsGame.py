import random
m=["rock","scissor","paper"]
'''
    C               U            W
  rock           paper          paper
  rock           scissor        rock
  paper          scissor        scissor

'''
while True:
    ccount=0
    ucount=0
    uc=int(input('''
    Game Start....
    1 Yes|Play
    2 No|Exit
    '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
            1 Rock
            2 Scissor
            3 paper
            '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoise=random.choice(m)
            if Cchoise==uchoice:
                print("User Value ",uchoice)
                print("Computer Value ",Cchoise)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="rock" and Cchoise=="scissor") or (uchoice=="scissor"and Cchoise=="paper")or (uchoice=="paper" and Cchoise=="rock"):
                print("User Value ",uchoice)
                print("Computer Value ",Cchoise)
                print("You Win")
                ucount=ucount+2
               
            else:
                print("User Value ",uchoice)
                print("Computer Value ",Cchoise)
                print("Computer Win")
                ccount=ccount+2
        
        print("Final Result Of The Game is ----------- ")
        if ucount==ccount:
            print("Series Draw....")
            print("User Score - ",ucount)
            print("Computer Score - ",ccount)
        elif ucount>ccount:
            print("You Win The Game")
            print("User Score - ",ucount)
            print("Computer Score - ",ccount)
        else:
            print("Computer Win The Game")
            print("User Score - ",ucount)
            print("Computer Score - ",ccount)
               


            
            
        
    else:
        break