import sqlite3
import revenue
import Comparison

class AdminFunction:

    def __init__(self):
        conn = sqlite3.connect('movie.db')

    def getAdminRoles(self):
        while True:
            print("Welcome to ADMIN Functionalities of Movie Analysis")
            print("---------------Welcome Scott------------\n")
            Admin_Task = input("Enter the Comparison Analysis you want to do:\
                               1.Revenue based comparison according to movies released and Genres - Enter R/revenue\
                               2.Comparison based on budget,profit,liking by end users,preferrance and criticism - Enter C/comparison\ ")
            
            if Admin_Task.lower() == "revenue" or Admin_Task.lower() == "r":
                my = revenue.revenue()
                my.movies_particular_year()
                my.revenues_particular_genre()
                my.genre_ofmovies_particularyear_comparison()
                my.revenues_particular_year()
                return my

            elif Admin_Task.lower() == "comparison" or Admin_Task.lower() == "c":
                comp = Comparison.comparison()
                comp.comparison_data_budget_profit()
                comp.genre_movies_performancetrend()
                comp.movies_heavy_criticism()
                comp.least_most_preferred_movies()
                comp.noofdays_movies_theatres()
                return comp

            else:
                print("Admin Function Over,Good bye")
                break





                
                
                
                
  
        
