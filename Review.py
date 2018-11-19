import sqlite3
import pandas as pd
import numpy as np
from IPython.display import display, HTML
from texttable import Texttable
#import matplotlib.pyplot as plt
#import seaborn as sns
#from IPython.display import HTML
class Review:

    global conn
    conn = sqlite3.connect('movie.db')
    
    def __init__(self):

        while True:
            print("Select 1 or 2 from below:")
            viewInput = input("1. Moview Review/Ratings\n2. Compare the reviews")
            if viewInput == "1":
                self.getMovieReview()
            elif viewInput == "2":
                self.getComparison()
            else:
                print("Selection is not from the list")
                cont = input("Do you want to continue[y for yes]?")
                if cont == "y":
                    continue
                else:
                    exit()
                
    def getMovieReview(self):
        t= Texttable()
        movie = input("Please enter the name of the movie: ")
        curObject = conn.cursor()
        #df = pd.read_sql_query("select MM.movie_title, MR.poll_value, MR.comment from movies_metadata MM inner join movies_ratings MR on \MM.movies_id = MR.movies_id where MM.movie_title LIKE '%"+movie+"%'",conn)
        getReviewQuery = curObject.execute("select MM.movie_title, MR.poll_value, MR.comment from movies_metadata MM inner join movies_ratings MR on \
                                        MM.movies_id = MR.movies_id where MM.movie_title LIKE '%"+movie+"%'")
        getReviewResults = getReviewQuery.fetchall()
        print(getReviewResults)
        for i in range(len(getReviewResults)):
                t.add_rows([['movie_title','poll_value','comment'],[getReviewResults[i][0],getReviewResults[i][1],getReviewResults[i][2]]])
        #print(getReviewResults[0][0],getReviewResults[0][1])
        #t.add_rows([['movie_title','poll_value','comment'],[getReviewResultsList[0],getReviewResultsList[1],getReviewResultsList[2]]])
        print(t.draw())
        #print(HTML(df.to_html()))
##        getReviewQuery = curObject.execute("select MM.movie_title, MR.poll_value, MR.comment from movies_metadata MM inner join movies_ratings MR on \
##                                         MM.movies_id = MR.movies_id where MM.movie_title LIKE '%"+movie+"%'")
##        
##        getReviewResults = getReviewQuery.fetchall()
##        df = pd.DataFrame({'MovieTitle': np.linspace(1, 10, 10)})
##        #df = datasets['movies_metadata','movies_ratings']
##        #df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],axis=1)
##        df = pd.concat([df,pd.DataFrame(getReviewResults, columns=['MovieTitle','Poll','Comments'])],axis=1)
##        df.iloc[0, 2] = np.nan
##        df.style
##        print(df.style)
##        print(pd.DataFrame(getReviewResults, columns=['MovieTitle','Poll','Comments']))


    def getComparison(self):
        print("abc")
