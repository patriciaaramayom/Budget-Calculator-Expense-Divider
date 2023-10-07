#The menu function shows the options that the user has.
def menu():
    print('WELCOME TO EXPENSE SPLITTER')
    print('	1.New Group')
    print('	2.Exit')

#This function has the purpose of asking the user basic info about the new expense, this is needed to make calculations in future fuctions. Also in this function a list is created with the names of the participants.

def create_new_group():
    names_par=[]
    title=input('Title: ')
    des=input('Description: ')
    cur=input('Currency: ') 
    cat=input('Category: ') 
    par=int(input('Number of Participants: ')) 
    for i in range(0, par):
        ele = (input())
        names_par.append(ele) 
    return title,des,cur,cat,par,names_par

#This is the fuction that makes the calculations, with the expense and participants value, it will show the amount everyone has to pay, equially divided.Also in this function a matrix is created with the first list that contains the names of the participants, and under their names, the amount of money they have to pay.
def calc(title,des,cur,cat,par, expense, names_par):
    amount= [expense/par,expense/par,expense/par]
    matrix=[names_par,amount]
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()
    return
#In this function a goodbye message is displayed, where the computer thanks the user for using the program.
def printString(message):
    for i in range(0,len(message)):
        print(message[i], end="")
    print("\n")
#the main fuction is where we ask the user for the inputs, except for the create_new_group function. In this funcion we use the condicionals and loops. When the user finished using a group, the menu will be shown again.
def main():
    continua= True
    while continua:
        print("\n")
        menu()
        opcion = int(input("Choose an option: "))
        if opcion == 1:
            title,des,cur,cat,par,names_par=create_new_group()
            expense=float(input("Put a value: "))
            calc(title,des,cur,cat,par, expense, names_par)
            message="Thank you for using the Expense Splitter."
            printString(message)
        elif opcion == 2:
            print('Goodbye')
        else:
            print("Error")
main()
    
