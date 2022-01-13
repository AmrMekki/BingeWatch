import imdb

movies = imdb.IMDb()
top250 = movies.get_top250_movies()


for movie_count in range(0, 20):
    
    movie = movies.get_movie(top250[movie_count].movieID)
    
    print(movie['title'])
    print(*movie['genres'], sep=", ")