#print(input("Hello:")) #Task 1

#name=input()#Task 2
#surname=input()
#print("Hello",name,surname)

#print("What do you call a bear with no teeth. \nA gummy bear")#Task 3

#a=int(input())#Task 4
#b=int(input())
#sum=a+b
#print("the total is:",sum)

#a=int(input())#Task 5
#b=int(input())
#c=int(input())
#total=(a+b)*c
#print("the total is:",total)

#started=int(input("How many slices:"))#Task 6
#eaten=int(input("How many eaten:"))
#print("Slices left:",started-eaten)

#name=input("Your name:")#Task 7
#age=int(input("Your age"))
#print("Your name is "+ name +" and you will be ",age+1,"next year")

#price=int(input("Total price of the bill is :$"))#Task 8
#diners=int(input("How many diners:"))
#print("Each person must pay $",price/diners)

#num_days=int(input("Give numbers of day:"))#Task 9
#secs=num_days*(24*3600)
#mints=num_days*(24*60)
#hours=num_days*24
#print("In that number of days:",hours," hours,",mints," minutes,and ",secs," secounds.")

#pounds=2.204#Task 10
#mass=int(input("Weight in kilograms:"))
#print("Total price is :",pounds*mass)

#a=int(input("Give number over 100:"))#Task 11
#if a>=100:
#   print("Your number is:",a)
#else:
#   print("Number is less than 100!")
#b=int(input("Give number under 10:"))
#if b<=10:
#    print("Your number is:",b)
#else:
#    print("Number is more then 10!")
#c=a//b
#print("Smaller number goes into the larger number ",c,"times.")

#a=int(input("Number one:"))#Task 12
#b=int(input("Number two:"))
#if a>b:
#    print("The first number is ",a,"larger than the secound number ",b)
#elif a==b:
#    print("Given numbers are equal!")
#else:
#    print("The secound number is ",b,"larger than first number ",a)

#a=int(input("Give nuber undeer 20 :"))#Task 13
#if a>=20:
#    print("too high!")
#else:
#    print("Thank you!")

#a=int(input("Enter number : "))#Task 14
#if a>=10 and a<=20:
#    print("Thank you!")
#else:
#    print("Incorrect answer!")

#a=str(input("Your favourite colour is "))#Task 15
#if a=="red" or a=="RED" or a=="Red":
#    print("I like red too")
#else:
#    print("I don't like ",a,", I prefer red.")


#print("It is raining?")#Task 16
#a=str(input())
#b=str(input("Is it windy?\n"))
#if a=="YES" or a=="yes" or a=="Yes":
#    if b=="YES" or b=="yes" or b=="Yes":
#        print("It is too windy for an umbrella!")
#    else:
#        print("Take umbrella!")
#else:
#    print("Enjoy you day!")

#a=int(input("what is your age?\n"))#Task 17
#if a>=18:
#    print("You can vote!")
#elif a==17:
#   print("you can lear to drive!")
#elif a==16:
#    print("you can by lottery ticket!")
#else:
#    print("you can go Trick-or-Treating!")     

#a=int(input("Please enter number!\n"))#Task 18
#if a<10:
#    print("too low!")
#elif a>=10 and a<=20:
#    print("correct")
#else:
#    print("too high!")

#a=int(input("please enter 1,2 or 3\n"))#Task 19
#if a==1:
#    print("Thank you!")
#elif a==2:
#    print("Well done!")
#elif a==3:
#    print("Correct!")
#else:
#    print("Error message!")

#a=str(input("please enter your first name!\n"))#Task 20
#print(len(a))

#a=str(input("enter your name! "))#Task 21
#b=str(input("enter your surname!"))
#c=(a + " "+ b)
#print(c)
#print(len(c))

#a=str(input("please enter your name in lower case!\n"))#Task 22
#b=str(input("please enter your surname in lower case!\n"))
#c=(a+ " " +b)
#print(c.title())

#a=str(input("Please tipe nursery rhyme\n"))#Task23
#print(len(a))
#b=int(input())
#c=int(input())
#d=(a[b:c])
#print(d)

#a=str(input("Write any word:\n"))#|Task24
#print(a.upper())

#a=str(input("Enter your name:\n"))#Task25
#if len(a)<5:
#    print("Enter your name and surname together")
#    a=str(input().upper())
#    print(a)
#elif len(a)>=5:
#    print("Enter name")
#    a=str(input().lower())
#    print(a)





#a=float(input("Enter decemal number: ")) #Task 27
#b=a*2
#print(b)


#a=float(input("Enter decemal number: ")) #Task 28
#print(round(a,2))

#import math #Task 29
#a=int(input("Enter umber over 500: "))
#b=int(math.sqrt(a))
#print(b)

#import math #Task 30
#a=math.pi
#print(round(a,5))

#import math #Task 31
#a=int(input("Enter radius of a circle: "))
#b=math.pi
#c=b*a**2
#print("Area of circle is ",c)

#import math #Task 32
#a=int(input("Enter radius: "))
#b=int(input("Enter depth: "))
#c=math.pi
#d=b*c*a**2
#print("Total value: ", round(d,3))

#a=int(input("Enter first number: ")) #Task 33
#b=int(input("Enter secound number: "))
#c=a//b
#d=a%b
#print(a,"divided by ",b," is equal to ",c," with reminder ",d)

#a=int(input()) #Task 34
#if a==1:
#    b=int(input("Length of sides: "))
#    print(b*3)
#elif a==2:
#    c=int(input("Base and high: "))
#    d=int(input())
#    print(c*d/2)
#else:
#    print("Incorrect number!")


#a=str(input("Enter your name: ")) #Task 35
#for i in range (1,4):
#    print(a)


#a=str(input("Enter your name: ")) #Task 36
#b=int(input("Enter number: "))
#for i in range(b):
#    print(a)


#a=str(input("Enter name: ")) #Task 37
#for i in a:
#    print(i)


#a=str(input("Enter name: ")) #Task 38
#b=int(input("Enter number: "))
#for i in range(b):
#    for b in a:
#        print(b)


#a=int(input("Enter number between 1 and 12: ")) #Task 39
#for i in range(1,a):
#    b=a*i
#    print(a,"x",i,"=",b)

#a=int(input("Enter numbr below 50: ")) #Task 40
#for i in range(50,a-1,-1):
#    print(i)

#a=str(input("Enter name: ")) #Task 41
#b=int(input("Enter number: "))
#if b<=10:
#    for i in range(b):
#        print(a)        
#else:
#    print("Too high!")


#print("Enter five numbers!") #Task 42
#total=0
#a=int(input("enter number: "))
#f=int(input("if you want this included press 1\n"))
#if f==1:
#    total=total+a
#b=int(input("enter number: "))
#g=int(input("if you want this included press 1\n"))
#if g==1:
#    total=total+a
#c=int(input("enter number: "))
#h=int(input("if you want this included press 1\n"))
#if h==1:
#    total=total+a
#d=int(input("enter number: "))
#i=int(input("if you want this included press 1\n"))
#if i==1:
#    total=total+a
#e=int(input("enter number: "))
#j=int(input("if you want this included press 1\n"))
#if j==1:
#    total=total+a
#print(total)


#print("Which direction the user wants to count (up/down)") #Task 43
#a=input()
#if a=="up":
#    b=int(input("Enter top number: "))
#    for i in range(1,b+1):
#        print(i)
#elif a=="down":
#    c=int(input("Enter number below 20: "))
#    for d in range(20,c-1,-1):
#        print(d)
#else:
#    print("I don't understand!")
    

#print("how many user you want to invite?\t") #Task 44
#a=int(input())
#if a<=10:    
#    for i in range(1,a+1):
#        b=str(input("Please give the name: "))
#        print(b," has been invited!")
#else:
#    print("Too many people!")
        
    

#Total=0 #Task 45
#while Total<=50:
#    a=int(input("Enter number: "))
#    Total=Total+a
#print("Total is ",Total)


#a=0 #Task46
#while a<=5:
#    a=int(input("Enter number: "))
#print("The last number you entered was a ",a)



#a=int(input("Enter number: ")) #Task47
#b=int(input("Enter number: "))
#c=a+b
#d=str(input("Want add again number? (yes/no)\n "))
#while d=="yes":
#    e=int(input("Enter number: "))
#    c=c+e
#    d=input("Do you want to enter number? (yes/no) ")  
#print("Thanks! Total is ",c)    



#a=str(input("Enter someone's name tha you want to invite: ")) #Task 48
#print(a," has been invited")
#b=0
#a=input("do you want add someone else? (yes/no)")
#while a=="yes":
#    a=str(input("Enter someone's name tha you want to invite: "))
#    print(a," has been invited")
#    b=b+1
#    a=input("do you want add someone else? (yes/no)")


#compnum=50 #Task 49
#b=1
#a=int(input("Enter number: "))
#while a!=compnum:
#    if a<compnum:
#        print("too low!")
#    elif a>compnum:
#        print("too high!")
#    b=b+1
#    a=int(input("Enter number: "))    
#print("Well done, you took ",b," attempts.")    


#a=int(input("Enter number between 10 and 20 : ")) #Task 50
#while a<10 or a>20:
#    if a<=10:
#        print("Too low!")
#    else:
#        print("Too high!")
#    a=int(input("Enter number between 10 and 20 : "))
#print("Thank you!")
    
    

#def pypart(n):
#    for i in range(0, n):
#        for j in range(0, i+1):
#            print("* ",end="")
#        print("\r")
#n = 5
#pypart(n)





