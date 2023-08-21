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






    




  





































  
    
