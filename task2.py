# Import Libraries
import datetime

sampledata = [{'first_name': 'Joe', 'last_name': 'Bloggs', 'isvolunteer': True, 'volunteerarea': '2', 'datejoined': datetime.datetime(2021, 1, 17, 0, 0), 'isfeepaid': False}, {'first_name': 'John', 'last_name': 'Smith', 'isvolunteer': False, 'volunteerarea': '', 'datejoined': datetime.datetime(2021, 2, 10, 0, 0), 'isfeepaid': True}, {'first_name': 'Dom', 'last_name': 'Smith', 'isvolunteer': True, 'volunteerarea': '1', 'datejoined': datetime.datetime(2018, 10, 9, 0, 0), 'isfeepaid': True}, {'first_name': 'Sue', 'last_name': 'Earl', 'isvolunteer': False, 'volunteerarea': '', 'datejoined': datetime.datetime(2012, 12, 10, 0, 0), 'isfeepaid': False}, {'first_name': 'David', 'last_name': 'Xu', 'isvolunteer': True, 'volunteerarea': '3', 'datejoined': datetime.datetime(2022, 1, 16, 0, 0), 'isfeepaid': False}]

while True:
  print("Please Select a query")

  print("---------------------------------")
  print("1. Members who have chosen to work as volunteers.") 
  print("2. Volunteers who would like to work at the pier entrance gate.") 
  print("3. Volunteers who would like to work in the gift shop.")
  print("4. Volunteers who would like to help with painting and decorating tasks.")
  print("5. Members whose membership has expired (they have not re-joined this year).")
  print("6. Members who have not yet paid their $75 fee.")
  print("---------------------------------")

  queryinput = input("What is your query? (1-6)? : ")

  print("---------------------------------")

  try:
    query = int(queryinput)
    
    if query == 1:
      print("1. Members who have chosen to work as volunteers:") 
      for member in sampledata:
        if member["isvolunteer"]:
          
          print(member["first_name"],member["last_name"])

    elif query == 2:
      print("2. Volunteers who would like to work at the pier entrance gate.") 
      for member in sampledata:
        if member["volunteerarea"] == '1':
          print(member["first_name"],member["last_name"])

    elif query == 3:
      print("3. Volunteers who would like to work in the gift shop.")
      for member in sampledata:
        if member["volunteerarea"] == '2':
          print(member["first_name"],member["last_name"])

    elif query == 4:
      print("4. Volunteers who would like to help with painting and decorating tasks.")
      for member in sampledata:
        if member["volunteerarea"] == '3':
          print(member["first_name"],member["last_name"])
      
    elif query == 5:
      print("5. Members whose membership has expired (they have not re-joined this year).")
      for member in sampledata: 
        today = datetime.datetime.today()
        oneyearago = today.replace(year=today.year -1)
        
        
        if oneyearago>member["datejoined"]:
          print(member["first_name"],member["last_name"])

    elif query == 6:
      print("6. Members who have not yet paid their $75 fee.")
      for member in sampledata:
        if member["isFeepaid"]=='n':
          print(member["first_name"],member["last_name"])

    else:

      print("\n \n \n \n \n")
      print("Invalid query, please try again")
      continue
    
    while True:

        print("---------------------------------")

        question = input("Would you like to make another query? (y/n): ").lower()

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
