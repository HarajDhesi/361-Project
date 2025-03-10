# CS-361 Course Project

## Overview
Welcome to Movie Hub, a program to track your watched movies in one central location. This project utilizes a microservice architecture to schedule movie reminders, allow users to fetch movie details with an IMDb id, recieve AI movie recommendations, and view the most trending movies of the day and week.

## Microservices
1. Microservice A: Movie Reminders

2. Microservice B: Retrieve Movie Details

3. Microservice C: AI Movie Recommendations

4. Microservice D: Trending Movies

## Project Structure
```
movie_hub/
├── main.py                    # Main CLI program
├── reminder_service/
│   └── reminder.py            # Handles movie reminders for email and/or sms
├── imdb_id_search_service/
│   └── imdb_id_search.py      # Fetches movie details based on IMDb id
├── recommendation_service/
│   └── recommendation.py      # AI recommendations based on a movie
├── trending_movies_service/
│   └── trending.py             # Fetches trending movies of the day or week
```
