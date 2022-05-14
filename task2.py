# Task 2

# Import Libraries
import datetime

sampledata = [{'name': 'dylan', 'isVolunteer': 'y', 'volunteerArea': '3', 'dateJoined': datetime.datetime(2018, 12, 9, 0, 0), 'isFeepaid': 'y'}]

while True:
    print("Please Select a query")

    print("1. Members who have chosen to work as volunteers.")
    print("2. Volunteers who would like to work at the pier entrance gate.")
    print("3. Volunteers who would like to work in the gift shop.")
    print("4. Volunteers who would like to help with painting and decorating tasks.")
    print("5. Members whose membership has expired (they have not re-joined this year).")
    print("6. Members who have not yet paid their $75 fee.")

    queryinput = input("What is your query? (1-6)? : ")

    try:
        query = int(queryinput)

        if query == 1:
            print("1. Members who have chosen to work as volunteers:")
            for member in sampledata:
                if member["isVolunteer"] == 'y':

                    print(member["name"])

        elif query == 2:
            print("2. Volunteers who would like to work at the pier entrance gate.")
            for member in sampledata:
                if member["volunteerArea"] == '1':
                    print(member["name"])

        elif query == 3:
            print("3. Volunteers who would like to work in the gift shop.")
            for member in sampledata:
                if member["volunteerArea"] == '2':
                    print(member["name"])

        elif query == 4:
            print(
                "4. Volunteers who would like to help with painting and decorating tasks.")
            for member in sampledata:
                if member["volunteerArea"] == '3':
                    print(member["name"])

        elif query == 5:
            print(
                "5. Members whose membership has expired (they have not re-joined this year).")
            for member in sampledata:
                today = datetime.datetime.today()
                oneyearago = today.replace(year=today.year - 1)

                if oneyearago > member['dateJoined']:
                  print(member["name"])

        elif query == 6:
            print("6. Members who have not yet paid their $75 fee.")
            for member in sampledata:
                if member["isFeepaid"] == 'n':
                    print(member["name"])

        else:
            print("Invalid query, please try again")
            continue

        while True:
            question = input("Would you like to make another query? (y/n): ")

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

    except:
        continue
