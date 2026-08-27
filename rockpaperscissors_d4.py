import random
users_choice= int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))

rock = '''

       ,--.--._
------" _,   __)
        / _/____)
          /(____)
------      (__)
       `-----"
'''
paper = '''

           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'     
'''
scissors ='''
   ____
  / __ \
 ( (__) |___ ___
    _______,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
    ___/
'''
if users_choice == 0:
    print(f"Your choice: {rock}")
elif users_choice == 1:
    print(f"Your choice: {paper}")
elif users_choice == 2:
    print(f"Your choice: {scissors}")
else:
    print("You typed an invalid number, you lose!")

computer_choise = random.randint(0, 2)
if computer_choise == 0:
     print(f"Computer's choice: {rock}")
elif computer_choise == 1:
        print(f"Computer's choice: {paper}")
elif computer_choise == 2:
        print(f"Computer's choice: {scissors}")

if computer_choise == users_choice:
    print("It's a draw")
elif users_choice == "0" and computer_choise == 2:
    print("You win!")
elif users_choice == "1" and computer_choise == 0:
    print("You win!")
elif users_choice == "2" and computer_choise == 1:
    print("You win!")
else:
    print("You lose!")
