"""
Name: Benjamin Nguyen
Date: 5/25/2026
Short Description: This program will calculate the index statement from your bank statement
"""

import csv

def description():
    print('Your bank statement must be in a csv file')
    print('Based of user input of the file location that lists the bank statement, this program will calculate the index.')

# gives the user a menu to choose a selection, in which returns the selection to main
def menu():
    print('Type 1 to enter the file name of the bank statement and read its contents')
    print('Type 2 to display the contents of the banks statement')
    print('Type 2 to calculate the index of the file name')
    print('Type 3 to calculate the cost of the one of the statements in a time frame')
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
def bank_display(numbers):
    #Iterates through the strings in the 2d list, and makes sure that and finds the max character of spaces to
    #separate the bank statement

    length = 0
    for row in numbers:
        for item in row:
            if len(item) > length:
                length = len(item)

    #Determines the column_width by adding the max amount of characters + 1

    column_width = length + 1

    #Iterates through the strings in the 2d list and adds them through row_string with a format of the max amount of spaces
    #calculated earlier to separate the strings from overlapping to the next column.

    for row in numbers:
        row_string = ''
        for item in row:
            row_string += f'{item:<{column_width}}'
        print(row_string)


# Where all the functions are called
if __name__ == "__main__":
    description()
    print()
    selection = menu()
    flag = 0

    #determines when to selection is over and when the other functions are called
    while selection != 5:
        if selection == 1:
            raw_statement = read_file()
            flag = 1
        if selection == 2:
            if flag == 0:
                print('Must choose choice 1 first')
            else:
                bank_display(raw_statement)

        #Goes back to the menu after each function is done
        selection = menu()

