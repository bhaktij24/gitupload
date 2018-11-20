import sqlite3
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import date
from datetime import time
from datetime import datetime
import pandas as pd
from tabulate import tabulate
import plotly.plotly as py
import plotly.graph_objs as go

class comparison:
    global conn
    conn = sqlite3.connect('movie.db')

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
   

    def comparison_data_budget_profit(self):
        #GRAPH 1 - COMPARISON GRAPH 1
        curObj_budget_profit = conn.execute("SELECT strftime('%Y',MM.movie_releaseDate) as Year,MR.budget as Total_Budget,MR.profit as Total_Profit from movies_metadata MM inner join revenue MR on MM.movie_title=MR.movie_title")
        for row in curObj_budget_profit:    
            self.year = self.year+ [row[0]]
            self.Budget = self.Budget + [row[1]] 
            self.Profit = self.Profit+ [row[2]]

        df = pd.DataFrame({'MOVIE RELEASE YEAR' : self.year,
                           'BUDGET ALLOCATED(IN MILLION DOLLARS)':self.Budget,
                           'PROFIT EARNED(IN MILLION DOLLARS)':self.Profit})

        pd.options.display.max_columns = None
        print(tabulate(df, headers='keys', tablefmt="orgtbl"))

  
    def genre_movies_performancetrend(self):
        #GRAPH 2 - COMPARISON GRAPH 2
        curObj_genre_performingwell = conn.execute("SELECT MM.movie_genre, MR.poll_value from movies_metadata MM inner join movies_ratings MR on MM.movies_id=MR.movies_id where MR.poll_value>=6.5")
        for row in curObj_genre_performingwell:    
            self.movie_genre_performingwell =self.movie_genre_performingwell+ [row[0]]
            self.pollvalue = self.pollvalue + [row[1]] 
           
        self.movie_genre_performingwell =  sorted(list(self.movie_genre_performingwell))
        self.pollvalue = sorted(list(self.pollvalue))

        fig, ax = plt.subplots()
        ax.plot(self.movie_genre_performingwell, self.pollvalue)

        ax.set(xlabel='MOVIE GENRE ~ PERFORMING ABOVE OTHER MOVIES', ylabel='IMDB POLL VALUE',
               title='Genre of movies performing well & received maximum good reviews from End Viewers')
        ax.grid()
        plt.show()

    def movies_heavy_criticism(self):
        #GRAPH 3 - COMPARISON GRAPH 3
        curObj_genre_performingbad = conn.execute("SELECT MM.movie_genre, MR.poll_value from movies_metadata MM inner join movies_ratings MR on MM.movies_id=MR.movies_id where MR.poll_value<=6.5")
        for row in curObj_genre_performingbad:    
            self.movie_genre_performingbad = self.movie_genre_performingbad + [row[0]]
            self.pollvalue = self.pollvalue + [row[1]] 
           
        self.movie_genre_performingbad =  sorted(list(self.movie_genre_performingbad))
        self.pollvalue = sorted(list(self.pollvalue))

        fig, ax = plt.subplots()
        ax.plot(self.movie_genre_performingbad,self.pollvalue)

        ax.set(xlabel='HEAVILY CRITICIZED MOVIES', ylabel='IMDB POLL VALUE',
               title='Genre of movies performing bad & received maximum bad reviews from End Viewers')
        ax.grid()
        plt.show()


    def least_most_preferred_movies(self):
        #GRAPH 4 - COMPARISON GRAPH 4
        curObj_genre_poll = conn.execute("SELECT MM.movie_genre,case when MR.poll_value<=4 then 'Low' when MR.poll_value>4 and MR.poll_value <=7 then 'Average' else 'High'\
                                         end as 'Poll_Category',count(MM.movies_id) as cnt from movies_metadata MM inner join movies_ratings MR \
                                         on MM.movies_id=MR.movies_id group by MM.movie_genre,Poll_Category")

        for row in curObj_genre_poll:    
            self. movie_genre_poll = self.movie_genre_poll + [row[0]]
            self.pollvalue = self.pollvalue + [row[1]]
            self.count=self.count+[row[2]]

        self.movie_genre_poll =  sorted(list(self.movie_genre_poll))
        self.pollvalue = sorted(list(self.pollvalue))
        self.count=sorted(list(self.count))
        print(self.movie_genre_poll)
        print(self.pollvalue)
        print(self.count)
        y_pos = np.arange(len(self.movie_genre_poll))
         
        plt.bar(y_pos, self.pollvalue, align='center', alpha=0.5)
        plt.xticks(y_pos, self.movie_genre_poll)
        plt.xlabel('MOVIE GENRE')
        plt.ylabel('POLL VALUE')
        plt.title('COMPARISON OF LEAST AND MOST PREFERRED MOVIES BASED ON POLL VALUE')
         
        plt.show()

    def noofdays_movies_theatres(self):
        #GRAPH 5 - COMPARISON GRAPH 5
        curObj_noofdays = conn.execute("SELECT MM.movie_title, MR.noofdayssuccessfulrun from movies_metadata MM inner join movies_ratings MR on MM.movies_id=MR.movies_id")
        for row in curObj_noofdays:    
            self.movies_ran_intheatre = self.movies_ran_intheatre + [row[0]]
            self.noofdayssuccessfulrun = self.noofdayssuccessfulrun + [row[1]]
            
        self.movies_ran_intheatre =  sorted(list(self.movies_ran_intheatre))
        self.noofdayssuccessfulrun = sorted(list(self.noofdayssuccessfulrun))

        df = pd.DataFrame({'MOVIES RAN IN THEATRE' : self.movies_ran_intheatre,
                           'NO OF DAYS OF SUCCESSFUL RUN':self.noofdayssuccessfulrun})

        pd.options.display.max_columns = None
        print(tabulate(df, headers='keys', tablefmt="orgtbl"))

        plt.scatter(self.noofdayssuccessfulrun,self.movies_ran_intheatre,c="green")# A scatter chart

        plt.xlabel('NO OF DAYS OF SUCCESSFUL RUN')
        plt.ylabel('MOVIES RAN IN THEATRE')

        plt.show()

"""c = comparison()
#c.comparison_data_budget_profit()
#c.genre_movies_performancetrend()
c.movies_heavy_criticism()
#c.least_most_preferred_movies()
#c.noofdays_movies_theatres()"""











        

    
        
