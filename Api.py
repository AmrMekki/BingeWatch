import imdb



ia = imdb.IMDb()
top250 = ia.get_top250_movies()

# Iterate through the first 20 movies in the top 250
for movie_count in range(0, 20):
    # First, retrieve the movie object using its ID
    movie = ia.get_movie(top250[movie_count].movieID)
    # Print movie title and genres
    print(movie['title'])
    print(*movie['genres'], sep=", ")