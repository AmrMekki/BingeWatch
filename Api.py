import imdb
moviesDB = imdb.IMDb()

#print(dir(moviesDB))


movies = moviesDB.search_movie('titanic')

print('Searching for "titanic": ')
for movie in movies:
    title = movie['title']
    year = movie['year']
    print(f'{title} - {year}')
    
    
