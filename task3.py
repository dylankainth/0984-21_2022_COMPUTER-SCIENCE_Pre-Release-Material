# Task 3

# Import Libraries
plankdatastructure = []

# would be in task 1
name = input("Enter name: ")

# PLANK SPONSOR
# validate plank sponsor

while True:

    # ... inside the loop in task 1

    isPlankSponsor = input("Is the person a plank sponsor? (y/n): ")
    if isPlankSponsor == "y":
        # verify plank sponsor
        while True:
            plankmessage = input('Enter message: ')

            print('your message is: ' + plankmessage)
            plankinput = input('Is this correct? (y/n): ')

            if plankinput == 'y':
                # add message to plank datastructure
                plankdatastructure.append({'name': name, 'message': plankmessage})
                break
            else:
                continue;

    elif isPlankSponsor == "n":
        break;
    else:
        print("Invalid input")