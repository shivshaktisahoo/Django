# ROCK-PAPER-SCISSOR  GAME
import random
print("\n!!!!!!!!! Welcome  to   ROCK, PAPER, SCISSOR   Game !!!!!!!!!!")
list1=['rock','paper','scissor'] 
def player_input():
    while(True):                                    # while loop due to particular input by user only, else ask again & again 
        p_choice=str(input("\nEnter your choice:\n for rock:\ttype r\n for paper:\ttype p\n for scissor:   type s\n for exit the game: type 0\n")).lower()
        if(p_choice=='r'):
            p_choice=list1[0]                                       
            return p_choice
        elif(p_choice=='p'):
            p_choice=list1[1]
            return p_choice
        elif(p_choice=='s'):
            p_choice=list1[2]
            return p_choice
        elif(p_choice=='0'):                                        # for exit the game
             print('Thanks for Playing !!!!')
             break
        else:
            print("\nPLEASE enter Correct keyword")
            
def check(p_input,comp_choice):                                                                # for user_choice = rock, 
    print(f'your choice is {p_input}\ncomputer choice is {comp_choice}')    # there is 3 possibilites with computer choice
    if(p_input==comp_choice):                                               # similary for others
       print('\n**************** \"TIE" ***************')
    else:
        if(p_input=='rock'):
            if(comp_choice=='paper'):
                print('\n**************** \"Computer WIN\" ***************')
            else:
                print('\n\"**************** \"You WIN\" ***************\"')
        if(p_input=='paper'):
            if(comp_choice=='scissor'):
                print('\n**************** \"Computer WIN\" ***************')
            else:
                print('\n\"**************** \"You WIN\" ***************\"')
        if(p_input=='scissor'):
            if(comp_choice=='rock'):
                print('\n**************** \"Computer WIN\" ***************')
            else:
                print('\n**************** \"You WIN\" ***************')

while(True):
    p_input=player_input()                            # calling player input function for user choice      
    comp_choice=random.choice(list1)                  # computer is choosing random values from list1
    if(p_input==None):                                # for Exit purpose
        break
    check(p_input,comp_choice)                        # calling check fun. for user and computer choice