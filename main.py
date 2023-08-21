from datetime import datetime

users_file = open("users.txt", "r")
lines = users_file.readlines()
#create an empty dict :
employees_info = {}
for line in lines:
   user_id, username, timestamp, gender, salary = line.strip().split(', ')
   employees_info[user_id] = {
    'username': username,
    'gender': gender,
    'salary': float(salary), 
    'timestamp': timestamp,
  }
  #rune time: bio o(N) where n is lines number 
count = 0
correct_username = "admin"
correct_pass = "admin123123"
input_username = 0
input_pass = 0


def admin_menu():
  print("Enter:")
  print("1. Display Statistics")
  print("2. Add an Employee")
  print("3. Display all Employees")
  print("4. Change Employee’s Salary")
  print("5. Remove Employee")                           #run time o(1)
  print("6. Raise Employee’s Salary")
  print("7. Exit")

males = 0
females = 0


def display_statistics(employees_info):
  males = 0
  females = 0

  for emp_id, data in employees_info.items():
                                                        #run time: o(N) n is nb of employees
    if data ['gender'] == 'male':
      males += 1
    elif data['gender'] == 'female':
      females += 1
  print("Number of male employees is:", males)
  print("Number of female employees is:", females)



  
    




  





































  
    
