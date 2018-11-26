#Import functions
#Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming languag
#Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.It can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code
#python-tabulate is used for printing readable presentation of mixed textual and numeric data: smart column alignment, configurable number formatting, alignment by adecimal point
#The datetime module supplies classes for manipulating dates and times.class datetime.datetime ==> A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
#Plotly's Python graphing library makes line plots, scatter plots, area charts, bar charts, error bars, box plots, histograms, heatmaps, subplots, multiple-axes, polar charts, and bubble charts.
import sqlite3
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import date
from datetime import time
from datetime import datetime
import plotly.plotly as py
import pandas as pd
from tabulate import tabulate

#Create class revenue
class revenue:
    #Connect to movie.db database and create a connection variable conn which can be used inside all methods.
    global conn
    conn = sqlite3.connect('movie.db')

    #Declare the required variables to be used
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

                      
    #movies_particular_year() compares the number of movies released in a particular year
    def movies_particular_year(self):
       
        #GRAPH 1 - ALL MOVIES IN A PARTICULAR YEAR
        #strftime('%Y',movie_releaseDate) extracts the year alone from the movie releasedate column from movies_metadata table
        curObj_movie_year = conn.execute("SELECT strftime('%Y',movie_releaseDate),count(movie_title) as Year from movies_metadata group by\
                                         strftime('%Y',movie_releaseDate)")
        
        #To retrieve data after executing a SELECT statement, treat the cursor as an iterator and store the retrieved data in list variables release_year and noof_movies_released
        for row in curObj_movie_year:
            self.release_year = self.release_year + [row[0]]
            self.noof_movies_released = self.noof_movies_released + [row[1]]

        #len() returns the length of the string        
        y_pos = np.arange(len(self.release_year))

        #plt.bar makes a bar plot with X Axis as Movies and Y Axis as Count of Number of Movies
        plt.bar(y_pos, self.noof_movies_released, align='center', alpha=0.5)
        plt.xticks(y_pos, self.release_year)
        
        #To Set tables for X and Y Axis and title for the graph
        plt.ylabel('Count of Number of Movies')
        plt.xlabel('Movies')
        plt.title('Bar graph Comparison - All movies in a particular year')

        #Displays the graph
        plt.show()
        
    #revenues_particular_genre compares all the revenues for a particular genre
    def revenues_particular_genre(self):
        #GRAPH 2 - ALL REVENUE FOR A PARTICULAR GENRE
        curObj_revenue_sum = conn.execute("SELECT MM.movie_genre,strftime('%Y',MM.movie_releaseDate) as Year,sum(MR.revenue) as Total_Revenue from\
                                        movies_metadata MM inner join revenue MR on MM.movies_id=MR.movies_id GROUP BY MM.movie_genre,\
                                        strftime('%Y',MM.movie_releaseDate) order by MM.movie_genre,strftime('%Y',MM.movie_releaseDate)")
    
        for row in curObj_revenue_sum:
            self.movies_each_genre = self.movies_each_genre + [row[0]]
            self.movie_title_year = self.movie_title_year + [row[1]]
            self.sum_revenues_each_genre = self.sum_revenues_each_genre+ [row[2]]

        self.movies_genre = list(self.movies_each_genre)
        self.sum_revenues = list(self.sum_revenues_each_genre)

        #A Data frame is a two-dimensional data structure i.e., data is aligned in a tabular fashion in rows and columns
        df = pd.DataFrame({'MOVIE GENRE' : self.movies_each_genre,
                            'YEAR RELEASED':self.movie_title_year,
                            'REVENUE YIELDED(IN MILLION DOLLARS)':self.sum_revenues_each_genre})
        
        #Display data in a tabular form without any truncation
        pd.options.display.max_columns = None
        print(tabulate(df, headers='keys', tablefmt="orgtbl"))
        
    #genre_ofmovies_particularyear_comparison() compares the genre of movies in a particular year
    def genre_ofmovies_particularyear_comparison(self):
        #GRAPH 3 - GENRE OF MOVIES FOR A PARTICULAR YEAR
        #create a Cursor object and call its execute() method to perform SQL SELECT command
        font = {'family': 'normal','weight': 'bold','size': 5}
        curObj_genre_count_year1 = conn.execute("SELECT MM.movie_genre,count(MM.movies_id) from \
                                           movies_metadata MM where  \
                                           strftime('%Y',MM.movie_releaseDate) = '2017'\
                                           GROUP BY MM.movie_genre,strftime('%Y',MM.movie_releaseDate) order by MM.movie_genre,strftime('%Y',MM.movie_releaseDate);")

        #To retrieve data after executing a SELECT statement,call fetchall() to get a list of the matching rows
        resultRatings1 = curObj_genre_count_year1.fetchall()
        
        curObj_genre_count_year2 = conn.execute("SELECT MM.movie_genre,count(MM.movies_id) from \
                                           movies_metadata MM where  \
                                           strftime('%Y',MM.movie_releaseDate) = '2018'\
                                           GROUP BY MM.movie_genre,strftime('%Y',MM.movie_releaseDate) order by MM.movie_genre,strftime('%Y',MM.movie_releaseDate);")
        resultRatings2 = curObj_genre_count_year2.fetchall()
        
        #The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc
        genre17, count17 = zip(*resultRatings1)
        genre18,count18 = zip(*resultRatings2)

        fig = plt.figure()
        ax1 = fig.add_axes([0, 0, .5, .5], aspect=1)
        #Plot a pie chart where the slices will be ordered and plotted counter-clockwise
        #First parameter sets The wedge sizes.labels - A sequence of strings providing the labels for each wedge
        # shadow : Draw a shadow beneath the pie.
        # autopct : None (default), string, or function, optional.If not None, is a string or function used to label the wedges with their numeric value.
        # startangle = 90 such that everything is rotated counter-clockwise by 90 degrees,radius sets the radius of the pie
        ax1.pie(count17,explode=None,labels=genre17, autopct='%1.1f%%',shadow=True, startangle=90, radius = 1.2)
        plt.title(2017, bbox={'facecolor':'0.8', 'pad':5})
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')

        # add_axes produces two pie charts side by side
        ax2 = fig.add_axes([.5, .0, .5, .5], aspect=1) # add_axes parameters => left, bottom, width, height (range 0 to 1)
        ax2.pie(count18,explode=None,labels=genre18, autopct='%1.1f%%',shadow=True, startangle=90, radius = 1.2)
        #Sets title of the graph
        plt.title(2018, bbox={'facecolor':'0.8', 'pad':5})
        ax2.axis('equal')
        plt.show()

    #revenues_particular_year() compares the revenues for a particular year
    def revenues_particular_year(self):
        #GRAPH 4 - REVENUES FOR A PARTICULAR YEAR
        #Extracts movie title,release year and sum of revenues from database
        curObj_revenue_year = conn.execute("SELECT MM.movie_title,strftime('%Y',MM.movie_releaseDate) as Year,sum(MR.revenue) as Total_Revenue from \
                                            movies_metadata MM inner join revenue MR on MM.movies_id=MR.movies_id GROUP BY MM.movie_genre,\
                                            strftime('%Y',MM.movie_releaseDate)")
        
        for row in curObj_revenue_year:
            self.movie_title_year=self.movie_title_year + [row[0]]
            self.movie_release_year = self.movie_release_year +[row[1]]
            self.sum_revenues_each_genre = self.sum_revenues_each_genre+ [row[2]]

            df = pd.DataFrame({'MOVIE NAME' : self.movie_title_year,
                               'REVENUE YIELDED(IN MILLION DOLLARS)':self.sum_revenues_each_genre,
                               'YEAR RELEASED':self.movie_release_year})

        #Displays data in tabular form
            pd.options.display.max_columns = None
        print(tabulate(df, headers='keys', tablefmt="orgtbl"))

            


        



