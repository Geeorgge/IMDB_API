import sqlite3
from DB_Interface import DataBaseMovies
from Movie import Movie


 

#implementa de la interface "DataBaseMovies"
 
class DataBase(DataBaseMovies):

    def __init__(self): #, 

        # Se crea la conexion a la base de datos
        self.conexion = sqlite3.connect("moviesDB")

    def createTable(self):
        # Se crea el cursor para manejar consultas
        cursor = self.conexion.cursor()
        #se crea la tabla de peliculas y la demas logica
        try:
            #sí no existe, se crea la tabla movies
            cursor.execute("""CREATE TABLE IF NOT EXISTS movies (id_imdb  TEXT (15) PRIMARY KEY,
                                            title TEXT (15),
                                            yearr INTEGER(10),
                                            description TEXT (500),
                                            directors TEXT (50),
                                            stars TEXT (500),
                                            genres TEXT (50),
                                            image TEXT (80)
                                            )""")
            return ("Tabla _movie_ creada con éxito")
            
        
        except sqlite3.Error as error:
            
            print("Error al conectar con sqlite", error)

            #Commit y se cierra la conexion
            self.conexion.commit()
            self.conexion.close()


    def saveMovie(self, movie: Movie): #movie: Movie
        # Se crea el cursor para manejar consultas
        self.cursor = self.conexion.cursor()
        #Consulta para ver si existen datos 
        self.cursor.execute(f"SELECT id_imdb FROM movies WHERE id_imdb = '{movie.id_imdb}' ")
        id_movie = self.cursor.fetchone() #guardamos la pelicula en una variable
        if id_movie != None:
            return "Esta pelicula ya fue guardada en la DB"
        else:
            
            self.cursor.execute("INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (movie.id_imdb, movie.title, movie.yearr, movie.description, movie.directors, movie.stars, movie.genres, movie.image))
            self.conexion.commit()   
        return "¡¡¡ Datos guardados :D !!!"                                  
         

    def deleteMovie(self, id_movie):
        # Se crea el cursor para manejar consultas
        self.cursor = self.conexion.cursor()
        #Sí no existe la pelicula, manda error
        if id_movie == None or id_movie == "":
            return "Esta pelicula no esta en la base de datos!!!"
        #Sí no, se procede a borrarla de la base de datos
        else:

            self.cursor.execute("DELETE FROM movies WHERE id_imdb = ?", (id_movie,)) #Borramos pelicula mediante el id
            
            self.conexion.commit()

        return "Pelicula borrada :O"

    def showAllMovies(self):                                
        # Se crea el cursor para manejar consultas
        self.cursor = self.conexion.cursor()
        #Query para mostrar todas las peliculas en la DB
        self.cursor.execute("SELECT * FROM movies")
        data = self.cursor.fetchall() #Tomamos todas las peliculas con "fetchall"
        movies_saved = [] #Lista para almacenar las peliculas
        if data == None or data == "":
            return "No existe ésta pelicula en la DB"
        else:
            print("Peliculas guardadas: ")
             
            
            for results in data:
                A = Movie(results[0], results[1], 
                                results[2],results[3],    
                                    results[4], results[5],   
                                        results[6], results[7])
                
                movies_saved.append(str(A))
             
        return ''.join(movies_saved)

    
    def showMovie(self, movie:str):                            
        # Se crea el cursor para manejar consultas
        self.cursor = self.conexion.cursor()
        #Query para mostrar la pelicula solicitada de la DB
        self.cursor.execute("SELECT * FROM movies WHERE title = ?", (movie,))
        data = self.cursor.fetchone() #tomamos solo la pelicula solicitada con "fetchone"
        #movies_saved = []
        if data == None or data == "" or movie not in data:
            return "No existe ésta pelicula en la DB"
        else:
            print("Pelicula encontrada: ")
        #for i in range(len(data)):
            A = Movie(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        #movies_saved.append(A)

        return A

 

if __name__ == "__main__":
     
     pass