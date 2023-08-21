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
  
  
ef add_employee(employees_info):
    added_username = input("Enter new username: ")
    added_salary = int(input("Enter new salary: "))
    added_gender = input("Enter new gender: ")

#to increment new id:
    ids = list(employees_info.keys())
    id = ids[len(ids)-1]
    id = id[-3:]
    id = '{:03d}'.format(int(id) + 1)    
    new_id = "emp" + id
#autoincrement date: https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
    input_date = datetime.today().strftime('%Y%m%d')
#add the new employee to the dictionary
    employees_info[new_id] = {
        'username': added_username,
        'gender': added_gender,
        'salary': added_salary,
        'timestamp': input_date                     #Run time: bio O(N) depending on nb of employees
    }
#print the data:
    print("New Employee Data: ")
    print("new id: " + new_id)
    print("username: " + added_username)
    print("gender: " + added_gender)
    print("input date: " + input_date)
    print("Salary: " + str(added_salary))
    


#to add the new employee information to the text file: https://pynative.com/python-save-dictionary-to-file/
    new_employee = new_id + ", " + added_username + ", " + input_date + ", " + added_gender + ", " + str(added_salary) +"\n"
    with open("users.txt", "a") as file:
        file.write(new_employee)
        print('New employee was added successfully to file. ')


#the system should display all the employees registered in the system ordered by date (Today, Yesterday, etc).BY SORTING:
def sorted_employee(employees_info):
#https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
   sorted_employees = sorted( employees_info.items(),key=lambda x: datetime.strptime(x[1]['timestamp'], '%Y%m%d')) 
   reverse=True
   sorted_dict = dict(sorted_employees)
                                                        #Big O(N)
   print(sorted_dict)
   



  
    




  





































  
    
