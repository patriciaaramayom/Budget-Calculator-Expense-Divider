#The menu function shows the options that the user has.
def menu():
    print('WELCOME TO EXPENSE SPLITTER')
    print('	1.New Group')
    print('	2.Exit')

#This function has the purpose of asking the user basic info about the new expense, this is needed to make calculations in future fuctions.
def create_new_group():
    title=input('Title: ')
    des=input('Description: ')
    cur=input('Currency: ')
    cat=input('Category: ')
    par=float(input('Participants: '))
    return title,des,cur,cat,par

#This is the fuction that makes the calculations, with the expense and participants value, it will show the amount everyone has to pay, equially divided.
def calc(title,des,cur,cat,par, expense):
    amount= expense/par
    print (amount)
    return

#the main fuction is where we ask the user for the inputs, except for the create_new_group function. In this funcion we use the condicionals and loops. When the user finished using a group, the menu will be shown again.
def main():
    continua= True
    while continua:
        print("\n")
        menu()
        opcion = int(input("Choose an option: "))
        if opcion == 1:
            title,des,cur,cat,par=create_new_group()
            expense=float(input("Put a value: "))
            calc(title,des,cur,cat,par, expense)
            
        elif opcion == 2:
            print('Goodbye')
        else:
            print("Error")
main()
    
