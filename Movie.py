class Movie():

    #constructor
    
    def __init__(self, id_imdb: str, title: str, yearr: int, description: str, directors: str, stars: str, genres: str, image: str):
        self.id_imdb = id_imdb           
        self.title = title               
        self.yearr = yearr               
        self.description = description     
        self.directors = directors         
        self.stars = stars                 
        self.genres = genres               
        self.image = image                

    #Representacion en "str" del objeto de tipo "Pelicula"
    def __str__(self):
         return f"""\nID de la Película: {self.id_imdb}\nTitulo de la pelicula: {self.title}\nAño de emision: {self.yearr}\nDescripción: {self.description}\nDirectores: {self.directors}\nActores: {self.stars}\nGeneros: {self.genres}\nPoster: {self.image}\n\n"""
    
    def __eq__(self, movie):
        
        if movie.id_imdb != self.id_imdb:
            print(movie.id_imdb, "no es igual a", self.id_imdb)
            return False

        if movie.yearr != self.yearr:
            print(movie.yearr, "no es igual a", self.yearr)
            return False

        if movie.description != self.description:
            print(movie.description, "no es igual a", self.description)
            return False

        if movie.directors != self.directors:
            print(movie.directors, "no es igual a", self.directors)
            return False

        if movie.stars != self.stars:
            print(movie.stars, "no es igual a", self.stars)
            return False

        if movie.genres != self.genres:
            print(movie.genres, "no es igual a", self.genres)
            return False

        if movie.image != self.image:
            print(movie.image, "no es igual a", self.image)
            return False

if __name__ == "__main__":
    pass