# WORKING OF ATM FOR A SINGLE USER. PROJECT NO.- 23
Name = "Mr. ADEY RATNA SHAH "
print("Hello,",Name)
PIN = int(input(" Enter your four digit safety PIN: "))
a  = ['1. Account balance','2. PIN change', '3. Cash withdrawal', '4. Cash Deposit']
balance  = 95056
if PIN == 5648:
    print("Welcome, ", Name) 
    print("How can we help you today?")
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    help = input("Type your query here: ")
    if help == "Account balance" or help=="1":
        print("Your account balance is", balance)
    elif help== "PIN change" or help=="2":
        num = int(input("Enter your mobile number: "))
        if num == 9068632853:
            OTP = int(input("Enter the OTP sent to your mobiLe number: "))
            if OTP == 4521:
                inst= ["Instructions:",'1. Each letter of the PIN should be a number between 0 to 9 including 0 and 9.',
                '2. The PIN should contain 4 digits.',"3. The PIN can't contain any special characters(@,$,%,&,_,<,>,?)."]
                print(inst[0])
                print(inst[1])
                print(inst[2])
                print(inst[3])
                new = (input("Enter your new PIN: "))
                print(new)

                if len(new) == 4 :
                    print("Your pin has been changed successfully")
                else:
                    print("Try a different valid combination")
            else:
                print("You have entered a wrong PIN")
        else:
            print("Please enter the bank registered mobile number and try again")
    elif help == "Cash withdrawal" or help=="3":
        cash = int(input("Enter the amount you want to withdrawal: "))
        remain1 = balance - cash
        if remain1>0:
            print("Please collect your cash. The amount has been debited from your account.") 
            ques = input("Do you want us to display your balance?: Yes(Y) or NO(N) ")
            if ques=="YES" or ques =="yes" or ques =="y" or ques=="Y" or ques =="Yes":
                print("Remaining amount in your account is:", remain1)
        elif remain1<0: 
            print("Your account balance is",balance)
            print("Please enter an amount lower than this.")
            pass              
        else:
            pass

    elif help := "Cash Deposit" or help=="4":
        deposit = int(input("Enter amount you want to deposit: "))
        remain2 = balance + deposit
        print("Your cash has been credited,", Name)
        ques = input("Do you want us to display your balance?: Yes(Y) or NO(N) ")
        if ques=="YES" or ques =="yes" or ques =="y" or ques=="Y" or ques =="Yes":
            print("Remaining amount in your account is:", remain2)   
        else:
            pass     

    else:
        print("Please choose one of the above mentioned options")

else:
    print(" You have entered an invalid PIN, kindly try again")

print("Have a nice day", Name)


