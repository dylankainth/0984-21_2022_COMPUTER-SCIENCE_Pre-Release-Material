# Import Libraries
from datetime import datetime

# Our data structure
datastructure = []
plankdatastructure = []

# Task 3

# A function to ask user for details and add new member to the list
def add_member():

    # declare local variables
    volunteerarea = ''
    datejoined = ''
    datejoinedinput = ''

    # NAMES
    # get first and last names, whilst capitalising the first letters.
    firstName = input('Enter first name: ').capitalize()
    lastName = input('Enter last name: ').capitalize()

    # VOLUNTEER
    while True:
        isVolunteer = input('Are you a volunteer? (y/n): ').lower()
        if isVolunteer == 'n':
            break;
        elif isVolunteer == 'y':
            # volunteer area things
            while True:
                print( " 1.The pier entrance gate \n 2.the gift shop \n 3.painting and decorating")
                volunteerarea = input('Enter volunteer area (1-3): ')

                if volunteerarea == '1' or volunteerarea == '2' or volunteerarea == '3':
                    break;
                else:
                    print('Invalid input, please try again.')
                    continue;
            break;
        else:
            print('Please enter y or n')
            continue;

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
    while True:
        isFeepaid = input('Have you paid the fee (y/n): ')
        if isFeepaid == 'y' or isFeepaid == 'n':
            break;
        else:
            print('Please enter y or n')
            continue;

    # add new member to the list
    datastructure.append({
        'first_name': firstName,
        'last_name': lastName,
        'isvolunteer': isVolunteer,
        'volunteerarea': volunteerarea,
        'datejoined': datejoined,
        'isfeepaid': isFeepaid
    })

    # PLANK SPONSOR
    # validate plank sponsor
    while not (plankinput.lower() == 'y' or plankinput.lower() == 'n'):
        plankinput = input('Would you like to sponsor a plank? (y/n): ')

    if plankinput=='y':
        
        # verify plank sponsor
        while True:
            plankmessage = input('Enter message: ')

            print('your message is: ' + plankmessage)
            plankinput = input('Is this correct? (y/n): ')

            if plankinput.lower() == 'y':
                # add message to plank datastructure
                plankdatastructure.append({'firstname': first_name, 'lastname': last_name, 'message': plankmessage})
                break
            else:
                continue;

    
        plankdatastructure.append({'firstname': first_name, 'lastname': last_name, 'message': plankmessage})


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