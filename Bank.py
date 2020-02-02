import smtplib
import random

# create bank class
class Bank:
    # declaring variables
    def __init__(self, name, age, balance, pin, email):
        self.name = name
        self.age = age
        self.balance = balance
        self.pin = pin
        self.email = email

    # deposit function
    def deposit(self):
        card = input("Are you depositing by card?(y/n) : ")
        if card == "y":
            pin = int(input("Please enter 4-digit pin : "))
            if pin == self.pin:
                y = int(input("How much funds would you like to deposit? : "))

                self.balance = self.balance + y
                print("{} user now has Rs. {} in their account".format(self.name, self.balance))
            else:
                print("INCORRECT PIN")
        else:
            y = int(input("How much funds would you like to deposit? : "))
            self.balance = self.balance + y
            print("{} user now has Rs. {} in their account".format(self.name, self.balance))

    # withdraw function
    def withdraw(self):
        card = input("Are you withdrawing by card?(y/n) : ")
        if card == "y":
            on = input("Are you doing an online transaction? (y/n)")
            if on == "y":
                otp = random.randint(1000,9999)
                #sending otp via email
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login("5358@sanskritischool.edu.in", "aadi17jain")
                server.sendmail(
                  "5358@sanskritischool.edu.in", 
                  self.email, 
                  str(otp) + ' is your otp')
                server.quit()
                print("An otp has been sent to your registered email")
                check = int(input("otp : "))
                if check == otp:
                    x = int(input("How much funds would you like to withdraw? : "))
                    if (self.balance > x):
                        self.balance = self.balance - x
                        print("{} user now has Rs. {} in their account".format(self.name, self.balance))
                    else:
                        print("insufficient funds")
                else:
                    print("the otp you entered was wrong")
            else:
            
                pin = int(input("Please enter 4-digit pin : "))
                if pin == self.pin:
                    x = int(input("How much funds would you like to withdraw? : "))
                    if (self.balance > x):
                        self.balance = self.balance - x
                        print("{} user now has Rs. {} in their account".format(self.name, self.balance))
                    else:
                        print("You don't have enough funds in your account to withdraw.")
                else:
                    print("INCORRECT PIN")
                    
        else:
            x = int(input("How much funds would you like to withdraw? : "))
            if (self.balance > x):
                self.balance = self.balance - x
                aadi
                print("{} user now has Rs. {} in their account".format(self.name, self.balance))
    # loan function
    def loan(self):
        z = int(input("For how much do you want to take a loan? : "))
        payback = z * 0.08 + z
        if z > 2 * self.balance:
            print("The bank cannot provide you a loan that large.")
        else:
            self.balance = self.balance + z
            print(
                "your rate of interest is 8% per annum, you will have to pay back Rs. {} in one year.".format(payback))
            print("{} user now has Rs. {} in their account".format(self.name, self.balance))


# bank accounts
aadi = Bank("aadi", 18, 20000, 8907,"aadijain48@gmail.com")
vipin = Bank("vipin", 23, 200000, 8908, "vipinkant132@gmail.com")
hershil = Bank("hershil", 18, 2000000, 8909, "fortnite.harshil@gmail.com")

 
# choosing user
active = "y"
while active == "y":
    name = input("Enter name : ")
    if name == "aadi":
        name = aadi
    elif name == "vipin":
        
        name = vipin
    elif name == "hershil":
        name = hershil

        # continuing trasactions
    # transactions
    a = input("Do you want to deposit, withdraw funds or take a loan? w/d/l : ")
    # Withdraw
    if a == "w":
        name.withdraw()
        # Deposit

    elif a == "d":
        name.deposit()
        # Loan
    elif a == "l":
        name.loan()

    print("You want to do something more (y/n)")
    active = input()