import sqlite3
import revenue
import Comparison

class AdminFunction:

    def __init__(self):
        conn = sqlite3.connect('movie.db')

        
    def getAdminRoles(self):
        while True:
            print("Welcome to ADMIN Functionalities of Movie Analysis")
            print("---------------Welcome ADMIN------------\n")
            Admin_Task = input("Enter the Comparison Analysis you want to do:\n\
                               1.Revenue based comparison according to movies released and Genres - Enter R/revenue\n\
                               2.Comparison based on budget,profit,liking by end users,preferrance and criticism - Enter C/comparison\n\ ")
    
            
            if Admin_Task.lower() == "revenue" or Admin_Task.lower() == "r":
                print("Welcome to Revenue based Analysis")
                revenue_graph_to_view = input("What kind of graph do you want to view?[y/n]\n\
                                               Enter your Choice:\n\
                                               1.Analysis of All movies released in a year\n\
                                               2.Analysis of Revenue Yielded(In million dollars) for a particular genre of movie\n\
                                               3.Analysis of Genre of movies for a particular year\n\
                                               4.Analysis of Revenue Yielded(In million dollars) for a particular year\n")
                            

                while True:
                    my = revenue.revenue()
                    if revenue_graph_to_view  == "1":
                        my.movies_particular_year()
                        break
                    elif revenue_graph_to_view  == "2":
                        my.revenues_particular_genre()
                        break
                    elif revenue_graph_to_view  == "3":
                        my.genre_ofmovies_particularyear_comparison()
                        break
                    elif revenue_graph_to_view  == "4":
                        my.revenues_particular_year()
                        break
                    else:
                        print("No such action available! Please try to login again for continuation")
                        break
                        return my

            elif Admin_Task.lower() == "comparison" or Admin_Task.lower() == "c":
                comparison_graph_to_view = input("What kind of graph do you want to view?[y/n]\n\
                                               Enter your Choice:\n\
                                               1.Comparison Analysis of Budget allocated and Profit earned for all movies\n\
                                               2.Comparison Analysis of Genre of movies that had maximum good reviews and performed well\n \
                                               3.Comparison Analysis of Genre of movies that had maximum poor reviews and faced heavy criticism by End Users\n\
                                               4.Comparison Analysis of Least and most Preferred movies for each year\n\
                                               5.Comparison Analysis of Number of successful days movies ran in theatres\n")

                while True:
                    comp = Comparison.comparison()
                    if comparison_graph_to_view   == "1":
                        comp.comparison_data_budget_profit()
                        break
                    elif comparison_graph_to_view   == "2":
                        comp.genre_movies_performancetrend()
                        break
                    elif comparison_graph_to_view  == "3":
                        comp.movies_heavy_criticism()
                        break
                    elif comparison_graph_to_view   == "4":
                        comp.least_most_preferred_movies()
                        break
                    elif  comparison_graph_to_view   == "5":
                        comp.noofdays_movies_theatres()
                        break
                    else:
                        print("No such action available! Please try to login again for continuation")
                        break
                        return comp

            else:
                print("Admin Function Over,Good bye")
                break





                
                
                
                
  
        
