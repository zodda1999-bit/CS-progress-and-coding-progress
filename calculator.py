import random
def Sqring():
    x=int(input("Type in the Value of X  "))
    print(f"{x} squared is {square(x)}")
def square(n):
    return n**2
# try to make a functional quadratic forumla calculator with values and make sure it works with no errors
# gives out full equations and is rounded to the nearest tenth digit
def Quad():
    print("Please input values for a, b and c in the formula aX²+bX+c")
    a=float(input("Please input the value of a   "))
    b=float(input(("Please input the value of b  ")))
    c= float(input(("Please input the value of c  ")))
    Root1 = (((0-b)+((b**2)-(4*a*c))**0.5)/(2*a))
    Root2= (((0-b)-((b**2)-(4*a*c))**0.5)/(2*a))
    D=(b**2)-(4*a*c)
    if D<0:  #Try to make complex answers considered ("Not Real")
        print("Your Equation has no real roots!")
        
    print(f"The two values of your quadratic equation are {Root1} and {Root2}")
#attempting a check on even and odd numbers

def check():
    o=0
    while o== 0:
        try:
            x=int(input("Enter the number you want to check for evenity or oddity (integers only duh)  "))
        except ValueError:
            print("This isn't an integer!")
        else:
            if x % 2==0:
                print(f"{x} is an even number!")
            
            
            else:
                print(f"{x} is an odd number!")
        p= 0
        while p==0:
            try:
                z=int(input("Would you like to try again? Press 1 if yes, press 2 to go back to interface menu!"))
            except ValueError:
                print("That isn't a choice!")
            else:
                if z ==1:
                    p=p+1
                elif z ==2:
                    p=p+1
                    o=o+1
                else:
                    print("That is not a choice!")

    
    
        
        
           
            
    
    

def Rand():
    while True:
        L=int(input("Let's Play! Make your decision! Type in 1 for Heads and 2 For Tails! ")) # 1 is heads and 2 is tails!!!
        x=random.randint(1,2)
        if x ==1 and L ==1:
            print("The answer is Heads! Correct!")
        elif x == 1 and L == 2:
            print("The answer is Heads! Not Tails!")
        elif x == 2 and L==1:
            print("The answer is Tails! Not Heads!")
        elif x ==2 and L==2:
            print("The answer is Tails! Correct!")
        else:
            print("You either didn't choose either or chose another number!")
        y=int(input(f"Wanna play again, {first}? Type any number except 2 if yes or Type 2 to return to main interface"))
        if y == 2:
            break
    

#Go Here and think about a way to add more mathematical operations and ways to calculate

#Now the interface (Will edit this later)
Brkr= int
Brkr = 0
while Brkr == 0:
    name=input("Please enter your name!  ").strip().title()
    if name != "":
        Brkr = Brkr+1
    else:
        print("The name is blank!")
first= name.split(" ")[0]
print("================================================================================")
print(f"By ZiadFazbear, Calucator Ver 0.5 (Fine Tuning Update (1) ), Hello {name}!")
print("================================================================================")
print("The currently available abilities to this calcutalor are squaring numbers and extracting the roots of quad equations, checking for evenity or oddity, heads or tails and closing the calculator!")
breaker = int
breaker = 0
while breaker == 0:
    print("Please choose your preferred option!   ")
    choice= int(input("1) Squaring any number, 2) Extracting roots of a Quadratic equation 3) Checking for even or odd nums 4) Heads or Tails 5) Close the Calculator     "))
    if choice == 1:
        Sqring()
    elif choice ==2:
        Quad()
    elif choice == 3:
        check()
    elif choice == 4:
        Rand()
    elif choice == 5:
        print(f"Goodbye, {first}!")
        breaker = breaker+1
    else:
        print("That was not a choice!")


#To Do: make a function that loops the calculator back to the menu after an operation is over :P (Done on 7/25/2026)
# Update: Added a loop function, let's go!
# Update 2: Added better fine tuning to Heads or Tails. 