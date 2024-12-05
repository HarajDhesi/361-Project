import zmq
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3/trending/movie"

def fetch_top_movies(time_period, number_of_movies=5):
    """Fetches trending movies from TMDB API based on the time period and number of movies."""

    url = f"{BASE_URL}/{time_period}"
    params = {"api_key": TMDB_API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()

    movies = response.json().get("results", [])
    top_movies = [{"title": movie["title"]} for movie in movies[:number_of_movies]]
    return top_movies


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5557")

    print("Trending Movies Microservice is running...\n")

    while True:
        message = socket.recv_json()
        print(f"Recieved request: {message}")
        
        time_period = message.get("time_period")
        number_of_movies = message.get("number_of_movies", 5)

        print(f"Recieved request for retrieval of Top {number_of_movies} Tending Movies of the '{time_period}' period.")

        result = fetch_top_movies(time_period, number_of_movies)

        print(f"Sending Top {number_of_movies} Trending Movies of the '{time_period}' to client.")
        socket.send_json(result)

        print("\nTrending Movies Microservice is running...\n")

if __name__ == "__main__":
    main()
