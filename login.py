import sqlite3
import AdminFunction
import UserFunction
import string
import getpass
#import Register

class ConnectDb:
    global conn
    conn = sqlite3.connect('movie.db')
    user = ""
    password = ""
    def __init__(self):
        
        while True:
            print("Select action from below options:\n")
            print("1. Login\n2. Registration")
            selectInput = input("Enter your selection(1/2): ")
            if selectInput == "1":
                self.verifyLogin()
                break
            elif selectInput == "2":
                self.createUser()
                break
            else:
                print("No such functionality available!")
                again = input("Do you want to try again?(y/n):")
                if again.lower() =="n":
                    break
                elif again.lower() =="y":
                    continue
                else:
                    print("No such functionality available!")
                    break

    def verifyLogin(self):
        
        print("Welcome to Movie Analysis")
        while True:
            with sqlite3.connect("movie.db") as db:
                curObject=db.cursor()
            userType = input("Admin/Customer, Enter a/admin for Admin OR c/customer for Customer: ")
            if userType.lower() == "admin" or userType.lower() == "a" or userType.lower() == "customer" or userType.lower() == "c":
                user = input("Enter your account name: ")
                password = getpass.getpass("Password: ")
                loginQuery = curObject.execute("SELECT ID,ROLE FROM MOVIEREVIEW WHERE USERNAME = '"+user+"' AND PASSWORD = '"+password+"'")
                results=loginQuery.fetchone()
                    #print(results[0])
                if results:
                    if results[1].lower() == "admin":
                        print("Welcome "+user+"!")
                        af = AdminFunction.AdminFunction()
                        af.getAdminRoles()
                        break
                    elif results[1].lower() == "end user":
                        print("Welcome "+user+"!")
                        uf = UserFunction.UserFunction(results)
                        #uf.getUserRoles()
                        break
                    else:
                        again = input("Invalid Login credentials. Do you want to try again?(y/n):")
                        if again.lower() =="n":
                            break
                else:
                    print("Please either select admin/customer or a/c for login.")
                    again = input("Do you want to try again?(y/n):")
                    if again.lower() =="n":
                        break               

    def createUser(self):
        while True:
            curObject=conn.cursor()
            user = input("Please enter the user name: ")
            password = input("Enter password: ")
            confirmPass = input("Confirm Password")
            print(user+password+confirmPass)
            if password == confirmPass:
                curObject.execute("insert into MOVIEREVIEW (ID,ROLE,USERNAME,PASSWORD) values (10,'End User','"+user+"','"+password+"')");
                conn.commit();
                print(curObject.rowcount, "record inserted.")    
                loginStatus = input("User creation is successful.Do you want to Login?[y/n]")
                #while True:
                if loginStatus.lower() == "y":
                    self.verifyLogin()
                    break
                else:
                    break
                    
            else:
                tryAgain = input("Passwords do not match! Would you like to try again?[y/n]")
                if tryAgain.lower() == "n":
                    exit()
                    
    def getUserType():
        curObject=conn.cursor()
        loginQuery = curObject.execute("SELECT ID,ROLE FROM MOVIEREVIEW WHERE USERNAME = '"+user+"' AND PASSWORD = '"+password+"'")
        results=loginQuery.fetchone()
        return results

dbase = ConnectDb()

        
