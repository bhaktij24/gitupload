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
        self.pollcategory =[]
   

    def comparison_data_budget_profit(self):
        #GRAPH 1 - COMPARISON GRAPH 1
        curObj_budget_profit = conn.execute("SELECT strftime('%Y',MM.movie_releaseDate) as Year,MR.budget as Total_Budget,MR.profit as Total_Profit from \
                                             movies_metadata MM inner join revenue MR on MM.movies_id=MR.movies_id")
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
        curObj_genre_performingwell = conn.execute("SELECT MM.movie_genre, MR.poll_value from movies_metadata MM inner join movies_ratings MR on \
                                                    MM.movies_id=MR.movies_id where MR.poll_value>=6.5")
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
        curObj_genre_performingbad = conn.execute("SELECT MM.movie_genre, MR.poll_value from movies_metadata MM inner join movies_ratings MR on \
                                                   MM.movies_id=MR.movies_id where MR.poll_value<=6.5")
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


    def comparisonbasedon_moviegenre_year_ratingsreceived(self):
        #GRAPH 4 - COMPARISON GRAPH 4
        curObject = conn.cursor()
        sqlQuery1 = curObject.execute("select MM.movie_genre,avg(MR.poll_value) from movies_ratings MR inner join  \
                                        movies_metadata MM on MM.movies_id = MR.movies_id where  \
                                        strftime('%Y',MM.movie_releaseDate) = '2017' and MM.movie_genre in('Action','Adventure','Fantasy') group by MM.movie_genre \
                                        order by MM.movie_genre")
        resultRatings1 = sqlQuery1.fetchall()
        print(resultRatings1)
        sqlQuery2 = curObject.execute("select MM.movie_genre,avg(MR.poll_value) from movies_ratings MR inner join  \
                                        movies_metadata MM on MM.movies_id = MR.movies_id where  \
                                        strftime('%Y',MM.movie_releaseDate) = '2018' and MM.movie_genre in('Action','Adventure','Fantasy') group by MM.movie_genre \
                                        order by MM.movie_genre")
        resultRatings2 = sqlQuery2.fetchall()
        print(resultRatings2)
        genre17, ratings17 = zip(*resultRatings1)
        genre18,ratings18 = zip(*resultRatings2)
        print(genre17, ratings17,genre18,ratings18)
        width = 0.35
       
        N = 3
        ind = np.arange(N)
        
        p1 = plt.bar(ind, ratings17, width, color='green')
        p2 = plt.bar(ind, ratings18, width,bottom=ratings17,color = 'blue')
       
        plt.ylabel('avg ratings')
        plt.title('Comparison based on year and genre')
        plt.xticks(ind, ('Action','Adventure','Fantasy'))
        plt.yticks(np.arange(0, 10, 1))
        

        plt.show()


    

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

        pd.options.display.max_columns = None
        print(tabulate(df, headers='keys', tablefmt="orgtbl"))

        plt.scatter(self.noofdayssuccessfulrun,self.movies_ran_intheatre,c="green")# A scatter chart

        plt.xlabel('NO OF DAYS OF SUCCESSFUL RUN')
        plt.ylabel('MOVIES RAN IN THEATRE')

        plt.show()

#c = comparison()
#c.comparison_data_budget_profit()
#c.genre_movies_performancetrend()
#c.movies_heavy_criticism()
#c.comparisonbasedon_moviegenre_year_ratingsreceived()
#c.noofdays_movies_theatres()











        

    
        
