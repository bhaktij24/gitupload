import sqlite3
import Review

class UserFunction:
    global conn
    conn = sqlite3.connect('movie.db')
    global getRating
    def __init__(self,idRole):
        self.Userid = idRole[0]
        #self.role = idRole[1]
        #user = verifyLogin().userType
        #print("Hello, "+user+"!!\nPlease select your actions from below:")
        userAction = input("1. Add Review/Ratings\n2. View reviews/ratings of a movie\n")
        while True:
            if userAction == "1":
                self.checkReview(self.Userid)
                moreActions = input("Do you still want to continue?[y/n]")
                if moreActions.lower() == "n":
                    break
                else:
                    continue
            elif userAction == "2":
                review = Review.Review()
                review.getReview()
                moreActions = input("Do you still want to continue?[y/n]")
                if moreActions.lower() == "n":
                    break
                else:
                    continue
            else:
                print("No such action available! Please try to login again for continuation")
                break

    def checkReview(self, Userid):
        self.User_Id = Userid
        movieName = input("Please enter the name of the movie:")
        #from login import getUserType
        #userID,userRole = getUserType()
        #if role.lower() == "end user":
        curObject = conn.cursor()
        getName = curObject.execute("select movie_title, movies_id from movies_metadata where movie_title=='"+movieName+"'")
        result = getName.fetchone()
        if result:
           movieRat = curObject.execute("select * from movies_ratings where ID='"+User_Id+"' and movies_id = '"+getName[1]+"'")
           getRating = movieRat.fetchone()
           if getRating:
               print("Below is your previous Review for this movie:\n",getRating[0] + getRating[1] + getRating[2] + getRating[3])
               updateComment = input("Enter any character to update your comment or press 'x' for Exit")
               if updateComment.lower() =="x":
                   return ''
               else:
                  self.addReview()
           else:
                    self.addReview()
        else:
           inc_moviename = input("Incorrect Movie Name. Press 'y' to enter the Movie Name Again, or any other key to exit")
           if inc_moviename.lower() == "y":
              self.checkReview(self.User_Id)
           else:
               exit()              
            
    def addReview(self):
        pollRatingsInput = input("Enter the ratings from 0-9(1 being worst and 9 being excellent):")
        updateComments = input("Please enter your comments, if any")
        if(0 <= float(pollRatingsInput) <= 9):
            curObject = conn.cursor()
            getPoll = curObject.execute("insert into movies_ratings values ('"+getRating[0]+"', '"+getRating[1]+"', '"+float(pollRatingsInput)+"', '"+updateComments+"'");
            conn.commit();
        else:
            inc_poll = input("Incorrect Value. Press 'y' to enter the Movie Name Again, or any other key to exit")
            if inc_poll.lower() == "y":
                self.checkReview()
            else:
                return ''
            
    def getUserRoles(self):
        print("Hello User")
import login
