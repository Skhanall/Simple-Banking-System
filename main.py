
def show_balance(balance):
    print("---------------------")
    print(f"\nYour balance is ${balance:.2f}") #(floating point decimal)
    

def deposit():
    print("---------------------")
    amount = float(input("\nEnter an amount to deposit: $ \n"))
    print("---------------------")
    if amount < 0:
        print("---------------------")
        print("\nPlease enter a valid amount.\n")
        print("---------------------")
        return 0
    else:
        print("---------------------")
        print("You have successfully deposited ${deposit} into your bank account!")
        print("---------------------")
        return amount

def withdraw(balance):
    print("---------------------")
    amount = float(input("Enter amount to withdraw: "))
    print("---------------------")

    if amount > balance:
        print("---------------------")
        print("Not enough funds.")
        print("---------------------")
        return 0
    elif amount < 0:
        print("---------------------")
        print("Amount must be greater than 0")
        print("---------------------")
        return 0
    else:
        print("You have successfully withdrawn ${balance} from your bank account!")
        return amount
    
def rating():
    print("---------------------")
    rate = int(input("Enter rating from 1-5: "))

    if rate<=0 or rate>5:
        print("---------------------")
        print("Please enter a valid rating.")
    else:
        print("---------------------")
        print("Thank you for your rating! We appreciate it.")
    

def main():
    balance = 0
    is_running = True

    while is_running:
        print("---------------------")
        print("   Banking Options   ")
        print("---------------------")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Rate Your Experience with us")
        print("5.Exit")
        print("---------------------")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            rating()
        elif choice == '5':
            is_running = False
        else:
            print("---------------------")
            print("Please make a valid option.")
            print("---------------------")

    print("---------------------")
    print("Thank you for banking with us! Have a nice day!")
    print("---------------------")

if __name__ == '__main__':
    main()
