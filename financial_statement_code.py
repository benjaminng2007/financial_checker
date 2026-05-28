"""
Name: Benjamin Nguyen
Date: 5/25/2026
Short Description: This program will calculate the index statement from your bank statement
"""

import csv

def description():
    print('Your bank statement must be in a csv file and have the starting balance on the first row')
    print('Bank statement only allows Balance, Housing, Food, Income, Utilities, Entertainment, Transport, and Healthcare in categories')
    print('Based of user input of the file location that lists the bank statement, this program will calculate the index.')
    print('Housing, Utilities and Online Subscriptions is only accounted into the index score')
    print('Example Fake Bank Statement I used is in the github commited to the main branch')
    print(
        'The file name should be copied as a path in your files for example C:\\Fake Bank Statement for Project Example\\Fake Bank Statement.csv then entered into terminal')

# gives the user a menu to choose a selection, in which returns the selection to main
def menu():
    print('Type 1 to enter the file name of the bank statement and read its contents')
    print('Type 2 to display the contents of the banks statement')
    print('Type 3 to calculate the index of the file name and display it')
    print('Type 4 to end the program')
    print()
    choice = int(input('Please enter your choice: '))
    return choice

# reads the file and returns a 2d list of the contents of the file before closing it
# checks if the file is found in the system and also tells the user to input the correct file name again
def read_file():
    while True:
        try:
            print()
            file_list = []
            file_name = input('Please enter your file name: ')
            # input('Please enter the file name of the bank statement: '))
            with open(file_name) as open_file:
                file_contents = csv.reader(open_file)
                for row in file_contents:
                    file_list.append(row)
            return file_list
        except FileNotFoundError:
            print('Please enter another csv file name again')

#Displays the bank statement of the csv file the user inputted earlier
def bank_display(list2d):
    #Iterates through the strings in the 2d list, and makes sure that and finds the max character of spaces to
    #separate the bank statement

    length = 0
    for row in list2d:
        for item in row:
            if len(item) > length:
                length = len(item)

    #Determines the column_width by adding the max amount of characters + 1

    column_width = length + 1

    #Iterates through the strings in the 2d list and adds them through row_string with a format of the max amount of spaces
    #calculated earlier to separate the strings from overlapping to the next column.

    #The outer loop "for row in numbers" resets the string to be empty each time a new row starts
    #print(raw_string) must be put underneath for row in numbers in order for the row_string to reset the string each time
    #or else the string will continue to be printed again each time

    for row in list2d:
        row_string = ''
        for item in row:
            row_string += f'{item:<{column_width}}'
        print(row_string)

def calculate_index(contents):
    income_row = []
    debt_row = []

    #detects if the category is an income and adds it to the income_row list to only allow income rows
    for row in contents:
        if 'Income' in row or 'Deposit' in row:
            income_row.append(row)
        #detects if the category is a debt and adds it to debt_row to allow only debt rows
        elif 'Housing' in row or 'Utilities' in row or 'Online Subscriptions' in row:
            debt_row.append(row)

    #only adds the income to the net income
    net_income = 0
    for positive_money in income_row:
        net_income += float(positive_money[5])

    #Estimates the gross income based of the net income using the formula of the net_income / (1-0.25)
    gross_income = net_income / (1-0.25)

    #Adds all the debt from the debt_row into debt
    debt = 0
    for negative_money in debt_row:
        debt += float(negative_money[4])

    #calculates the index score based of the formula of the (debt/ gross_income) * 100 and returns the score
    index_score = (debt / gross_income) * 100
    return f'{index_score:.2f}'


# Where all the functions are called
if __name__ == "__main__":
    description()
    print()
    selection = menu()
    flag = 0

    #determines when to selection is over and when the other functions are called
    while selection != 4:
        if selection == 1:
            raw_statement = read_file()
            flag = 1
        elif selection == 2:
            if flag == 0:
                print('Must choose choice 1 first')
            else:
                print()
                bank_display(raw_statement)
                print()
        elif selection == 3:
            if flag == 0:
                print('Must choose choice 1 first')
            else:
                score = calculate_index(raw_statement)
                print()
                print(f'Your index score is: {score}')
                print()

        #Goes back to the menu after each function is done
        selection = menu()
    print()
    print('Thank you for using this program')

