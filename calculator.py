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
    x = int(input("Enter the value you want to be checked for evenity or oddity (integers only obviously duh) "))
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
def Rand():
    L=int(input("Let's Play! Make your decision! Type in 1 and see the result! "))
    if L == 1:
        X= random.randint(0,1)
        if X==1:
            print("You Got Heads!")
        else:
            print("You got Tails!")
    else:
        print("You did not press 1, Sorry, Restart the calculator because i dont know how to loop back:P")
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
first,last= name.split(" ")[0]
print(f"By ZiadFazbear, Calucator Ver 0.4 (Loop Update), Hello {name}!")
print("The currently available abilities to this calcutalor are squaring numbers and extracting the roots of quad equations, checking for evenity or oddity, heads or tails and closing the calculator!")
breaker = int
breaker = 0
while breaker == 0:
    print("Please choose your needed option  ")
    choice= int(input("1) Squaring any number, 2) Extracting roots of a Quadratic equation 3) Checking for even or odd nums 4) Heads or Tails 5) Close the Calculator"))
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