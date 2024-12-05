import imdb
import zmq

def imdb_search():
    """Fetches movie details using the provided IMDb id and sends them back as a json."""
    
    ia = imdb.Cinemagoer()

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5561")
    print("IMDb ID Search Microservice is running...")

    while True:
        imdb_id = socket.recv_string()
        print(f"IMDb id has been recieved: {imdb_id}")

        movie = ia.get_movie(imdb_id)
        movieName = movie['title']
        directorName = ", ".join(director['name'] for director in movie.get('directors', []))
        releaseYear = movie['year']
        genreList = movie['genres']
        movieGenre = ", ".join(genreList)

        socket.send_json({
            'movie_name': movieName,
            'directors': directorName,
            'release_year': releaseYear,
            'genre': movieGenre
        })
        print(f"Movie details for IMDb ID: {imdb_id} ({movieName}) have been retrieved and sent out.")

        print("\nIMDb ID Search Microservice is running...")

if __name__ == "__main__":
    imdb_search()
