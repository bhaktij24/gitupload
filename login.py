import sqlite3
import AdminFunction
import UserFunction
import string
import getpass

class ConnectDb:

    ## connection to database and variables declaration
    global conn
    conn = sqlite3.connect('movie.db')
    user = ""
    password = ""

    ##init method of class ConnectDb
    
    def __init__(self):
        
        while True:
            print("Select action from below options:\n")
            print("1. Login\n2. Registration")
            selectInput = input("Enter your selection(1/2):\n")
            if selectInput == "1":
                self.verifyLogin()
                break
            elif selectInput == "2":
                self.createUser()
                break
            else:
                print("No such functionality available!\n ")
                again = input("Do you want to try again[y]?: ")
                if again.lower() =="y":
                    continue
                else:
                    print("No such functionality available!")
                    break
                
    ## Login verification code for existing user
                
    def verifyLogin(self):
        
        print("Welcome to Movie Analysis")
        while True:
            with sqlite3.connect("movie.db") as db:
                curObject=db.cursor()
            userType = input("Select your User type, Enter a/admin for Admin OR c/customer for Customer: ")
            if userType.lower() == "admin" or userType.lower() == "a" or userType.lower() == "customer" or userType.lower() == "c":
                if userType.lower() == "admin" or userType.lower() == "a":
                    userType = "Admin"
                else:
                    userType = "End User"
                user = input("Enter your user name: ")
                password = getpass.getpass("Password: ")
                
                ## Get results from database
                loginQuery = curObject.execute("SELECT * FROM user_details WHERE USERNAME = '"+user+"' AND PASSWORD = '"+password+"' and ROLE = '"+userType+"'")
                results=loginQuery.fetchone()
                if results != None:
                    
                    ## Compare whether the user is admin or customer and call the respective functions of that class
                    if results[1].lower() == "admin":
                        print("Welcome "+user+"!")
                        af = AdminFunction.AdminFunction()
                        af.getAdminRoles()
                        break
                    else: 
                        print("Welcome "+user+"!")
                        uf = UserFunction.UserFunction(results)
                        break
                else:
                    print("Invalid Username or Password.")
                    again = input("Do you want to try again[y]? : ")
                    if again.lower() =="y":
                        continue
                    else:
                        print("You chose to Exit!")
                        break
            else:
                print("Please select the correct User type")
                    
    ## Registration code for new user                

    def createUser(self):
        
        while True:
            ## Take user input
            
            curObject=conn.cursor()
            user = input("Please enter the user name: ")
            password = input("Enter password: ")
            confirmPass = input("Confirm Password: ")
            
            ## if password matches insert data in database, else ask user to retry
            
            if password == confirmPass:
                curObject.execute("insert into user_details (ROLE,USERNAME,PASSWORD) values ('End User','"+user+"','"+password+"')");
                conn.commit();
                print("Your login is successful!")    
                loginStatus = input("User creation is successful.Do you want to Login?[y]: ")
                if loginStatus.lower() == "y":
                    self.verifyLogin()
                    break
                else:
                    break
                    
            else:
                tryAgain = input("Passwords do not match! Would you like to try again?[y]: ")
                if tryAgain.lower() == "y":
                    continue
                else:
                    exit()
                    
## Create object of class and execute login
if __name__ == "__main__":
    dbase = ConnectDb()


        
