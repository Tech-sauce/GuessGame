import random
def play():
    n = random.randint(1,100)
    guess=int(input('Enter a number: '))
    compare= n-guess #used this to check -ivty. -89 will always be less than 10
    if compare < 0:
        compare=abs(compare) #i used this absolute function to get a positive number
    if guess == n:
        print('You are correct')
    elif (compare <=10):
        print ('You are close')
    else:
        print ('you are not close')
        again()
def again():
    print("You want to play again ?")
    ans=input("Type yes or no: ")
    if ans=='yes':
        play()
    elif ans=='no':
        print("Thank You!")
    else:
        print("please select a valid option")
        print("make sure you type the correct options provided above. AVOID SPACES!!!")
        again()




play()
again()

    


