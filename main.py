import zmq
import json

def main():

    # Intialize list datastructure
    movies_list = []

    print("\n")
    print("*** Welcome to Movie Hub ***")
    print("Save all of your favorite movies in one place!")

    user_input = 0
    while user_input != 7:

        print("\nCOMMANDS:")
        print("1) Type '1' to add a movie")
        print("2) Type '2' to lookup a movie")
        print("3) Type '3' to view all movies")
        print("4) Type '4' to acess movie reminder services")
        print("5) Type '5' to get an AI movie recommendation")
        print("6) Type '6' to view the most trending movies")
        print("7) Type '7' for help on how to use this program")
        print("8) Type '8' to quit")

        user_input = int(input("\nSelect command: "))

        if user_input == 1:
            print("Adding a movie ...\n")

            adding_method = int(input("Would you like to add the movie manually (1) or by the IMDb id (2) ? 1/2?: "))

            if adding_method == 1:
                correct_details = "N"
                while correct_details != "Y":
                    movieName = input("Enter the name of the movie > ")
                    directorName = input("Enter the name of the director > ")
                    releaseYear = input("Enter the year the movie was released > ")
                    movieGenre = input("Enter the movie genre > ")
                    print("\n")
                    print(f"Movie Name: {movieName}, Directors: {directorName}, Release Year: {releaseYear}, Genre: {movieGenre}")
                    correct_details = input("Are the movie details correct? (Y/N): ")

                movies_list.append([movieName, directorName, releaseYear, movieGenre])
                print(f"{movieName} has successfully been added to your catalog!")

            elif adding_method == 2:
                imdb_id = input("Please enter the IMDb movie id: ")
                context = zmq.Context()
                print("\nClient attempting to connect to IMDb ID Search Microservice...")
                socket = context.socket(zmq.REQ)
                socket.connect("tcp://localhost:5561") 

                print(f"Sending a request to the IMDB ID Search Microservice for IMDb id: {imdb_id}.")
                socket.send_string(imdb_id)

                imdb_response = socket.recv_json()
                movieName = imdb_response.get('movie_name')
                directorName = imdb_response.get('directors')
                releaseYear = imdb_response.get('release_year')
                movieGenre = imdb_response.get('genre')

                print(f"Movie Name: {movieName}, Directors: {directorName}, Release Year: {releaseYear}, Genre: {movieGenre}")
                correct_details = input("\nAre the movie details correct? (Y/N): ")

                if correct_details == "Y":
                    movies_list.append([movieName, directorName, releaseYear, movieGenre])
                    print(f"{movieName} has successfully been added to your catalog!")
                elif correct_details == "N":
                    print("Please try adding the movie manually")

        elif user_input == 2:
            print("Looking up a movie ...\n")
            if len(movies_list) == 0:
                print("You currently have no movies saved to your catalog. Please add a movie first by selecting the add movie option.")
            else:
                movie_lookup_name = input("Enter the movie title you want to lookup: ")
                for movie in movies_list:
                    if movie_lookup_name in movie:
                        print("\n")
                        print(f"Movie Name: {movie[0]}, Directors: {movie[1]}, Release Year: {movie[2]}, Genre: {movie[3]}")

                        print("\nCOMMANDS:")
                        print("1) Type '1' to delete a movie")
                        print("2) Type '2' to return back to the home page")
                        delete_request = int(input("\nSelect command: "))

                        if delete_request == 1:
                            print(f"Are you sure you want to delete {movie[0]} from your catalog?")
                            print("NOTE: Be aware that by confirming this deletion request, the movie will be permenately deleted from your collection and will need to be readded.")
                            confirmed_delete_request = input("Please confirm. (Y/N): ")

                            if confirmed_delete_request == "Y":
                                movies_list.remove(movie)
                                print("You have successfully removed this movie from your catalog.")

                            else:
                                print("You have aborted the deletion request.")

        elif user_input == 3:
            print("Displaying all movies in your catalog ...\n")

            if len(movies_list) == 0:
                print("You currently have no movies saved to your catalog. Please add a movie first by selecting the add movie option.")
            else:
                for i in range(len(movies_list)):
                    print(f"{i+1}. {movies_list[i][0]}")

                print("\nCOMMANDS:")
                print("1) Type '1' to lookup a movie")
                print("2) Type '2' to return back to the home page")
                display_user_request = int(input("\nSelect command: "))

                if display_user_request == 1:
                    print("Looking up a movie ...\n")
                    lookup_name = input("Enter the movie title you want to lookup: ")
                    for movie in movies_list:
                        if lookup_name in movie:
                            print("\n")
                            print(f"Movie Name: {movie[0]}, Directors: {movie[1]}, Release Year: {movie[2]}, Genre: {movie[3]}")

                            print("\nCOMMANDS:")
                            print("1) Type '1' to delete a movie")
                            print("2) Type '2' to return back to the home page")
                            delete_request = int(input("\nSelect command: "))

                            if delete_request == 1:
                                print(f"Are you sure you want to delete {movie[0]} from your catalog?")
                                print("NOTE: Be aware that by confirming this deletion request, the movie will be permenately deleted from your collection and will need to be readded.")
                                confirmed_delete_request = input("Please confirm. (Y/N): ")

                                if confirmed_delete_request == "Y":
                                    movies_list.remove(movie)
                                    print("You have successfully removed this movie from your catalog.")

                                else:
                                    print("You have aborted the deletion request.")

        elif user_input == 4:
            print("1) Type '1' to create a movie reminder")
            print("2) Type '2' to delete a previously created movie reminder")
            print("3) Type '3' to return back to the home page")
            request_type = int(input("\nSelect command: "))

            if request_type == 1:
                
                recipient_email = None
                recipient_phone = None

                user_selected_movie = input("Please enter the tile of the movie you would like to be reminded of?: ")
                message = (f"Hey! Don't forget to watch {user_selected_movie}. This reminder is brought to you by Moviehub.")
                
                reminder_type = int(input("Would you like to recieve this reminder via email (1), sms (2), or both (3)? 1/2/3: "))
                if reminder_type == 1:
                    reminder_delivery_method = 'email'
                    recipient_email = input("Please provide the email address at which you would like to recieve the reminder: ")
                elif reminder_type == 2:
                    reminder_delivery_method = 'sms'
                    recipient_phone = input("Please provide the phone number at which you would like to recieve the reminder. (Example format: 15551234567): ")
                elif reminder_type == 3:
                    reminder_delivery_method = 'both'
                    recipient_email = input("Please provide the email address at which you would like to recieve the reminder: ")
                    recipient_phone = input("Please provide the phone number at which you would like to recieve the reminder. (Example format: 15551234567): ")

                hours = int(input("In how many hours and minutes would you like to recieve this reminder? Hours first: "))
                minutes = int(input("In how many minutes would you like to recieve this reminder?: "))

                reminder_id_choice = input("Would you like to proivde a reminder id? Y/N: ")
                if reminder_id_choice == "Y":
                    reminder_id = str(input("Please enter an id: "))
                else:
                    reminder_id = None

                reminder_request(
                    microservice_request= "create",
                    reminder_id= reminder_id,
                    reminder_delivery_method= reminder_delivery_method,
                    hours= hours,
                    minutes= minutes,
                    email_subject= "Movie Reminder",
                    message= message,
                    recipient_email= recipient_email,
                    recipient_phone= recipient_phone
                )

            elif request_type == 2:
                reminder_id = input("Please enter the reminder id: ")

                reminder_request(
                    microservice_request= "delete",
                    reminder_id= reminder_id
                )

        elif user_input == 5:
            movie_name = input("Please enter the name of the movie you would like your recommendation to be based on: ")

            context = zmq.Context()
            print("\nClient attempting to connect to the AI Recommendation Microservice...")
            socket = context.socket(zmq.REQ)
            socket.connect("tcp://localhost:5560")

            keep_recommending = True
            while keep_recommending:

                print("\nSending a recommendation request to the AI Recommendation Microservice.")
                socket.send_string(movie_name)

                recommendation_response = socket.recv_string()
                print(f"Response from AI Recommendation Microservice recieved: {recommendation_response}")

                retry = input("\nWould you like another recommendation based on the same movie? (Y/N): ")
                if retry != "Y":
                    keep_recommending = False

        elif user_input == 6:
            print("1) Type '1' to get Top Trending Movies of the Day.")
            print("2) Type '2' to get Top Trending Movies of the Week.")
            
            choice = int(input("\nSelect command: "))
            time_period = "day" if choice == 1 else "week"

            number_of_movies = int(input("PLease enter the number of movies you want to see: "))

            context = zmq.Context()
            print("\nClient attempting to connect to the Trending Movies Microservice...")
            socket = context.socket(zmq.REQ)
            socket.connect("tcp://localhost:5557")
            
            print(f"Sending a request for the Top {number_of_movies} Trending Movies of the {time_period} to the Trending Movies Microservice.")
            socket.send_json({
                "time_period": time_period,
                "number_of_movies": number_of_movies
            })

            popular_response = socket.recv_json()
            print("Response from the Trending Movies Microservice:")
            print(f"Top {number_of_movies} Trending Movies of the {time_period}:")
            for idx, movie in enumerate(popular_response, start=1):
                print(f"{idx}, {movie['title']}")

        elif user_input == 7:
            print("\nMovieHub serves as a catalog to store all your favorite movies.")
            print("You can add movies to your catalog by selecting the 'add a movie' option.")
            print("If a movie was mistakenly added or a data error is present, a movie can be deleted by looking up the movie, and selecting the 'delete a movie' option.")
            print("Be aware that this wil result in the movie being permanetly deleted.")
            print("MovieHub also offers the option to set email and/or sms movie reminders, recieve AI movie recommendations, and view the most trending movies of the day/week.")
                
        elif user_input == 8:
            print("\nTerminating the program ...")

    print("Thank you for using MovieHub! Goodbye!\n")


def reminder_request(microservice_request, reminder_id=None, reminder_delivery_method=None, hours=None, minutes=None, email_subject=None, message=None, recipient_email=None, recipient_phone=None):
    context = zmq.Context()
    print("Client attempting to connect to Reminder Microservice...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    reminder_message = {
        'microservice_request': microservice_request,
        'reminder_id': reminder_id,
        'reminder_delivery_method': reminder_delivery_method,
        'hours': hours,
        'minutes': minutes,
        'message': message,
        'email_subject': email_subject,
        'provider_email': "moviehubalerts@gmail.com",
        'recipient_email': recipient_email,
        'recipient_phone': recipient_phone
    }

    reminder_message = {key: value for key, value in reminder_message.items() if value is not None}

    print("Sending a request to the Reminder Microservice")
    socket.send_json(reminder_message)
    response = socket.recv_json()
    print(f"Response from Reminder Microservice: {json.dumps(response, indent=2)}")


if __name__ == "__main__":
    main()
