#Import functions
#Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming languag
#Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.It can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code
#python-tabulate is used for printing readable presentation of mixed textual and numeric data: smart column alignment, configurable number formatting, alignment by adecimal point
#The datetime module supplies classes for manipulating dates and times.class datetime.datetime ==> A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
#Plotly's Python graphing library makes line plots, scatter plots, area charts, bar charts, error bars, box plots, histograms, heatmaps, subplots, multiple-axes, polar charts, and bubble charts.
import sqlite3
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import datetime
from datetime import date
from datetime import time
from datetime import datetime
import pandas as pd #import the pandas library and aliasing as pd
from tabulate import tabulate
import plotly.plotly as py

#Create class comparison
class comparison:
    #Connect to movie.db database and create a connection variable conn which can be used inside all methods.
    global conn
    conn = sqlite3.connect('movie.db')

    #Declare the required variables to be used
    def __init__(self):
        self.year=[]
        self.Budget = []
        self.Profit =[]
        self.movie_genre_performingwell=[]
        self.pollvalue = []
        self.movie_genre_performingbad=[]
        self.movies_ran_intheatre=[]
        self.noofdayssuccessfulrun= []
        self. movie_genre_poll = []
        self.count = []
        self.pollcategory =[]
   

    # comparison_data_budget_profit() compares the budget allocated and profit earned for movies
    def comparison_data_budget_profit(self):
        #GRAPH 1 - COMPARISON GRAPH 1
        #create a Cursor object and call its execute() method to perform SQL SELECT command
        curObj_budget_profit = conn.execute("SELECT strftime('%Y',MM.movie_releaseDate) as Year,MR.budget as Total_Budget,MR.profit as Total_Profit from \
                                             movies_metadata MM inner join revenue MR on MM.movies_id=MR.movies_id")
        
        #To retrieve data after executing a SELECT statement, treat the cursor as an iterator
        for row in curObj_budget_profit:    
            self.year = self.year+ [row[0]]
            self.Budget = self.Budget + [row[1]] 
            self.Profit = self.Profit+ [row[2]]

        #A Data frame is a two-dimensional data structure i.e., data is aligned in a tabular fashion in rows and columns
        df = pd.DataFrame({'MOVIE RELEASE YEAR' : self.year,
                           'BUDGET ALLOCATED(IN MILLION DOLLARS)':self.Budget,
                           'PROFIT EARNED(IN MILLION DOLLARS)':self.Profit})

        pd.options.display.max_columns = None
        #Display data in a tabular form
        print(tabulate(df, headers='keys', tablefmt="orgtbl"))

  
    # genre_movies_performancetrend() compares the movie genres that are performing well with respect to their poll value (IMDB Poll value above 6.5)
    def genre_movies_performancetrend(self):
        #GRAPH 2 - COMPARISON GRAPH 2
        #SQL Command to extract movie genres with poll value> 6.5
        curObj_genre_performingwell = conn.execute("SELECT MM.movie_genre, MR.poll_value from movies_metadata MM inner join movies_ratings MR on \
                                                    MM.movies_id=MR.movies_id where MR.poll_value>6.5")

        #Treat the cursor object as an iterator and putting the retrieved data into list variables
        for row in curObj_genre_performingwell:    
            self.movie_genre_performingwell =self.movie_genre_performingwell+ [row[0]]
            self.pollvalue = self.pollvalue + [row[1]] 
           
        #The sorted() method sorts the elements of a given iterable in a specific order - Ascending or Descending.
        self.movie_genre_performingwell =  sorted(list(self.movie_genre_performingwell))
        self.pollvalue = sorted(list(self.pollvalue))

        fig, ax = plt.subplots()
        #Display Line Plot
        ax.plot(self.movie_genre_performingwell, self.pollvalue)

        #Set X Axis as MOVIE GENRE and y Axis as IMDB POLL VALUE and title of the graph
        ax.set(xlabel='MOVIE GENRE ~ PERFORMING ABOVE OTHER MOVIES', ylabel='IMDB POLL VALUE',
               title='Genre of movies performing well & received maximum good reviews from End Viewers')
        ax.grid()
        #Displays the graph
        plt.show()
        
    #movies_heavy_criticism() compares the movie genres that are performing bad with respect to their poll value (IMDB Poll value <= 6.5)
    def movies_heavy_criticism(self):
        #GRAPH 3 - COMPARISON GRAPH 3
        #SQL Command to extract movie genres with poll value<= 6.5
        curObj_genre_performingbad = conn.execute("SELECT MM.movie_genre, MR.poll_value from movies_metadata MM inner join movies_ratings MR on \
                                                   MM.movies_id=MR.movies_id where MR.poll_value<=6.5")

        #Treat the cursor object as an iterator and putting the retrieved data into list variables
        for row in curObj_genre_performingbad:    
            self.movie_genre_performingbad = self.movie_genre_performingbad + [row[0]]
            self.pollvalue = self.pollvalue + [row[1]] 
           
        #The sorted() method sorts the elements of a given iterable in a specific order - Ascending or Descending.
        self.movie_genre_performingbad =  sorted(list(self.movie_genre_performingbad))
        self.pollvalue = sorted(list(self.pollvalue))

        fig, ax = plt.subplots()
        #Display Line Plot
        ax.plot(self.movie_genre_performingbad,self.pollvalue)

        ax.set(xlabel='HEAVILY CRITICIZED MOVIES', ylabel='IMDB POLL VALUE',
               title='Genre of movies performing bad & received maximum bad reviews from End Viewers')
        ax.grid()
        plt.show()


    #least_most_preferred_movies() categorizes movies with poll value<=5.8 as BAD ,poll_value>5.8 and poll_value<=7 as DECENT and poll value >7 as GREAT
    def least_most_preferred_movies(self):
        #GRAPH 4 - COMPARISON GRAPH 4
        curObj_genre_poll = conn.execute("SELECT case when MR.poll_value<=5.8 then 'Bad' when MR.poll_value>5.8 and MR.poll_value <=7 then 'Decent' else 'Great'\
                                         end as 'Poll_Category',count(MM.movies_id) as cnt from movies_metadata MM inner join movies_ratings MR \
                                         on MM.movies_id=MR.movies_id group by Poll_Category")

        #Treat the cursor object as an iterator and putting the retrieved data into list variables pollcategory and count
        for row in curObj_genre_poll:    
            self.pollcategory=self.pollcategory+[row[0]]
            self.count=self.count+[row[1]]
        self.pollcategory=(list(self.pollcategory))
        self.count =(list(self.count))
        print(self.pollcategory)
        print(self.count)
         
        #Display Line Plot
        plt.plot(self.pollcategory, self.count, linewidth=2.0)
              
        #Set X Axis as POLL CATEGORY and Y Axis as COUNT
        plt.xlabel('POLL CATEGORY')
        plt.ylabel('COUNT')
        plt.title('COMPARISON OF LEAST AND MOST PREFERRED MOVIES BASED ON POLL VALUE')
        plt.show()
         

    #noofdays_movies_theatres() compares movies and number of days successful run in theatres
    def noofdays_movies_theatres(self):
        #GRAPH 5 - COMPARISON GRAPH 5
        curObj_noofdays = conn.execute("SELECT MM.movie_title, MR.noofdayssuccessfulrun from movies_metadata MM inner join movies_ratings MR on \
                                        MM.movies_id=MR.movies_id")
        for row in curObj_noofdays:    
            self.movies_ran_intheatre = self.movies_ran_intheatre + [row[0]]
            self.noofdayssuccessfulrun = self.noofdayssuccessfulrun + [row[1]]
            
        self.movies_ran_intheatre =  sorted(list(self.movies_ran_intheatre))
        self.noofdayssuccessfulrun = sorted(list(self.noofdayssuccessfulrun))

        df = pd.DataFrame({'MOVIES RAN IN THEATRE' : self.movies_ran_intheatre,
                           'NO OF DAYS OF SUCCESSFUL RUN':self.noofdayssuccessfulrun})

        #Displays data in tabular form 
        pd.options.display.max_columns = None
        print(tabulate(df, headers='keys', tablefmt="orgtbl"))

        #Display Scatter Plot chart for the data analysed
        plt.scatter(self.noofdayssuccessfulrun,self.movies_ran_intheatre,c="green")# A scatter chart

        #Set X Axis as NO OF DAYS OF SUCCESSFUL RUN and Y Axis as MOVIES RAN IN THEATRE 
        plt.xlabel('NO OF DAYS OF SUCCESSFUL RUN')
        plt.ylabel('MOVIES RAN IN THEATRE')

        plt.show()













        

    
        
