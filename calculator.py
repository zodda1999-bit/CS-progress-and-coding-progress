import random
def Sqring():
    o=0
    while o==0:
     try:
      x=float(input("Type in the Value of X  "))
     except (TypeError,ValueError) :
        print("This isn't a number!")
     else:
      print(f"{x} squared is {square(x)}")
      p=0
     while p==0:

      try:
       y=int(input("Would you like to try another equation? Type 1 if yes or type 2 to return back to the main interface  "))
      except (TypeError, ValueError) as error:
         print("This isn't a choice!")
      else:
            if y==2:
             p=1
             o=1
            elif y==1:
                p=1
            else:
                print("This isn't a choice!")
         
         
         

def square(n):
    return n**2
# try to make a functional quadratic forumla calculator with values and make sure it works with no errors
# gives out full equations and is rounded to the nearest tenth digit
def Quad():
  o=0
  while o==0:
    print("Please input values for a, b and c in the formula aX²+bX+c")
    try:
        a=float(input("Please input the value of a   "))
        b=float(input("Please input the value of b   "))
        c=float(input("Please input the value of c   "))
        Root1 = float((((0-b)+((b**2)-(4*a*c))**0.5)/(2*a)))
        Root2 = float((((0-b)-((b**2)-(4*a*c))**0.5)/(2*a)))
    except (TypeError, ValueError) as error:
       print("This answer is complex! No Real Roots!")
    else:
        print(f"The roots of this equation are {Root1:.1f} and {Root2:.1f} .")
    p= 0
    while p ==0:
        try:
         y=int(input("Would you like to try another equation? Type 1 if yes or type 2 to return back to the main interface  "))
        except (ValueError,TypeError) as error:
            print("This isn't a choice!")
        else:
            if y==2:
             p=1
             o=1
            elif y ==1:
                p=1
            else:
                print("This isn't a choice!") #try and except really do save me from human errors and bugs! what a nice feature!
    

        


     
    
    
    
       
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
                print("This isn't a choice!")
            else:
                if z ==1:
                    p=p+1
                elif z ==2:
                    p=p+1
                    o=o+1
                else:
                    print("This isn't a choice!")

    
    
        
        
           
            
    
    

def Rand():
    o=0
    while o==0:
        try:
            L=int(input("Let's Play! Make your decision! Type in 1 for Heads and 2 For Tails! ")) # 1 is heads and 2 is tails!!!
        except ValueError:
            print("That is not a choice!")
        else:
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
        p=0
        while p == 0:
         y=int(input(f"Wanna play again, {first}? Type 1 if yes or Type 2 to return to main interface   "))
         if y == 2:
            o=1
            p=1
         elif y ==1:
            p=1
         else:
            print("This isn't a choice!")

                
        

    

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
        print("This isn't a choice!")


#To Do: make a function that loops the calculator back to the menu after an operation is over :P (Done on 7/25/2026)
# Update: Added a loop function, let's go!
# Update 2: Added better fine tuning to Heads or Tails. 
# Update 3: Fine tuned and error-proofed the rest of the functions! (Done on 7/26/2026) :3