# Import Libraries
from datetime import datetime

# Task 1

# our data structure
datastructure = []

# datastructure.append({'first_name': 'John', 'last_name': 'Doe', 'volunteer': False,  'volunteerarea': 3,  'datejoined': '','feepaid': True})

# a function to ask user for details and add new member to the list

def add_member():

    # declare local variables
    first_name = ''
    last_name = ''
    volunteerinput = ''
    volunteerarea = ''
    datejoined = ''
    datejoinedinput = ''
    feepaidinput = ''

    # NAMES
    # validate first name as not being empty
    while not first_name.isalpha():
        first_name = input('Enter first name: ')

    # capitalize first letter of first name
    first_name = first_name.capitalize()

    # validate last name
    while not last_name.isalpha():
        last_name = input('Enter last name: ')

    # capitalize first letter of last name
    last_name = last_name.capitalize()

    # VOLUNTEER
    # validate volunteer status
    while not (volunteerinput.lower() == 'y' or volunteerinput.lower() == 'n'):
        volunteerinput = input('Are you a volunteer? (y/n): ')

        if volunteerinput.lower() == "y":
            # validate volunteer areainput
            while not (volunteerarea.isdigit() and int(volunteerarea) in range(1, 4)):

                print(
                    " 1.The pier entrance gate \n 2.the gift shop \n 3.painting and decorating")

                volunteerarea = input("What area are you in? (1-3): ")

        elif volunteerinput.lower() == "n":

            break

    # convert volunteer input to boolean
    if volunteerinput == 'y':
        volunteer = True

    elif volunteerinput == 'n':
        volunteer = False

    # DATE JOINED
    while True:
        try:
            datejoinedinput = input('Enter date joined (DDMMYYYY): ')
            # parse date joined
            datejoined = datetime.strptime(datejoinedinput, '%d%m%Y')
            break
        except:
            print("Please enter a date in the correct format")

    # FEES PAID
    # validate fees paid
    while not (feepaidinput.lower() == 'y' or feepaidinput.lower() == 'n'):
        feepaidinput = input('Have you paid the fee (y/n): ')

    if feepaidinput == 'y':
        feepaid = True
    elif feepaidinput == 'n':
        feepaid = False

    # add new member to the list
    datastructure.append({
        'first_name': first_name,
        'last_name': last_name,
        'isvolunteer': volunteer,
        'volunteerarea': volunteerarea,
        'datejoined': datejoined,
        'isfeepaid': feepaid
    })

while True:
    add_member()

    while True:
        question = input("Would you like to add another? (y/n): ").lower()

        if question == "y":
            break
        elif question == "n":
            break
        else:
            print("Please try to input again")

    if question == "y":
        continue
    elif question == "n":
        break

print(datastructure)