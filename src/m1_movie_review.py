###############################################################################
# DONE: 1. (3 pts)
#
#   In this module, we are going to create a program that will allow a user to
#   give a review for a movie.
#
#   First, write a function called movie() that will prompt the user to enter
#   a movie title and return the title.
#
#   The function should prompt the user with this prompt:
#
#       "Please enter a movie title: "
#
#   The function should return the string that the user enters as the movie
#   title.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def movie(): 
    title = input("Please enter a movie title: ")
    return title
print(movie())
#####################################################
# DONE: 2. (4 pts)
#
#   Next, write a function called rating() that will prompt the user to enter a
#   rating for the movie and return it as a float.
#
#   The function should prompt the user with this prompt:
#
#       "Please enter a movie rating (1-5): "
#
#   The function should return the rating that the user enters as a float.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def rating(): 
    user_input = input("Please enter a movie rating (1-5): ")
    try: 
        user_rating = float(user_input)
        if 1 <= user_rating <= 5: 
            return user_rating 
        else: 
            print("Please enter a valid rating between 1 and 5.")
            return rating()
    except ValueError: 
        print("Please enter a valid numeric rating.")
        return rating 
print(rating())

###############################################################################
# DONE: 3. (3 pts)
#
#   Now, write a function called review() that will prompt the user to enter a
#   short review of the movie return the review text.
#
#   The function should prompt the user with this prompt:
#
#       "Please enter a brief review: "
#
#   The function should return the string that the user enters as the movie
#   review.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def review(): 
    user_input = input("Please enter a brief review: ")
    return user_input 
print(review())

###############################################################################
# DONE: 4. (7 pts)
#
#   Now, let's put it all together.
#
#   Write a function called main() that does these things in order (make sure
#   you use the functions you defined above and use f-strings in your
#   solution):
#
#       1. Prints "Please write your review below."
#       2. Asks the user for a movie title and save it to a variable.
#       3. Asks the user for a rating and save it to a variable.
#       4. Asks the user for a brief review and save it to a variable.
#       5. Prints the review in a format just like the example below (use
#          f-strings):
#
#           Movie: Mr. Church
#           Rating: 4.5/5
#           Review: This movie has a wonderful story about a cook and is a
#           great adaptation of the short story on which it is based.
#
#   Make sure you call your main() function after you define it.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def main(): 
    print("Please write your moview review below.")
    movie_title = movie() 
    movie_rating = rating()
    movie_review = review() 
    print(f"\nMovie: {movie_title}")
    print(f"Rating: {movie_rating:.1f}/5")
    print(f"Review: {movie_review}")
main()