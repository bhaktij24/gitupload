## import statements
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from texttable import Texttable

## review class
class Review:

    global conn

    #connect sqlite3
    conn = sqlite3.connect('movie.db')
    
    def __init__(self):

        while True:
            print("Select 1 or 2 from below:")

            #user input to get reviews of one movie or count of all movies w.r.t. genre for last 2 years
            viewInput = input("1. View all the reviews of a particular movie(Tabular display)\n2. Genre based count of movies for last 2 years(Visual display).")
            if viewInput == "1":
                self.getMovieReview()
                break
            elif viewInput == "2":
                self.getComparison()
                break

            #invalid input by user
            else:
                print("Selection is not from the list")
                cont = input("Do you want to continue[y for yes]?")
                if cont == "y":
                    continue
                else:
                    break
    # display all the reviews and ratings for a particular movie           
    def getMovieReview(self):
        t= Texttable()

        #user inputs movie 
        movie = input("Please enter the name of the movie: ")
        curObject = conn.cursor()

        #query to find all the movies with related movie name
        getReviewQuery = curObject.execute("select MM.movie_title, MR.poll_value, MR.comment from movies_metadata MM inner join movies_ratings MR on \
                                        MM.movies_id = MR.movies_id where MM.movie_title LIKE '%"+movie+"%' order by MM.movie_title")
        getReviewResults = getReviewQuery.fetchall()
        for i in range(len(getReviewResults)):
                t.add_rows([['movie_title','poll_value','comment'],[getReviewResults[i][0],getReviewResults[i][1],getReviewResults[i][2]]])
        print(t.draw())

    ## Comparison for count of movies based on genres for latest 2 years
    ## Visually displaying stacked graphs
    def getComparison(self):
        resultRatingsSet = set()
        font = {'family': 'normal','weight': 'bold','size': 5}

        #fetch genres for 2017
        curObject = conn.cursor()
        sqlQuery1 = curObject.execute("SELECT distinct mm1.movie_genre, count(mm2.movies_id) FROM movies_metadata mm1 left join movies_metadata mm2 on \
                                    mm1.movies_id = mm2.movies_id and strftime('%Y',mm1.movie_releaseDate) = '2017' \
                                    group by mm1.movie_genre order by mm1.movie_genre")
        resultRatings1 = sqlQuery1.fetchall()
        
        #fetch genres for 2018
        sqlQuery2 = curObject.execute("SELECT distinct mm1.movie_genre, count(mm2.movies_id) FROM movies_metadata mm1 left join movies_metadata mm2 on \
                                    mm1.movies_id = mm2.movies_id and strftime('%Y',mm1.movie_releaseDate) = '2018'\
                                    group by mm1.movie_genre order by mm1.movie_genre")
        resultRatings2 = sqlQuery2.fetchall()
        sqlQuery3 = curObject.execute("SELECT distinct mm1.movie_genre FROM movies_metadata mm1")
        resultRatings3 = sqlQuery3.fetchall()
        resultRatingsSet = [x[0] for x in resultRatings3]
        resultRatingsSet = sorted(set(resultRatingsSet))
        genre17, count17 = zip(*resultRatings1)
        #print(genre17)
        genre18, count18 = zip(*resultRatings2)
        width = 0.35
        N = len(resultRatings1)
        ind = np.arange(N)
        p1 = plt.bar(ind, count17, width, color='green')
        p2 = plt.bar(ind, count18, width,bottom=count17,color = 'blue')

        plt.ylabel('Count of movies')
        plt.xlabel('Genres')
        plt.title('Comparison based on year and genre')
        plt.xticks(ind, resultRatingsSet)
        plt.yticks(np.arange(0, 10, 1))
        plt.legend((p1[0], p2[0]), ('2017', '2018'))
        plt.show()

if __name__ == "__main__":
    print("Sorry, to access movie reviews module please login with your user credentials to the system.")
    exit()
