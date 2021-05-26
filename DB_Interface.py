from abc import ABC, abstractmethod


class DataBaseMovies(ABC):

    #Crea una tabla en la base de datos 
    @abstractmethod
    def createTable(self):
        pass
    
    #Guarda una pelicula en la base de datos
    @abstractmethod
    def saveMovie(self, movie_name):
        pass
   
    #Borra una pelicula de la BDD conforme al nombre
    @abstractmethod
    def deleteMovie(self, movie_name):
        pass

    #Muestra todas las peliculas de la base de datos
    @abstractmethod
    def showAllMovies(self):
        pass

    #Muestra una las peliculas de la base de datos
    @abstractmethod
    def showMovie(self, movie_name):
        pass
 
