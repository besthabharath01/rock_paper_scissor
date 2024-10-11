import random as r
rock = """
    _____
   /      )
  |       |
   \_____/
"""
paper = """
    _______
   |       |
   |       |
   |_______|
"""
scissors = """
     .--.       .--..
    /    \     /     |
   |      |   |      |
    \    /     \    /
     '--'       '--'        
      \           /
        \        /
          \     /
            \  /
             ()
            
"""
images=[rock,paper,scissors]
x='y'
user_score=0
computer_score=0
while x.lower()=='y':
    user_choice=int(input("enter choice:0 for rock (or) 1 for paper (or) 2 for scissoir:"))
    comp_choice=r.randint(0,2)
    # print("user's choice:",user_choice)
    # print("computer choice:",comp_choice)
    if user_choice>2 and user_choice<0:
        print("enter valid number")
    else:
        print("user choice:")
        print(images[user_choice])
        print("computer choice is:")
        print(images[comp_choice])
        if user_choice==comp_choice:
            print("draw")
        elif user_choice==0 and comp_choice==2:
            print("you won")
            user_score+=1
        elif user_choice==2 and comp_choice==0:
            print("computer won")
            computer_score+=1
        elif user_choice>comp_choice:
            print("you won")
            user_score+=1
        elif comp_choice>user_choice:
            print("computer won")
            computer_score+=1
    x=input("enter (y/n) to play another game:")
print("userscore:",user_score)
print("computerscore:",computer_score)