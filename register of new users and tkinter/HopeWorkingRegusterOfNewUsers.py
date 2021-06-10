class hotelfarecal:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):

        print ("\n\n*****WELCOME TO HI-TECH HOTEL*****\n")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your full name:")
        self.address=input("\nEnter your curent address:")
        self.cindate=input("\nEnter year to check in date:")
        self.coutdate=input("\nEnter year to checkout date:")
        print("Your have room nos.:",self.rno,"\n")
        
    def roomrent(self):#sel1353

        print ("We have the following available options for you:-")

        print ("1.  type A---->$ 900 Per Night\-")

        print ("2.  type B---->$ 600 Per Night\-")

        print ("3.  type C---->$ 450 Per Night\-")

        print ("4.  type D---->$ 300 Per Night\-")

        x=int(input("Enter Your Choice Please->"))

        n=int(input("For How Many Nights Did You Stay:"))

        if(x==1):

            print ("You have booked room type A")

            self.s=900*n

        elif (x==2):

            print ("You have booked room type B")

            self.s=600*n

        elif (x==3):

            print ("You have booked room type C")

            self.s=450*n

        elif (x==4):
            print ("You have booked room type D")

            self.s=300*n

        else:

            print ("Please choose a room")

        print ("Total sum of your room is =$",self.s,"\n")

    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")

        print("1.water----->$2","2.tea----->$1,5","3.breakfast combo--->$9","4.lunch---->$12","5.dinner--->$15","6.Exit")


        while (1):

            c=int(input("Enter your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+20*d

            elif (c==2):
                d=int(input("Enter the quantity:"))
                self.r=self.r+10*d

            elif (c==3):
                d=int(input("Enter the quantity:"))
                self.r=self.r+90*d
            elif (c==4):
                d=int(input("Enter the quantity:"))
                self.r=self.r+110*d

            elif (c==5):
                d=int(input("Enter the quantity:"))
                self.r=self.r+150*d

            elif (c==6):
                break;
            else:
                print("Invalid option")

        print ("Total food Cost=$",self.r,"\n")

    

    def gamebill(self):
        print ("******GAME MENU*******")

        print ("1.Table tennis----->$5","2.Bascketball----->$7","3.Football--->$10","4.Video games---->$4","5.Pool--->$8==6","6.Exit")



        while (1):

            
            g=int(input("Enter your choice:"))


            if (g==1):
                h=int(input("No. of hours:"))
                self.p=self.p+60*h

            elif (g==2):
                h=int(input("No. of hours:"))
                self.p=self.p+80*h

            elif (g==3):
                h=int(input("No. of hours:"))
                self.p=self.p+70*h

            elif (g==4):
                h=int(input("No. of hours:"))
                self.p=self.p+90*h

            elif (g==5):
                h=int(input("No. of hours:"))
                self.p=self.p+50*h
            elif (g==6):
                break;

            else:

                print ("Invalid option")



        print ("Total Game Bill=$",self.p,"\n")

    def display(self):
        print ("******HOTEL BILL CHECK******")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)
        print ("Your Food bill is:",self.r)
        print ("Your Game bill is:",self.p)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total bill is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.rt+self.a,"\n")
        self.rno+=1

            

        

        

def main():

    a=hotelfarecal()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate rommrent")

        print("3.Calculate restaurant bill")

        print("4.Calculate gamebill")

        print("5.Show total Check")

        print("6.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurentbill()

        if (b==4):

            a.gamebill()

        if (b==5):

            a.display()

        if (b==6):

            quit()



main()

