import sqlite3
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import date
from datetime import time
from datetime import datetime
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from tabulate import tabulate

class revenue:
    global conn
    conn = sqlite3.connect('movie.db')

    def __init__(self):
        self.noof_movies_released = []
        self.release_year = []
        self.sum_revenues_each_genre =[]
        self.movies_each_genre = []
        self.year=[]
        self.movie_release_year = []
        self.count_noofmovies_each_genre =[]
        self.movie_title_year=[]
        self.sum_revenues =[]
        self.movies_genre =[]
        self.labells = []
        self.sizes = []
        self.row =[]
        self.p1=[]
        self.p2=[]
                      
    def movies_particular_year(self):
       
        #GRAPH 1 - ALL MOVIES IN A PARTICULAR YEAR
        curObj_movie_year = conn.execute("SELECT strftime('%Y',movie_releaseDate),count(movie_title) as Year from movies_metadata group by strftime('%Y',movie_releaseDate)")
        for row in curObj_movie_year:
            self.release_year = self.release_year + [row[0]]
            self.noof_movies_released = self.noof_movies_released + [row[1]]
            print(self.noof_movies_released)
            print(self.release_year)
        y_pos = np.arange(len(self.release_year))
        plt.bar(y_pos, self.noof_movies_released, align='center', alpha=0.5)
        plt.xticks(y_pos, self.release_year)
        plt.ylabel('Count of Number of Movies')
        plt.xlabel('Movies')
        plt.title('Bar graph Comparison - All movies in a particular year')

        plt.show()

    def revenues_particular_genre(self):
        #GRAPH 2 - ALL REVENUE FOR A PARTICULAR GENRE
        curObj_revenue_sum = conn.execute("SELECT MM.movie_genre,strftime('%Y',MM.movie_releaseDate) as Year,sum(MR.revenue) as Total_Revenue from\
                                        movies_metadata MM inner join revenue MR on MM.movie_title=MR.movie_title GROUP BY MM.movie_genre,\
                                        strftime('%Y',MM.movie_releaseDate) order by MM.movie_genre,strftime('%Y',MM.movie_releaseDate)")
    
        for row in curObj_revenue_sum:
            self.movies_each_genre = self.movies_each_genre + [row[0]]
            self.movie_title_year = self.movie_title_year + [row[1]]
            self.sum_revenues_each_genre = self.sum_revenues_each_genre+ [row[2]]
        print(self.movies_each_genre)
        print(self.sum_revenues_each_genre)
        print(self.movie_title_year)

        self.movies_genre = list(self.movies_each_genre)
        self.sum_revenues = list(self.sum_revenues_each_genre)

        df = pd.DataFrame({'MOVIE GENRE' : self.movies_each_genre,
                            'YEAR RELEASED':self.movie_title_year,
                            'REVENUE YIELDED(IN MILLION DOLLARS)':self.sum_revenues_each_genre})

        pd.options.display.max_columns = None
        print(tabulate(df, headers='keys', tablefmt="orgtbl"))

        #plt.figure();
        #df.plot.hist(stacked=True, bins=20)
        #plt.show()
        
        
    def genre_ofmovies_particularyear_comparison(self):
        #GRAPH 3 - GENRE OF MOVIES FOR A PARTICULAR YEAR
        font = {'family': 'normal','weight': 'bold','size': 5}
        curObj_genre_count_year1 = conn.execute("SELECT MM.movie_genre,count(MM.movies_id) from \
                                           movies_metadata MM where  \
                                           strftime('%Y',MM.movie_releaseDate) = '2017'\
                                           GROUP BY MM.movie_genre,strftime('%Y',MM.movie_releaseDate) order by MM.movie_genre,strftime('%Y',MM.movie_releaseDate);")
        resultRatings1 = curObj_genre_count_year1.fetchall()
        print(resultRatings1)
        
        curObj_genre_count_year2 = conn.execute("SELECT MM.movie_genre,count(MM.movies_id) from \
                                           movies_metadata MM where  \
                                           strftime('%Y',MM.movie_releaseDate) = '2018'\
                                           GROUP BY MM.movie_genre,strftime('%Y',MM.movie_releaseDate) order by MM.movie_genre,strftime('%Y',MM.movie_releaseDate);")
        resultRatings2 = curObj_genre_count_year2.fetchall()
        print(resultRatings2)
        
        genre17, count17 = zip(*resultRatings1)
        genre18,count18 = zip(*resultRatings2)

        # Make figure and axes
        fig, axs = plt.subplots(2,2)


        fig = plt.figure()
        ax1 = fig.add_axes([0, 0, .5, .5], aspect=1)
        ax1.pie(count17,explode=None,labels=genre17, autopct='%1.1f%%',shadow=True, startangle=90, radius = 1.2)
        plt.title(2017, bbox={'facecolor':'0.8', 'pad':5})
        ax1.axis('equal')

        ax2 = fig.add_axes([.5, .0, .5, .5], aspect=1)
        ax2.pie(count18,explode=None,labels=genre18, autopct='%1.1f%%',shadow=True, startangle=90, radius = 1.2)
        plt.title(2018, bbox={'facecolor':'0.8', 'pad':5})
        ax2.axis('equal')
        plt.show()

       
    def revenues_particular_year(self):
#GRAPH 4 - REVENUES FOR A PARTICULAR YEAR
        curObj_revenue_year = conn.execute("SELECT MM.movie_title,strftime('%Y',MM.movie_releaseDate) as Year,sum(MR.revenue) as Total_Revenue from movies_metadata MM inner join revenue MR on MM.movie_title=MR.movie_title GROUP BY MM.movie_genre,strftime('%Y',MM.movie_releaseDate)")
        self.movie_release_year = []
        self.sum_revenues_each_genre =[]
        self.movie_title_year=[]
        self.space = []

        for row in curObj_revenue_year:
            print("movie title",row[0])
            self.movie_title_year=self.movie_title_year + [row[0]]
                
            print("Revenue Yielded: ","$",row[2]," million")
            self.sum_revenues_each_genre = self.sum_revenues_each_genre+ [row[2]]

            print("movie release year",row[1])
            self.movie_release_year = self.movie_release_year +[row[1]]

            df = pd.DataFrame({'MOVIE NAME' : self.movie_title_year,
                               'REVENUE YIELDED(IN MILLION DOLLARS)':self.sum_revenues_each_genre,
                               'YEAR RELEASED':self.movie_release_year})

            pd.options.display.max_columns = None
        print(tabulate(df, headers='keys', tablefmt="orgtbl"))

            
r = revenue()
r.movies_particular_year()
r.revenues_particular_genre()
r.genre_ofmovies_particularyear_comparison()
r.revenues_particular_year()

        



