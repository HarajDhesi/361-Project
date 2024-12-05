import zmq
import vertexai
from vertexai.generative_models import GenerativeModel
import random
import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")

def ai_recommendation(movie_title):
    """Provides a movie recommendation using the Google Gemini model."""
    try:
        vertexai.init(project=PROJECT_ID, location="us-central1")
        model = GenerativeModel("gemini-1.5-flash-002")
        response = model.generate_content(f"You are a movie recommendation assistant that helps with movie suggestions. Can you please recommend a movie similar to {movie_title}. This recommendation should be made as if it's the {random.randint(1,100)}th time you have been asked to give a recommendation, and every time, it is a unique recommendation compared to before. PLease only provide the title of the movie.")
        return response.text.strip()
    except Exception as e:
        return f"Error in generating recommendation: {str(e)}"


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5560")
    print("AI Recommendation Microservice is running...\n")

    while True:
        movie_name = socket.recv_string()
        print(f"A request for a recommendation based on the movie: {movie_name} has been recieved.")

        movie_recommendation = ai_recommendation(movie_name)

        print(f"Sending movie recommendation: {movie_recommendation} to client.")

        socket.send_string(movie_recommendation)

        print("\nAI Recommendation Microservice is running...\n")

if __name__ == "__main__":
    main()
