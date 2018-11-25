#Import revenue.py and comparison.py files for ADMIN operations
import sqlite3 #To perform Database operations
import revenue
import Comparison

#Create class AdminFunction
class AdminFunction:

    #Connect to the sqlite3 database movie.db
    def __init__(self):
        conn = sqlite3.connect('movie.db')

    #Admin Functionality and Roles
    def getAdminRoles(self):
        #Admin is asked to enter Revenue/R or C/Comparison to view the various data visualization graphs
        while True:
            print("Welcome to ADMIN Functionalities of Movie Analysis")
            print("---------------Welcome ADMIN------------\n")
            Admin_Task = input("Enter the Comparison Analysis you want to do:\n\
                               1.Revenue based comparison according to movies released and Genres - Enter R/revenue\n\
                               2.Comparison based on budget,profit,liking by end users,preferrance and criticism - Enter C/comparison\n ")
    
            
            #Admin enters Revenue option and is asked to choose one from the 4 different analysis graphs
            if Admin_Task.lower() == "revenue" or Admin_Task.lower() == "r":
                print("Welcome to Revenue based Analysis")
                #Takes input from Admin
                revenue_graph_to_view = input("What kind of graph do you want to view?[y/n]\n\
                                               Enter your Choice:\n\
                                               1.Analysis of All movies released in a year\n\
                                               2.Analysis of Revenue Yielded(In million dollars) for a particular genre of movie\n\
                                               3.Analysis of Genre of movies for a particular year\n\
                                               4.Analysis of Revenue Yielded(In million dollars) for a particular year\n")
                            

                while True:
                    #Creating an object 'my' and accessing the class revenue from revenue.py file
                    my = revenue.revenue()
                    #Admin enters option 1 and chooses to view All movies released in a year
                    if revenue_graph_to_view  == "1":
                        my.movies_particular_year()
                        break
                    
                    #Admin enters option 2 and chooses to view Revenue Yielded(In million dollars) for a particular genre
                    elif revenue_graph_to_view  == "2":
                        my.revenues_particular_genre()
                        break
                    
                    #Admin enters option 3 and chooses to view Genre of movies for a particular year
                    elif revenue_graph_to_view  == "3":
                        my.genre_ofmovies_particularyear_comparison()
                        break
                    
                    #Admin enters option 4 and chooses to view Revenue Yielded(In million dollars) for a particular year
                    elif revenue_graph_to_view  == "4":
                        my.revenues_particular_year()
                        break
                    
                    #Admin enters invalid options
                    else:
                        print("No such action available! Please try to login again for continuation")
                        break
                        return my

            #Admin enters Comparison option and is asked to choose one from the 5 different analysis graphs
            elif Admin_Task.lower() == "comparison" or Admin_Task.lower() == "c":
                #Takes input from Admin
                comparison_graph_to_view = input("What kind of graph do you want to view?[y/n]\n\
                                                  Enter your Choice:\n\
                                                  1.Comparison Analysis of Budget allocated and Profit earned for all movies\n\
                                                  2.Comparison Analysis of Genre of movies that had maximum good reviews and performed well\n\
                                                  3.Comparison Analysis of Genre of movies that had maximum poor reviews and faced heavy criticism by End Users\n\
                                                  4.Comparison Analysis of Least and most Preferred movies for each year\n\
                                                  5.Comparison Analysis of Number of successful days movies ran in theatres\n")

                while True:
                    #Creating an object 'comp' and accessing the class comparison from Comparison.py file
                    comp = Comparison.comparison()

                    #Admin enters option 1 and chooses to view Budget allocated and Profit earned for all movies
                    if comparison_graph_to_view   == "1":
                        comp.comparison_data_budget_profit()
                        break

                    #Admin enters option 2 and chooses to view Genre of movies that had maximum good reviews and performed well
                    elif comparison_graph_to_view   == "2":
                        comp.genre_movies_performancetrend()
                        break

                    #Admin enters option 3 and chooses to view maximum poor reviews and faced heavy criticism by End Users
                    elif comparison_graph_to_view  == "3":
                        comp.movies_heavy_criticism()
                        break

                    #Admin enters option 4 and chooses to view Least and most Preferred movies for each year
                    elif comparison_graph_to_view   == "4":
                        comp.least_most_preferred_movies()
                        break

                    #Admin enters option 5 and chooses to view Number of successful days movies ran in theatres
                    elif  comparison_graph_to_view   == "5":
                        comp.noofdays_movies_theatres()
                        break

                    #Admin enters invalid options
                    else:
                        print("No such action available! Please try to login again for continuation")
                        break
                        return comp

            else:
                print("Admin Function Over,Good bye")
                break





                
                
                
                
  
        
