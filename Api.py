import imdb
moviesDB = imdb.IMDb()

#print(dir(moviesDB))


movies = moviesDB.search_movie('titanic')

    
id = movies[0].getID()
movie = moviesDB.get_movie(id)

title = movie['title']
year = movie['year']
genre = movie['genre']

print("movie info: ")
print(f"{title} -{year} - {genre}")