# Python login simulator

# a dictionary used to store registered users.

userA = {}

# A function to display the menu and ask for the users choice of action...
def action():
 
 print("Welcome to the python simulator program...")
print("Welcome to the python simulator program..")
print("Please choose an option")
print("(a) Login")
print("(b) Register")
print("(c) Exit")
choose = input("Make your choice: ")

# function to validate users login details

def loginn():
 username = input("Enter your username: ")
 passkey = input ("Enter your password: ")
 if username in userA and userA[username] == passkey:
  print("Login successful:")
 else:
  print("Invalid username or password...")


#A function to register new member

def registration():
 username = input ("Register a username: ")
 if username in userA:
  print("This username is not available, or already taken!... ")
 else:
  passkey = input ("Enter a password!... ")
  userA[username] = passkey 
  print("Congratulations Registration successful!... ")

  #Loop

if choose == "a":
        loginn()
elif choose == "b":
        registration()
elif choose == "c":
        print("Thank you for using the program Goodbye!")
        
        
else:
        print("Invalid choice. Please select a, b, or c.")
 
       
      







