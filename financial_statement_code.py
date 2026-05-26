"""
Name: Benjamin Nguyen
Date: 5/25/2026
Short Description: This program will calculate the index statement from your bank statement
"""
import csv

def description():
    print('Based of user input of the file location that lists the bank statement, this program will calculate the index.')

def menu():
    print('Type 1 to enter the file name of the bank statement and read its contents')
    print('Type 2 to display the contents of the banks statement')
    print('Type 2 to calculate the index of the file name')
    print('Type 3 to calculate the cost of the one of the statements in a time frame')
    choice = int(input('Please enter your choice: '))
    return choice

def read_file():
    while True:
        try:
            print()
            file_list = []
            file_name = input('Please enter the file name of the bank statement: ')
            with open(file_name) as open_file:
                file_lines = csv.reader(open_file)
                for row in file_lines:
                    file_list.append(row)
            return file_list
        except FileNotFoundError:
            print('Please enter another csv file name again')

def bank_display(numbers):
    print(numbers)


if __name__ == "__main__":
    description()
    print()
    selection = menu()

    while selection != 5:
        if selection == 1:
            raw_statement = read_file()
        if selection == 2:
            bank_display(raw_statement)
        selection = menu()

