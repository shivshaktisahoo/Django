def guess_number():
    import random
    print('\n🎮🎮🎮🎮🎮🎮 𝐇 𝐞 𝐥 𝐥 𝐨 !!!   𝐖 𝐞 𝐥 𝐜 𝐨 𝐦 𝐞   𝐭𝐨   𝓝𝓤𝓜𝓑𝓔𝓡  𝐆 𝐀 𝐌 𝐄 🎮🎮🎮🎮🎮🎮')
    while True:
        try:                        # if user gives wrong input, Try and exception is done
            actual_num = int(input("Give a number between 0-100 : "))
            break  
        except:
            print("Enter number only")
            continue 

        # actual_num = 50
        # comp_choice = 30 
    x = lambda r1,r2:random.randint(r1,r2) 


    comp_choice = random.randint(0,101)
    loop_cond = True               # condition for while loop
    while loop_cond:
        if (comp_choice < actual_num):  # 30<50:True
            print("Too Low")
            comp_choice = x(comp_choice,actual_num+1)
            continue
        if (comp_choice > actual_num):  # 30<100:True
            print("Too Low")
            num = comp_choice
        if 
        comp_choice = x(num,actual_num+1)

        
        else:
         print("😆😆😆😆😆😆😆😆😆😆 𝙐 𝙂𝙪𝙚𝙨𝙨𝙚𝙙 𝘾𝙤𝙧𝙧𝙚𝙘𝙩𝙡𝙮 😆😆😆😆😆😆😆😆😆😆")
        loop_cond = False         # stoping condition

# guess_number()                # calling a function
import random
x = lambda r1,r2:random.randint(r1,r2+1)
comp_choice = x(30,100)
print(comp_choice)
