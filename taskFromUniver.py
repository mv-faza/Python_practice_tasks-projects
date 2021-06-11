#a=str(input())#task1
#b=str(input())
#c=str(input())
#d=str(input())
#e=str(input())
#f=str(input())
#g=str(input())
#h=str(input())
#i=str(input())
#MyGird=[[a,b,c],[d,e,f],[g,h,i]]
#def Flip(x):
#    AsSet=0
#    AsSet=x[0]
#    x[0]=x[2]
#    x[2]=AsSet
#    for i in x:
#        print(i)
#Flip(MyGird)

#a=str(input())#task2
#b=str(input())
#c=str(input())
#d=str(input())
#e=str(input())
#f=str(input())
#g=str(input())
#h=str(input())
#i=str(input())
#MyGird=[[c,b,a],[f,e,d],[i,h,g]]
#def Flip(x):
#    AsSet=0
#    AsSet=x[0]
#    x[0]=x[2]
#    x[2]=AsSet
#   for i in x:
#        print(i)
#Flip(MyGird)

#a=str(input())#task3
#b=str(input())
#c=str(input())
#d=str(input())
#e=str(input())
#f=str(input())
#g=str(input())
#h=str(input())
#i=str(input())
#MyGird=[[c,f,i],[b,e,h],[a,d,g]]
#def Flip(x):
#    for i in x:
#        print(i)
#Flip(MyGird)

#a= (1,2,3,4,5,6,7,8,9,0)
#b= [1,2,3,4,5,6,7,8,9,0]

#print('a=',a.__sizeof__())
#print('b=',b.__sizeof__())




a=str(input("Enter name of the student: "))
b=int(input("Please enter student score(1 to 10): "))
if b<=7:
    print("You fail exam!")    
c=int(input("Please enter student score(1 to 10): "))
if c<=7:
    print("You fail exam!")   
d=int(input("Please enter student score(1 to 10): "))
if d<=7:
    print("You fail exam!")   
e=int(input("Please enter student score(1 to 10): "))
if e<=7:
    print("You fail exam!")   
f=int(input("Please enter student score(1 to 10): "))
if f<=7:
    print("You fail exam!")   
g=b+c+d+e+f
if g>=40:
    print("Your total score is: ",g)
else:
    print("Your total score is: ",g,". You fail it!")
