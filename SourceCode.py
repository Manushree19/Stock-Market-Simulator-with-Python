import random
import numpy as np
import matplotlib.pyplot as plt

def Stock1():
    
    print("1. Data from the the last 1 year.")
    print("2. Data from the the last 8 months.")
    print("3. Data from the the last 4 months.")
    print("4. Data from the the last 1 month.")
    print("5. Data from the the last 1 day.")
    print()
    x= int(input("Choose from 1 to 5: "))

    f = open("Stock1.txt", "w")

    if x==1:
            
        a= random.randrange(0,10000)
        b = str(a)
        f.write(b)
        for i in range(0,365):
            a= random.randrange(0,10000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 365
        y = [random.randint(0, 10000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Quantum Capital Company-1 Year Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x==2:
            
        a= random.randrange(0,10000)
        b = str(a)
        f.write(b)
        for i in range(0,240):
            a= random.randrange(0,10000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 240
        y = [random.randint(0, 10000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Quantum Capital Company-8 Months Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x==3:
            
        a= random.randrange(0,10000)
        b = str(a)
        f.write(b)
        for i in range(0,120):
            a= random.randrange(0,10000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 120
        y = [random.randint(0, 10000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Quantum Capital Company-4 Months Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x==4:
            
        a= random.randrange(0,10000)
        b = str(a)
        f.write(b)
        for i in range(0,30):
            a= random.randrange(0,10000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 30
        y = [random.randint(0, 10000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Quantum Capital Company-1 Month Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

    elif x==5:
         a= random.randrange(0,10000)
         b = str(a)
         f.write(b)

    else:
        print("Inputted value is not a valid number.")

    f.close()
    
def Stock2():
    
    print("1. Data from the last 1 year.")
    print("2. Data from the last 8 months.")
    print("3. Data from the last 4 months.")
    print("4. Data from the last 1 month.")
    print("5. Data from the last 1 day.")
    print()
    x = int(input("Choose from 1 to 5: "))

    f = open("Stock2.txt", "w")

    if x == 1:
            
        a= random.randrange(0,20000)
        b = str(a)
        f.write(b)
        for i in range(0,365):
            a= random.randrange(0,20000)
            b = str(a)
            f.write("\n")
            f.write(b)
            
        num_values = 365
        y = [random.randint(0, 20000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Visionary Ventures Company-1 Year Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x == 2:
            
        a= random.randrange(0,20000)
        b = str(a)
        f.write(b)
        for i in range(0,240):
            a= random.randrange(0,20000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 240
        y = [random.randint(0, 20000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Visionary Ventures Company-8 Months Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x == 3:
            
        a= random.randrange(0,20000)
        b = str(a)
        f.write(b)
        for i in range(0,120):
            a= random.randrange(0,20000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 120
        y = [random.randint(0, 20000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Visionary Ventures Company-4 Months Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()
            
    elif x == 4:
            
        a= random.randrange(0,20000)
        b = str(a)
        f.write(b)
        for i in range(0,30):
            a= random.randrange(0,20000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 30
        y = [random.randint(0, 20000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Visionary Ventures Company-1 Month Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()
    
    elif x == 5:
         a = random.randrange(0, 20000)
         b = str(a)
         f.write(b)

    else:
        print("Inputted value is not a valid number.")

    f.close()


def Stock3():
    
    print("1. Data from the the last 1 year.")
    print("2. Data from the the last 8 months.")
    print("3. Data from the the last 4 months.")
    print("4. Data from the the last 1 month.")
    print("5. Data from the the last 1 day.")
    print()
    x= int(input("Choose from 1 to 5: "))

    f = open("Stock3.txt", "w")

    if x==1:
            
        a= random.randrange(0,30000)
        b = str(a)
        f.write(b)
        for i in range(0,365):
            a= random.randrange(0,30000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 365
        y = [random.randint(0, 30000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Cosmos Limited Company-1 Year Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x==2:
            
        a= random.randrange(0,30000)
        b = str(a)
        f.write(b)
        for i in range(0,240):
            a= random.randrange(0,30000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 240
        y = [random.randint(0, 30000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Cosmos Limited Company-8 Months Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x==3:
            
        a= random.randrange(0,30000)
        b = str(a)
        f.write(b)
        for i in range(0,120):
            a= random.randrange(0,30000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 120
        y = [random.randint(0, 30000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Cosmos Limited Company-4 Months Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x == 4:
            
        a= random.randrange(0,30000)
        b = str(a)
        f.write(b)
        for i in range(0,30):
            a= random.randrange(0,30000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 30
        y = [random.randint(0, 30000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Cosmos Limited Company-1 Month Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()
        
    elif x==5:
         a= random.randrange(0,30000)
         b = str(a)
         f.write(b)

    else:
        print("Inputted value is not a valid number.")

    f.close()

def Stock4():
    
    print("1. Data from the the last 1 year.")
    print("2. Data from the the last 8 months.")
    print("3. Data from the the last 4 months.")
    print("4. Data from the the last 1 month.")
    print("5. Data from the the last 1 day.")
    print()
    x= int(input("Choose from 1 to 5: "))

    f = open("Stock4.txt", "w")

    if x==1:
            
        a= random.randrange(0,40000)
        b = str(a)
        f.write(b)
        for i in range(0,365):
            a= random.randrange(0,40000)
            b = str(a)
            f.write("\n")
            f.write(b)
 
        num_values = 365
        y = [random.randint(0, 40000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Phoenix Financials Company-1 Year Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x==2:
            
        a= random.randrange(0,40000)
        b = str(a)
        f.write(b)
        for i in range(0,240):
            a= random.randrange(0,40000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 240
        y = [random.randint(0, 40000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Phoenix Financials Company-8 Months Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x==3:
            
        a= random.randrange(0,30000)
        b = str(a)
        f.write(b)
        for i in range(0,120):
            a= random.randrange(0,30000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 120
        y = [random.randint(0, 30000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Phoenix Financials Company-4 Months Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x==4:
            
        a= random.randrange(0,40000)
        b = str(a)
        f.write(b)
        for i in range(0,30):
            a= random.randrange(0,40000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 30
        y = [random.randint(0, 40000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Phoenix Financials Company-1 Month Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x==5:
         a= random.randrange(0,40000)
         b = str(a)
         f.write(b)

    else:
        print("Inputted value is not a valid number.")

    f.close()

def Stock5():
    
    print("1. Data from the the last 1 year.")
    print("2. Data from the the last 8 months.")
    print("3. Data from the the last 4 months.")
    print("4. Data from the the last 1 month.")
    print("5. Data from the the last 1 day.")
    x= int(input("Choose from 1 to 5: "))

    f = open("Stock5.txt", "w")

    if x==1:
            
        a= random.randrange(0,50000)
        b = str(a)
        f.write(b)
        for i in range(0,365):
            a= random.randrange(0,50000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 365
        y = [random.randint(0, 50000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Cybertech Inc. Company-1 Year Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x==2:
            
        a= random.randrange(0,50000)
        b = str(a)
        f.write(b)
        for i in range(0,240):
            a= random.randrange(0,50000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 240
        y = [random.randint(0, 50000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Cybertech Inc. Company-8 Months Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x==3:
            
        a= random.randrange(0,50000)
        b = str(a)
        f.write(b)
        for i in range(0,120):
            a= random.randrange(0,50000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 120
        y = [random.randint(0, 50000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Cybertech Inc. Company-4 Months Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()

    elif x == 4:
            
        a= random.randrange(0,50000)
        b = str(a)
        f.write(b)
        for i in range(0,30):
            a= random.randrange(0,50000)
            b = str(a)
            f.write("\n")
            f.write(b)

        num_values = 30
        y = [random.randint(0, 50000) for _ in range(num_values)]

        plt.plot(range(1, num_values + 1), y, linestyle="solid",color="green")

        plt.fill_between(range(1, num_values + 1), y, color='green', alpha=0.3)

        plt.title("Cybertech Inc. Company-1 Month Stocks Graph")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")

        plt.show()
        
    elif x==5:
         a= random.randrange(0,50000)
         b = str(a)
         f.write(b)

    else:
        print("Inputted value is not a valid number.")

    f.close()

def choice():
    print("1. Stock 1 - Quantam Capital Company ($0-10000)")
    print("2. Stock 2 - Visionary Ventures Company ($0-20000)")
    print("3. Stock 3 - Cosmos Limited Company ($0-30000)")
    print("4. Stock 4 - Phoenix Financials Company ($0-40000)")
    print("5. Stock 5 - Cybertech Inc. Company ($0-50000)")

    n= int(input("Enter which number of Stock's data you want- "))

    while True:
        if n==1:
            Stock1()
            break
        elif n==2:
            Stock2()
            break
        elif n==3:
            Stock3()
            break
        elif n==4:
            Stock4()
            break
        elif n==5:
            Stock5()
            break
        else:
            n= int(input("Enter a valid number- "))
            
class StockMarket:
    def __init__(self):
        self.s = {}
        self.s["quantum capital"] = random.randint(0,10000)
        self.s["visionary ventures"] = random.randint(0,20000)
        self.s["cosmos limited"] = random.randint(0,30000)
        self.s["phoenix financials"] = random.randint(0, 40000)
        self.s["cybertech inc"] = random.randint(0, 50000)
        self.p = {}

    def buy_stock(self, comp, value):
        comp_lower = comp.lower() 
        
        if comp_lower in map(str.lower, self.s.keys()):
            if value <= 0:
                print("Invalid value. Please enter a positive amount.")
                return

            price = self.s[comp_lower]
            quantity = value / price

            if self.p.get(comp_lower):
                self.p[comp_lower]["quantity"] += quantity
                self.p[comp_lower]["total_value"] += value
            else:
                self.p[comp_lower] = {"quantity": quantity, "total_value": value}

            print(f"Bought {quantity:.2f} shares of {comp} at ${price} each.")
        else:
            print(f"{comp} is not listed in the stock market.")

    def sell_stock(self, comp, value):
        if comp.lower() in self.p:
            if value <= 0:
                print("Invalid value. Please enter a positive amount.")
                return

            price = self.s[comp.lower()]
            quan = value / price

            if self.p[comp.lower()]["quantity"] >= quan and self.p[comp.lower()]["total_value"] >= value:
                self.p[comp.lower()]["quantity"] -= quan
                self.p[comp.lower()]["total_value"] -= value
                print(f"Sold {quan:.2f} shares of {comp} at ${price} each.")
            else:
                print(f"You don't have enough shares of {comp} to sell.")
        else:
            print(f"You don't have any shares of {comp} in your portfolio.")


    def display_portfolio(self):
    
        print("Portfolio:")
    
        for comp, info in self.p.items():
            print(f"{comp}: {info['quantity']:.2f} shares, Total Value: ${info['total_value']:.2f}")

    def display_stock_prices(self):
    
        print("Stock Prices:")
    
        for comp, price in self.s.items():
            print(f"{comp}: ${price}")

market = StockMarket()

def buysell():

    while True:
                
        market.display_stock_prices()     

        print("\nWhat do you want to do?")
        print("1. Buy stocks")
        print("2. Sell stocks")
        print("3. Display Portfolio")
        print("4. Exit")
        print()
        choice = input("Enter your choice (1/2/3/4): ")
        print()

        if choice == "1":
            comp = input("Enter the company name: ").upper()
            value = float(input("Enter the value of stocks to buy: "))
            market.buy_stock(comp, value)
            print()
    
        elif choice == "2":
            comp = input("Enter the company name: ").upper()
            value = float(input("Enter the value of stocks to sell: "))
            market.sell_stock(comp,value)
            print()
        
        elif choice == "3":
            market.display_portfolio()
            print()
        
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid.")

def editprofile():

    EDIT = input("Do you want to edit your username?Enter yes or no: ")
    if EDIT.lower() == 'yes':
        ch1 = input("Enter your old username: ")
        with open("User_Database.txt", 'r') as f:
            lines = f.readlines()
        isthereinfile = False
        for line in lines:
            if ch1 in line:
                ch2 = input("Enter the new username: ")
                with open("User_Database.txt", 'w') as f:
                    for line in lines:
                        if ch1 in line:
                            f.write(line.replace(ch1, ch2))
                        else:
                            f.write(line)
                            print("Username updated successfully.")
        isthereinfile = True
        if not isthereinfile:
            print("Please input the correct old username. Kindly check again.")
    elif EDIT.lower() == 'no':
        print("Okay.")
        print()
    else:
        print("Invalid Input.")
            

check = 1

while check == 1:
    
    x= input("Are you a subscriber- ")
    print()

    if x.lower()=="no":
        a= int(input("Choose 1 for Sign up and 2 for Login- "))
    
        if a==1:
        
            flag=1
            while flag==1:
    
                f= open("User_Database.txt", "r+")

                print()
                u= input("Enter Username- ")
                
                for line in f:
                    if u.lower() in line.lower():
                        flag=1
                        print()
                        print("This username is taken.")
                        print()
                        u= input("Enter another Username- ")
                        print()
                          
                email= input("Enter Email-Id- ")
                age= int(input("Enter age- "))

                if age<18:
                     print()
                     print("You are too young for this.")
                     flag=0
                     break

                v= input("Make a strong Password- ")
                flag=0
    
    
                f.write(u)
                f.write(" ")
                f.write(email)
                f.write(" ")
                agestr= str(age)
                f.write(agestr)
                f.write(" ")
                f.write(v)
                f.write(" ")
                f.write("\n")
                f.close()

        elif a==2:
        
            u= input("Enter Username= ")
            v= input("Enter Password= ")
            f= open("User_Database.txt", "r")

            flag=0
            name= " "

            for line in f:
                if u and v in line:
                    flag=1
                    name= line

            while True:
                if flag==1:
                    break
                
                else:
                    print("Wrong username or password.")
                    continue

            f.close()

        else:
            print("Invalid input.")
            break

        editprofile()
        
        print("You can now successfully view stocks. ")
        print()
        y= input("Do you want to become a subscriber to be able to buy and sell stocks? ")

        if y.lower()=="no":
            print("You can only view the stocks then. ")
            z= input("Do you want to view any stocks? ")
            
            if z.lower()=="no":
                print("Okay. Thank you for visiting!")
                
            elif z.lower()=="yes":
                print("""These is the list of the companies we have a collaboration with: 
Quantum Capital
StellarTech Solutions
Virtuoso Ventures
Cybertech Inc
Nexus Industries
Pinnacle Holdings
Phoenix Financials
Titan Technologies Inc.
Spectrum Solutions Group
Cosmos Limited
Nova Enterprises
Momentum Holdings
Synergy Solutions Inc.
Evolve Industries
Visionary Ventures.""")

                print()
                
                n=input("Search the company name here: ")

                if n==['StellarTech Solutions','Evolve Industries','Spectrum Solutions Group','Momentum Holdings','Pinnacle Holdings','Nova Enterprises','Virtuoso Ventures','Nexus Industries','Titan Technologies Inc.','Synergy Solutions Inc.']:
                    print(n," is not selling their company stocks right now.")
                    
                else:
                    print(n," is selling their company stocks right now.")
                    choice()

            break
    
        elif y.lower()=="yes":
            f1= open("User_Database.txt", "r")
            f2= open("Sub_Database.txt", "a")

            u= input("Enter Username= ")
            v= input("Enter Password= ")

            for line in f1:
                if u and v in line:
                    flag=1
                    name= line

            f2.write(name)
            
            f1.close()
            f2.close()

            editprofile()

            m=input("Do you want to view stocks? ")
            
            if m.lower()== "yes":
                choice()
                n= input("Do you want to buy or sell stocks? ")
                
                if n.lower()=="yes":
                    buysell()
                    
                elif n.lower()=="no":
                    print("Alright. Have a good day!")
                    break
                    
                else:
                    print("Invalid input.")
                    break

            elif m.lower()=="no":
                print("Alright. Have a good day!")
                break
                    
            else:
                print("Invalid input.")
                break

        else:
            print("Invalid input")

    elif x.lower()== "yes":
        print("Login- ")
        u= input("Enter Username= ")
        v= input("Enter Password= ")
        f= open("Sub_Database.txt", "r")

        flag=0

        for line in f:
            if u and v in line:
                flag=1

        if flag==1:

            editprofile()
            
            m=input("Do you want to view stocks? ")
            
            if m.lower()== "yes":
                choice()
                n= input("Do you want to buy or sell stocks? ")
                
                if n.lower()=="yes":
                    buysell()
                    
                elif n.lower()=="no":
                    print("Alright. Have a good day!")
                    break
                    
                else:
                    print("Invalid input.")
                    break
                    
            elif m.lower()=="no":
                print("Alright. Have a good day!")
                break
                    
            else:
                print("Invalid input.")
                break
            
        else:
            print("Wrong username or password.")
            break

        f.close()

    check = 0
