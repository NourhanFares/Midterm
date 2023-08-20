#Read one text file and upload all the students into the dictionary of the system:
#solved by th help of: https://www.quora.com/How-do-you-convert-a-text-file-into-a-dictionary-Python-syntax-file-dictionary-object-methods-and-development
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
    'salary': int(salary), 
    'timestamp': timestamp,
  }
count = 0
correct_username = "admin"
correct_pass = "admin123123"
input_username = 0
input_pass = 0

#When admin enters wrong pssword, he will have only  trials otherwise he will be be blocked from entering.
while count < 5 and (correct_pass != input_pass
                     or correct_username != input_username):
  input_username = input("Enter your username: ")
  input_pass = input("Enter your password: ")
  if correct_pass != input_pass or correct_username != input_username:
    count += 1
  if count == 5:
    print("You are out of trials! ")


def admin_menu():
  print("Enter:")
  print("1. Display Statistics")
  print("2. Add an Employee")
  print("3. Display all Employees")
  print("4. Change Employee’s Salary")
  print("5. Remove Employee")
  print("6. Raise Employee’s Salary")
  print("7. Exit")


#when admin logs in correctly, admin menu will be shown
if correct_pass == input_pass or correct_username == input_username:
  admin_menu()

#the system should display how many employees are male and how many are female
males = 0
females = 0


def display_statistics(employees_info):
  males = 0
  females = 0

  for emp_id, data in employees_info.items():

    if data ['gender'] == 'male':
      males += 1
    elif data['gender'] == 'female':
      females += 1
  print("Number of male employees is:", males)
  print("Number of female employees is:", females)




#, the system should allow the admin to add a new employee to the system by specifying the username, gender and the salary only (the employee id is auto-incremented and the date is automatically taken from the computer)

def add_employee(employees_info):
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
        'timestamp': input_date
    }
#print the data:
    print("New Employee Data: ")
    print("new id: " + new_id)
    print("username: " + added_username)
    print("gender: " + added_gender)
    print("input date: " + input_date)
    


#to add the new employee information to the text file: https://pynative.com/python-save-dictionary-to-file/
    new_employee = new_id + ", " + added_username + ", " + input_date + ", " + added_gender + ", " + str(added_salary)
    with open("users.txt", "a") as file:
        file.write(new_employee)
        print('New employee was added successfully to file. ')


#the system should display all the employees registered in the system ordered by date (Today, Yesterday, etc).BY SORTING:





#the system should allow the admin to change the salary ofan employee by specifying his/her Id. The system should prompt the admin for the Employee ID and for the salary. 
def change_salary(employees_info):
  employee_id=input("To change salary, specify employee id: ")
#If the employee is found, then the salary is changed.
  if employee_id in employees_info:
        new_salary=int(input("Add the new salary: "))
        employees_info[employee_id]['salary'] = new_salary
        with open('users.txt', 'w') as file:
          #to add the updated salary to the file: 
          file.write("")
          for id in employees_info:
            values = employees_info[id]
            username = values['username']
            gender = values['gender']
            timestamp = values['timestamp']
            salary = values['salary']
            employee_data= id + ", " + username + ", " + timestamp+ ", " + gender + ", " + str(salary) + "\n"

            with open("users.txt", "a") as file:
             file.write(employee_data)
          
            
        print("Employee salary changed into: " + str(new_salary))
#if id is nor found:
  else:
    print("Invalid ID")




#the system should allow the admin to remove an employee from the system by asking for the ID
def delete_employee(employees_info):
  target_employee=input("Enter the ID of the employee to be deleted: ")
  if target_employee in employees_info: 
    del employees_info[target_employee]
    print('Target Employee have bee deleted successfully')
    with open('users.txt', 'w') as file:
          #to add the updates to the file: 
          file.write("")
          for id in employees_info:
            values = employees_info[id]
            username = values['username']
            gender = values['gender']
            timestamp = values['timestamp']
            salary = values['salary']
            employee_data= id + ", " + username + ", " + timestamp+ ", " + gender + ", " + str(salary) + "\n"

            with open("users.txt", "a") as file:
             file.write(employee_data)

   #if id inserted was not found:
  else:
    print('Target employee is not found, please try again!')


#he system should ask the user for the employee ID
def salary_raise(employees_info):
   id_for_raise = input("Enter the ID of employee who's salary is to be raised: ")
   
 #and the raise percentage
   raise_percent=float(input("Enter percentage for salary raise: "))
   if id_for_raise in employees_info:
     
      if 0 <=raise_percent<= 100 : 
         print("Salary have bee raised "+ str(raise_percent) + '%')
         old_salary= employees_info[id_for_raise]['salary']
         amount_raised= (raise_percent* current_salary)/100
         new_salary= amount_raised+old_salary_salary
         print("New salary for "+ id_for_raise + "is now" + new_salary)
     else:
         print('Invalid Input, please enter an number between 0-100')



    
  
    




  









































#when admin has to choose an option in range 1-7
choice = None
while choice != 7:
  choice = int(input("Enter your choice: "))
  if choice < 1 or choice > 7:
    print("Invalid Option, please try again")
    admin_menu()
  elif choice == 1:
    display_statistics(employees_info)
  elif choice==2:
    add_employee(employees_info)
  elif choice==4:
    change_salary(employees_info)
  elif choice==5:
    delete_employee(employees_info)
  elif choice==6:
    salary_raise(employees_info)
   elif choice==7:
      print("Good bye")
   else:
      print("Wront input")
  
    
