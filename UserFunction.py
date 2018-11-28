## import statements
import sqlite3
import Review
import string

## Class for user functionalities
class UserFunction:
    global conn

    #connect sqlite3
    conn = sqlite3.connect('movie.db')
    global getRating

    #init function of user module
    def __init__(self,idRole):

        #fetch userid from login module
        self.Userid = idRole[0]

        while True:

            #Takes user's input
            userAction = input("1. Add Review/Ratings\n2. View reviews/ratings of a movie\n")

            #compare the input with string.digits
            if userAction in string.digits:

                if userAction == "1":

                    # fetch movie reviews for the user and allow the user to input/update reviews
                    self.checkReview(self.Userid)
                    moreActions = input("Do you still want to continue?[y]: ")
                    if moreActions.lower() == "y":
                        continue
                    else:
                        break

                elif userAction == "2":

                    # fetch movie reviews in visually attracted format(graph or tabular forms)
                    review = Review.Review()
                    moreActions = input("Do you still want to continue?[y]: ")
                    if moreActions.lower() == "y":
                        continue
                    else:
                        break

                #Invalid user input
                else:
                    print("No such action available! Please login again to enter the correct input.")
                    break
                
            #condition to verify special characters
            else:
                print("Special characters or alphabets are not for input.")
                continue

    # fetching movie reviews
    def checkReview(self, Userid):

        User_Id = str(self.Userid)

        
        while True:

            #get the movie name
            movieName = input("Please enter the name of the movie:")
            curObject = conn.cursor()

            #database query to find the movie
            getName = curObject.execute("select movie_title, CAST(movies_id as VARCHAR) as movies_id from movies_metadata where movie_title like '%"+movieName+"%'")
            result = getName.fetchone()

            #check for empty records
            if result != None:
                
                print("The movie found with the given input is:",result[0])

                #get the expected movie name
                answer = input("If the movie listed is as expected, press 'y' to continue, any other key to exit: ")
                if answer.lower() == 'y':
                    if result:

                       #query to find movie review/ratings exist for that user
                       movieRat = curObject.execute("select CAST(ID as VARCHAR) as ID, CAST(movies_id as VARCHAR) as movies_id,poll_value,comment \
                                            from movies_ratings where ID= "+User_Id+" and movies_id = "+result[1]+"")
                       getRating = movieRat.fetchone()
                       
                       #if query result returns a row call the updateReview function
                       if getRating != None:
                           print("Below is your previous ratings and review for this movie:\n",getRating[2] +" "+ getRating[3])
                           updateComment = input("Enter any character to update your comment or press 'x' for Exit")
                           if updateComment.lower() =="x":
                               return ''
                           else:
                              self.updateReview(getRating)
                              break

                       #if query result returns a None call the addReview function
                       else:
                           getRating = (int(User_Id),int(result[1]))
                           self.addReview(getRating)
                           break

                    #movie does not exist in database
                    else:
                        
                       inc_moviename = input("Incorrect Movie Name. Press 'y' to enter the Movie Name Again, or any other key to exit")

                       #user input to continue(call again checkReview function)/exit
                       if inc_moviename.lower() == "y":
                          self.checkReview(self.User_Id)
                       else:
                           break
                else:
                    break

            #if movie name does not match the one in the database
            else:
                 answer = input("No such movie found! Press 'y' to continue, any other key to exit")
                 if answer.lower() == "y":
                     continue
                 else:
                     break
            
    # add review function, in case the review for that user does not exist           
    def addReview(self,userRating):
        while True:

            #user input for ratings between 0-9
            pollRatingsInput = input("Enter the ratings from 0-9(1 being worst and 9 being excellent): ")

            #compare the user input with string.digits
            if pollRatingsInput not in string.digits:
                    print("Ratings should be only a numeric value between 0-9")
                    answer = input("Press 'y' to try again, any other key to exit: ")
                    if answer.lower() == "y":
                        continue
                    else:
                        break

            #user inputs the reviews for movie
            updateComments = input("Please enter your comments, if any")
            pollRatingsInput = str(pollRatingsInput)
            updateComments = str(updateComments)

            # prints the user input for confirmation
            print("Your poll rating for the movie: "+pollRatingsInput+"\nYour Comments for the movie: "+updateComments)

            #compare the ratings between 0-9 and add the ratings/reviews to database
            if(0 <= float(pollRatingsInput) <= 9):
                curObject = conn.cursor()            
                getPoll = curObject.execute("insert into movies_ratings(ID,movies_id,poll_value,comment) values(?,?,?,?);",(userRating[0],userRating[1],pollRatingsInput,updateComments))    
                conn.commit();
                print("Thanks for sharing your views.")
                break

            #incorrect ratings
            else:
                inc_poll = input("Incorrect Value Press 'y' to enter the Movie Name Again, or any other key to exit")
                if inc_poll.lower() == "y":
                    self.checkReview()
                else:
                    break


    #if reviews already exist and user wants to change
    def updateReview(self,userRating):

        while True:

            #enter the ratings
            pollRatingsInput = input("Enter the ratings from 0-9(1 being worst and 9 being excellent): ")

            #compare it with string.didits
            if pollRatingsInput not in string.digits:
                print("Ratings should be only a numeric value between 0-9")
                answer = input("Press 'y' to try again, any other key to exit: ")
                if answer.lower() == "y":
                    continue
                else:
                    break

            # enter comments if needed
            updateComments = input("Please enter your comments, if any: ")
            pollRatingsInput = str(pollRatingsInput)
            updateComments = str(updateComments)

            # prints the user input for confirmation
            print("Your poll rating for the movie: "+pollRatingsInput+"\nYour Comments for the movie: "+updateComments)

            #validate the ratings between 0-9
            if(0 <= float(pollRatingsInput) <= 9):
                curObject = conn.cursor()

                #update ratings/reviews query
                getPoll = curObject.execute("update movies_ratings set poll_value= '"+pollRatingsInput+"', comment = '"+updateComments+"' where \
                                            ID= "+userRating[0]+" and movies_id = "+userRating[1]+"")   
                conn.commit();
                print("Thanks for sharing your views.")
                break

            #condition for incorrect ratings
            else:
                inc_poll = input("Incorrect Value Press 'y' to enter the movie name again, or any other key to exit: ")
                if inc_poll.lower() == "y":
                    self.checkReview()
                else:
                    break

import login

if __name__ == "__main__":
    print("Sorry, to access movie reviews module please login with your user credentials to the system.")
    exit()
