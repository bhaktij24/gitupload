import sqlite3
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import date
from datetime import time
from datetime import datetime

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
   

    def comparison_data_budget_profit(self):
        #GRAPH 1 - COMPARISON GRAPH 1
        year=[]
        Budget = []
        Profit =[]
        curObj_budget_profit = conn.execute("SELECT strftime('%Y',MM.movie_releaseDate) as Year,MR.budget as Total_Budget,MR.profit as Total_Profit from movies_metadata MM inner join revenue MR on MM.movie_title=MR.movie_title")
        for row in curObj_budget_profit:    
            year = year+ [row[0]]
            Budget = Budget + [row[1]] 
            Profit = Profit+ [row[2]]

        df = pd.DataFrame({'MOVIE RELEASE YEAR' : year,
                           'BUDGET ALLOCATED(IN MILLION DOLLARS)':Budget,
                           'PROFIT EARNED(IN MILLION DOLLARS)':Profit})

        pd.options.display.max_columns = None
        print(tabulate(df, headers='keys', tablefmt="orgtbl"))

  
    def genre_movies_performancetrend(self):
        #GRAPH 2 - COMPARISON GRAPH 2
        movie_genre_performingwell=[]
        pollvalue = []
        curObj_genre_performingwell = conn.execute("SELECT MM.movie_genre, MR.poll_value from movies_metadata MM inner join movies_ratings MR on MM.movies_id=MR.movies_id where MR.poll_value>=6.5")
        for row in curObj_genre_performingwell:    
            movie_genre_performingwell = movie_genre_performingwell+ [row[0]]
            pollvalue = pollvalue + [row[1]] 
           
        movie_genre_performingwell =  sorted(list(movie_genre_performingwell))
        pollvalue = sorted(list(pollvalue))

        fig, ax = plt.subplots()
        ax.plot(movie_genre_performingwell, pollvalue)

        ax.set(xlabel='MOVIE GENRE ~ PERFORMING ABOVE OTHER MOVIES', ylabel='IMDB POLL VALUE',
               title='Genre of movies performing well & received maximum good reviews from End Viewers')
        ax.grid()
        plt.show()

    def movies_heavy_criticism(self):
        print("Muvs which faced heavy criticism/was not accepted")
        #GRAPH 3 - COMPARISON GRAPH 3
        movie_genre_performingbad=[]
        pollvalue = []
        curObj_genre_performingbad = conn.execute("SELECT MM.movie_genre, MR.poll_value from movies_metadata MM inner join movies_ratings MR on MM.movies_id=MR.movies_id where MR.poll_value<=6.5")
        for row in curObj_genre_performingbad:    
            movie_genre_performingbad = movie_genre_performingbad + [row[0]]
            pollvalue = pollvalue + [row[1]] 
           
        movie_genre_performingbad =  sorted(list(movie_genre_performingbad))
        pollvalue = sorted(list(pollvalue))

        fig, ax = plt.subplots()
        ax.plot(movie_genre_performingbad, pollvalue)

        ax.set(xlabel='HEAVILY CRITICIZED MOVIES', ylabel='IMDB POLL VALUE',
               title='Genre of movies performing bad & received maximum bad reviews from End Viewers')
        ax.grid()
        plt.show()

    def least_most_preferred_movies(self):
        #GRAPH 4 - COMPARISON GRAPH 4
        movie_genre_poll=[]
        pollvalue = []
        count=[]
        curObj_genre_poll = conn.execute("SELECT MM.movie_genre,case when MR.poll_value<=4 then 'Low' when MR.poll_value>4 and MR.poll_value <=7 then 'Average' else 'High'\
                                         end as 'Poll_Category',count(MM.movies_id) as cnt from movies_metadata MM inner join movies_ratings MR \
                                         on MM.movies_id=MR.movies_id group by MM.movie_genre,Poll_Category")

        for row in curObj_genre_poll:    
            movie_genre_poll = movie_genre_poll + [row[0]]
            pollvalue = pollvalue + [row[1]]
            count=count+[row[2]]

        movie_genre_poll =  sorted(list(movie_genre_poll))
        pollvalue = sorted(list(pollvalue))
        count=sorted(list(count))
        print(movie_genre_poll)
        print(pollvalue)
        print(count)

        N=len(movie_genre_poll)
        x = movie_genre_poll
        y = pollvalue
        s = count
        colors = np.random.rand(N)
        area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

        plt.scatter(x, y, s=area,  c=colors, alpha=0.5, marker=r'$\clubsuit$',
                    label="least and most preferred movies based on IMDB Poll value")
        plt.xlabel("MOVIE GENRE")
        plt.ylabel("POLL VALUE")
        plt.legend(loc='upper left')
        plt.show()


    def noofdays_movies_theatres(self):
        #GRAPH 5 - COMPARISON GRAPH 5
        movies_ran_intheatre=[]
        noofdayssuccessfulrun = []
        curObj_noofdays = conn.execute("SELECT MM.movie_title, MR.noofdayssuccessfulrun from movies_metadata MM inner join movies_ratings MR on MM.movies_id=MR.movies_id")
        for row in curObj_noofdays:    
            movies_ran_intheatre = movies_ran_intheatre + [row[0]]
            noofdayssuccessfulrun = noofdayssuccessfulrun + [row[1]]
            
        movies_ran_intheatre =  sorted(list(movies_ran_intheatre))
        noofdayssuccessfulrun = sorted(list(noofdayssuccessfulrun))

        df = pd.DataFrame({'MOVIES RAN IN THEATRE' : movies_ran_intheatre,
                           'NO OF DAYS OF SUCCESSFUL RUN':noofdayssuccessfulrun})

        pd.options.display.max_columns = None
        print(tabulate(df, headers='keys', tablefmt="orgtbl"))

        plt.scatter(noofdayssuccessfulrun,movies_ran_intheatre,c="green")# A scatter chart

        plt.xlabel('NO OF DAYS OF SUCCESSFUL RUN')
        plt.ylabel('MOVIES RAN IN THEATRE')

        plt.show()



c = comparison()
c.comparison_data_budget_profit()
c.genre_movies_performancetrend()
c.movies_heavy_criticism()
c.least_most_preferred_movies()
c.noofdays_movies_theatres()







        

    
        
