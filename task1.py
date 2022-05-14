# Task 1 

# Our data structure
dataStructure = []

while True:
    volunteerArea = ""
    dateJoined = ""

    name = input("Enter name: ")

    while True:
        isVolunteer = input("Is the person a volunteer? (y/n): ")
        if isVolunteer == "y":

            while True:
                print("1.Gate  2.Shop  3.Painting")
                volunteerArea = input("Enter volunteer area: ")

                if volunteerArea=="1" or volunteerArea=="2" or volunteerArea=="3":
                    break;
                else:
                    print("Invalid input")
                    continue; 
            
            break;
        elif isVolunteer == "n":
            break;
        else:
            print("Invalid input")
            continue
    
    dateJoined = input("Enter date joined: ")
    #dateJoined = datetime.strptime(dateJoined, '%Y-%m-%d')

    while True:
        isFeepaid = input("Is the person fee paid? (y/n): ")
        if isFeepaid == "y":
            isFeepaid = True
            break;
        elif isFeepaid == "n":
            isFeepaid = False
            break;
        else: 
            print("Invalid input")
            continue;

    dataStructure.append({
        "name": name,
        "isVolunteer": isVolunteer,
        "volunteerArea": volunteerArea,
        "dateJoined": dateJoined,
        "isFeepaid": isFeepaid
    })

    while True:
        addMore = input("Add more? (y/n): ")
        if addMore == "y":
            break;
        elif addMore == "n":
            break;
        else:
            print("Invalid input")
            continue;
        
    if addMore == "n":
        break;
    else:
        continue;