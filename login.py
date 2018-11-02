import sqlite3
import AdminFunction
import UserFunction
import getpass


class ConnectDb:
    def __init__(self):
        conn = sqlite3.connect('movie.db')
        
    def verifyLogin(self):
        while True:
            
            print("Welcome to Movie Analysis")
            print("Select the user type:\n")
            userType = input("Admin/Customer, Enter a/admin for Admin OR c/customer for Customer: ")
            
            if userType.lower() == "admin" or userType.lower() == "a":
                
                user = input("Enter your account name: ")
                password = getpass.getpass("Password : ")
                with sqlite3.connect("movie.db") as db:
                    curObject = db.cursor()
                    print(curObject)
                loginQuery = curObject.execute("SELECT ROLE FROM MOVIEREVIEW WHERE USERNAME = '"+user+"' AND PASSWORD = '"+password+"'")
                results=loginQuery.fetchone()
                print(results)
                
            elif userType.lower() == "customer" or userType.lower() == "c":
                
                user = input("Enter your account name: ")
                password = getpass.getpass("Password : ")
                
                with sqlite3.connect("movie.db") as db:
                    curObject = db.cursor()
                loginQuery = curObject.execute("SELECT ROLE FROM MOVIEREVIEW WHERE USERNAME = '"+user+"' AND PASSWORD = '"+password+"'")
                results=loginQuery.fetchone()
                print(results)
            else:
                
                print("Either Customer or Admin can only login to the system!")
                exit()

            if len(results) == 0:
                
                print("No such user exits!!")
                again = input("Do you want to try again?(y/n):")
                if again.lower() =="n":
                    exit()
                    
            elif len(results) > 1:
                
                print("Too many results found!!")
                again = input("Do you want to try again?(y/n):")
                if again.lower() =="n":
                    exit()
            else:
                if results[0] == "Admin":
                    print("Welcome "+user+"!")
                    af = AdminFunction.AdminFunction()
                    af.getAdminRoles()
                    return af
                    break
                else:
                    print("Welcome "+user+"!")
                    uf = UserFunction.UserFunction()
                    uf.getUserRoles()
                    return uf
                    break

dbase = ConnectDb()
dbase.verifyLogin()

        
