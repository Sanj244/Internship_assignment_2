history=[]
balance = 10000
print("1.Check Balance")
print("2.Deposit")
print("3.Withdraw")
#Input
choice=int(input("Enter choice:"))
#user choice
#balance
if choice==1:
    print("Balance:",balance)
#deposit
elif choice==2:
    amt=int(input("Enter amount to deposit:"))
    balance+=amt
    history.append("Deposited"+str(amt))
    print("Deposit successful")
    print("New balance:",balance)
#withdrawal
elif choice==3:
    amt=int(input("Enter amount to withdraw: "))
    if balance-amt < 500:
        print("Minimum 500 balance must remain.")
    else:
        balance-=amt
        history.append("withdrawn"+str(amt))
        print("Withdrawal successful!")
        print("New balance:",balance)
else:
    print("Invalid choice")
print("balance:",balance)
print("history:",history)
