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
              
    def movies_particular_year(self):
       
        #GRAPH 1 - ALL MOVIES IN A PARTICULAR YEAR
        curObj_movie_year = conn.execute("SELECT strftime('%Y',movie_releaseDate),count(movie_title) as Year from movies_metadata group by strftime('%Y',movie_releaseDate)")
        #release_year = []
        #noof_movies_released = []
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
        curObj_revenue_sum = conn.execute("SELECT MM.movie_genre,strftime('%Y',MM.movie_releaseDate) as Year,sum(MR.revenue) as Total_Revenue from movies_metadata MM inner join revenue MR on MM.movie_title=MR.movie_title GROUP BY MM.movie_genre,strftime('%Y',MM.movie_releaseDate) order by MM.movie_genre,strftime('%Y',MM.movie_releaseDate)")
       # sum_revenues_each_genre =[]
       # movies_each_genre = []
       # movie_title_year=[]

        for row in curObj_revenue_sum:
            self.movies_each_genre = self.movies_each_genre + [row[0]]
            self.movie_title_year = self.movie_title_year + [row[1]]
            self.sum_revenues_each_genre = self.sum_revenues_each_genre+ [row[2]]
        print(self.movies_each_genre)
        print(self.sum_revenues_each_genre)
        print(self.movie_title_year)

        self.movies_genre = list(self.movies_each_genre)
        self.sum_revenues = list(self.sum_revenues_each_genre)



        """womenMeans = (movies_genre)
        menMeans = (sum_revenues)
        indices = [movie_title_year]
        #Calculate optimal width
        width = min(diff(indices))/3

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.bar(indices-width,womenMeans,width,color='b',label='-Ymin')
        ax.bar(indices,menMeans,width,color='r',label='Ymax')
        ax.set_xlabel('Bar graph Comparison - Revenue and Movie Genre in a particular year')
        plt.show()"""
        
    def genre_ofmovies_particularyear_comparison(self):
        #GRAPH 3 - GENRE OF MOVIES FOR A PARTICULAR YEAR
        curObj_genre_count = conn.execute("SELECT movie_genre,strftime('%Y',movie_releaseDate) as Year,count(movies_id) from movies_metadata GROUP BY movie_genre,strftime('%Y',movie_releaseDate);")
        self.movie_release_year = []
        self.count_noofmovies_each_genre =[]
        self.movies_each_genre = []
        self.labels = []
        self.sizes = []
        self.row =[]

        for row in curObj_genre_count:
            print("movie_genre",row[0])
            self.movies_each_genre = self.movies_each_genre + [row[0]]
           
            self.movie_release_year = self.movie_release_year  + [row[1]]
            print("movie_release_year",row[1])
            
            self.count_noofmovies_each_genre = self.count_noofmovies_each_genre + [row[2]]
            print("count",row[2])
            
            self.labels = list(self.movies_each_genre)
            self.sizes = list(self.count_noofmovies_each_genre)
            self.row = list(self.movie_release_year)
            
        fig = plt.figure()
        ax1 = fig.add_axes([0, 0, .5, .5], aspect=1)
        ax1.pie(sizes,explode=None, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90, radius = 1.2)
        plt.title(row, bbox={'facecolor':'0.8', 'pad':5})
        ax1.axis('equal')

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

            
"""r = revenue()
r.movies_particular_year()
r.revenues_particular_genre()
r.genre_ofmovies_particularyear_comparison()
r.revenues_particular_year()"""

        



