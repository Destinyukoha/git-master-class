name = input("Enter your name: ")

print("welcom "+ name +" to this game")

answer = input("you are on a gravel road and it has come to a dead end. you can turn left or right. would you like to go right or left? ").lower()

if answer == "left":
    answer = input("you have to come to a river. you either walk around it or swim across the river. if you choose to walk around it, type walk and if you choose to swim, type swin. what would you like to do?").lower()
    if answer == "walk":
        print("you walked a few miles, ran out of water, and lost the game.")
    elif answer == "swim":
        print("you swam across the river and found a bag of diamonds. you win the game!")
    else:
        print("This is not a valid answer. The game has ended")

elif answer == "right":
    answer = input("The sun has set and you have reached a forest.you can choose to pick some barries in this forest for food,start a warm fire and go to sleep next ot it, or continue walking food or sleep. please enter either food, fire or walk for each of the choices respectively. you can only choose one: ").lower()
    if answer == "food":
        answer = input("you have been walking and have not eaten in a few days now, but you have berries with you. however, you across a random man that shouts that the berries are poisonious. you can choose to either eat the berriers or throw them away.to eat, and to ditch the barriers,type throw: ").lower()
        if answer == "eat":
            print("you ate th berries and it turns out that they were not poisonious.you won the game!")
        elif answer == "throw":
            print("you throw the berriers away but they were never poisonious. you lose.")
        else:
            print("this is invalid answer and the game has ended.")
    elif answer == "fire":
        print("you choose to start a fire and fall asleep, but the fire spread around and you lost the game.")
    elif answer == "walk":
        print("you walked to the end of the forest and found a home. you win!")
    else:
        print("This is an invalid answer and the game has ended.")   
else:
    print("This answer is invalid. you need to enter either 'left' or 'right'.please restart the game to try")