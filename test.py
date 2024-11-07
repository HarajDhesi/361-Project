import imdb

ia = imdb.Cinemagoer()

imdb_id = input("Please enter the movie id: ")

movie = ia.get_movie(imdb_id)

print(movie['title'])

print(movie['directors'])
for item in movie['directors']:
    print(item)

print(movie['year'])

for item in movie['genres']:
    print(item)

