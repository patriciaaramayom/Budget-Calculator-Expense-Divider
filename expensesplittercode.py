"""
PATRICIA CAMILA ARAMAYO MEDINA - A01711784
The following project called “Budget Calculator / Expense Divider” is designed to make life easier for all people who have to share expenses, whether with family, roommates or friends, and also for people who have problems managing their budgets or finances. They can track expenses or simply balance them equally. As a foreigner living with roommates, I am experiencing how difficult it can be to balance or divide expenses equally and keep track in case someone owes money to another. So I think it's very interesting that you can solve a problem that I'm sure many other people have, including me. It is well known that relationships and money are not topics that can be mixed. But studies show that splitting expenses strengthens relationships and establishes equality. This project consists of a shared list of transactions that allows expenses to be balanced, each person enters their expenses and the balance of each participant is calculated.
"""

#The menu function shows the options that the user has.

def menu():
    print('WELCOME TO BUDGET ORGANIZER AND EXPENSES SPLITTER')
    print('---------------------MENU------------------------\n1.New Budget \n2.Expense Splitter \n3.Exit')
    
#This function asks for the basic information for creating a budget, asks for the user interaction. In this function you can add how much money do you have, and also you can record how much money do you spend
    
def create_new_budget():
    print('	BUDGET DETAILS')
    budget_name=str(input("Budget name: "))
    currency_dict = {
    1: {'code': 'MXN', 'name': 'Mexican Peso', 'symbol': 'Mex$'},
    2: {'code': 'USD', 'name': 'United States Dollar', 'symbol': '$'},
    3: {'code': 'BOB', 'name': 'Bolivian Boliviano', 'symbol': 'Bs.'},
    4: {'code': 'EUR', 'name': 'Euro', 'symbol': '€'},
    5: {'code': 'JPY', 'name': 'Japanese Yen', 'symbol': '¥'},
    6: {'code': 'GBP', 'name': 'British Pound Sterling', 'symbol': '£'},
    7: {'code': 'AUD', 'name': 'Australian Dollar', 'symbol': 'A$'},
    8: {'code': 'CNY', 'name': 'Chinese Yuan', 'symbol': '¥'},
    9: {'code': 'CAD', 'name': 'Canadian Dollar', 'symbol': 'C$'},
    10: {'code': 'INR', 'name': 'Indian Rupee', 'symbol': '₹'}}
    print("-----------------------------------------------")
    print("Currency")
    for i, value in currency_dict.items():
        print(f"{i}: {value['name']} ({value['code']})")
    user_choice1 = int(input("Select: "))
    if user_choice1 in currency_dict:
        selected_currency = currency_dict[user_choice1]
        print(f"You selected: {selected_currency['name']} ({selected_currency['code']})")
    else:
        print("ERROR.")
        
    print("-----------------------------------------------")
    print("	New Bank Account")
    debit_account=float(input("Debit account:"))
    credit_account=float(input("Credit account: "))
    cash=float(input("Cash: "))
    starting_balance=debit_account+credit_account+cash
    currency_symbol = selected_currency['symbol']
    print(f"TOTAL:{currency_symbol}{starting_balance:.2f}")
    
    print("-----------------------------------------------")
    print("	New Transaction")
    transaction_value=float(input("Transaction value: "))
    
    print("1.Debit \n2.Credit \n3.Cash")
    user_choice3=int(input("Select: "))
    
    print("1. - Outflow \n2. + Inflow")
    user_choice4=int(input("Select: "))
    if user_choice3 == 1:
        if user_choice4 == 1:
            debit_balance=debit_account-transaction_value
            account_balance=debit_balance+cash+credit_account
            print(f"Account Balance: {currency_symbol}{account_balance:.2f}")
        if user_choice4 == 2:
            debit_balance=debit_account+transaction_value
            account_balance=debit_balance+cash+credit_account
            print(account_balance)
    elif user_choice3 == 2:
        if user_choice4 == 1:
            credit_balance=credit_account-transaction_value
            account_balance=credit_balance+cash+debit_account
            print(account_balance)
        if user_choice4 == 2:
            credit_balance=credit_account+transaction_value
            account_balance=credit_balance+cash+debit_account
            print(account_balance)
    elif user_choice3 == 3:
        if user_choice4 == 1:
            cash_balance=cash-transaction_value
            account_balance=cash_balance+debit_account+credit_account
            print(account_balance)
        if user_choice4 == 2:
            cash_balance=cash+transaction_value
            account_balance=cash_balance+debit_account+credit_account
            print(account_balance)
    else:
        print("Error")
#This function has the purpose of asking the user basic info about the new expense, this is needed to make calculations in future fuctions. Also in this function a list is created with the names of the participants.
def create_new_expense_splitter():
    title=input('Title: ')
    par=int(input('Number of Participants: '))
    names_participants=[]
    for i in range(0, par):
        ele = input(f'Participant {i + 1} Name: ')
        names_participants.append(ele) 
    return title,par,names_participants

#This is the fuction that makes the calculations, with the expense and participants value, it will show the amount everyone has to pay, equially divided.Also in this function a list is created with the first list that contains the names of the participants, and the amount of money each participant has to pay
def calc(title,par, expense, names_participants):
    amount= expense/par
    lst_parts=[]
    for row in names_participants:
        lst_parts.append(row+": "+str(amount))
        print(row+": "+str(amount))
    return lst_parts
#In this function a goodbye message is displayed, where the computer thanks the user for using the expense splitter
def printString(message):
    for i in range(0,len(message)):
        print(message[i], end="")
    print("\n")
#the main fuction is where we ask the user for some inputs. In this funcion we use the condicionals and loops. When the user finished using the program, the menu will be shown again.
def main():
    continua= True
    while continua:
        menu()
        user_choice = int(input("Select: "))
        if user_choice == 1:
            create_new_budget()
        elif user_choice ==2:
            print("-----------------------------------------------")
            print('Expense Splitter')
            print("-----------------------------------------------")
            title,par,names_participants=create_new_expense_splitter()
            expense=float(input("Put a value: "))
            calc(title,par, expense, names_participants)
            message="Thank you for using the Expense Splitter."
            printString(message)
        elif user_choice == 3:
            print('Goodbye')
        else:
            print("Error")
        print("-----------------------------------------------")
main()
