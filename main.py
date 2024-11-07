import imdb

def main():

    ia = imdb.Cinemagoer()

    # Intialize list datastructure
    movies_list = []

    print("\n")
    print("*** Welcome to Movie Hub ***")
    print("Save all of your favorite movies in one place!")


    user_input = 0
    while user_input != 5:

        print("\nCOMMANDS:")
        print("1) Type '1' to add a movie")
        print("2) Type '2' to lookup a movie")
        print("3) Type '3' to view all movies")
        print("4) Type '4' for help on how to use this program")
        print("5) Type '5' to quit")

        user_input = int(input("\nSelect command: "))
        
        # user_input = int(input("\n[1/2/3/4]: "))

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
                movie = ia.get_movie(imdb_id)
                movieName = movie['title']
                # directorName = ""
                # for item in movie['directors']:
                #     directorName += " " + str(item)
                directors = movie['directors']
                directorName = ", ".join(director['name'] for director in directors)
                releaseYear = movie['year']
                genreList = movie['genres']
                movieGenre = ", ".join(genreList)
                print('\n')
                print(f"Movie Name: {movieName}, Directors: {directorName}, Release Year: {releaseYear}, Genre: {movieGenre}")
                correct_details = input("Are the movie details correct? (Y/N): ")

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

                        # implement deleting logic here
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
                # need to change so only the movie title is displayed
                for i in range(len(movies_list)):
                    print(f"{i+1}. {movies_list[i][0]}")

                    # print(f"{i+1}. Movie Name: {movies_list[i][0]}, Directors: {movies_list[i][1]}, Release Year: {movies_list[i][2]}, Genre: {movies_list[i][3]}")

                # have to implement logic to allow user to select a movie from the list of movies to get more details about it.
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

                            # implement deleting logic here
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
                
            # for registered_movie in movies_list:
            #     print(f"Moive Name: {registered_movie[0]}, Directors: {registered_movie[1]}, Release Year: {registered_movie[2]}, Genre: {registered_movie[3]}")


        elif user_input == 4:
            print("\nMovieHub serves as a catalog to store all your favorite movies.")
            print("You can add movies to your catalog by selecting the 'add a movie' option.")
            print("If a movie was mistakenly added or a data error is present, a movie can be deleted by looking up the movie, and selecting the 'delete a movie' option.")
            print("Be aware that this wil result in the movie being permanetly deleted.")
                
        elif user_input == 5:
            print("\nTerminating the program ...")

    print("Thank you for using MovieHub! Goodbye!\n")


    # Idea:
    # On the start of the app, give user the commands to View Catalog or Exit
    # when viewing catalog, it will display all movies or display a helpful promt that tells how to add a movie
        # command options will be
        # 1) Add a movie, 2) View a movie 3) Return to home 4) Quit


if __name__ == "__main__":
    main()