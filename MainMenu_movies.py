from ConnectionApi import APIMovie
from Database import DataBase
from Movie import Movie


class MenuOpciones():

    def search_movie(self, name:str): # ----> Busca una película y pregunta si quiere guardar
        
        movie_titles = APIMovie().get_movie_titles(name)
        if movie_titles == "Sin resultados":
            print("No existe esta pelicula en la API DB\n")
            print("Busca otra película por favor")

        else:
            print("Se encontraon los siguientes resultados: \n")
            for i in range(len(movie_titles)):
                print(movie_titles[i])
            n = False
            while n == False:
                print("\tEscoge el nombre de una película y vuelve a hacer la busqueda sí quieres guardarla :D\n") 
                op =  int(input("\t\tTeclea 1 para hacer la busqueda de nuevo y guardarla Ó teclea 2 para regresar al menu:\n"))
                if op == 1:
                    new_name = str(input("Cual fue la película que escogiste? \n"))
                    new_search = APIMovie().getMovie(new_name) #Se crea el objeto con la película nueva
                    DataBase().saveMovie(new_search) #Guardar en la base de datos
                    print("Pelicula guardada, hasta luego :D")
                    n = True
                    
                elif op == 2:
                    n = True
                    
                else:
                    print("Elige una opcion del menu")

    def save_movie(self, nombre: Movie): # ----> Busca una película
    
        movie_new = APIMovie().getMovie(nombre)
        
        DataBase().saveMovie(movie_new) 
           

    def show_all_movies(self): # ----> Muestra todas las películas guardadas en la BDD
         
        moviesList = DataBase().showAllMovies()
        print( moviesList)
    
    def show_a_movie(self, name:str):  # ----> Muestra una película que esta guardada en la BDD
        
        moviesList = DataBase().showMovie(name)
        print(moviesList)

    def delete_movie(self, name):  # ----> Borra una película que esta guardada en la BDD by ID

        moviesList = DataBase().deleteMovie(name)
        if moviesList == None: 
            print("No se pudo borrar la película D:")
        else:
            print("Película Borrada :D")
            
    
def main():
    
    salir = False
    inst = MenuOpciones()
    
    while salir == False:
        op = int(input("""\t\t\t\t  - - - - - - - - - -  Escoge la opición - - - - - - - - - - -\n
                    \t\t\t- - - - - - - - - MENÚ DE OPCIONES - - - - - - - -\n
                        \t\t\t1. Buscar película\n
                        \t\t\t2. Mostrar todas las peliculas guardadas\n
                        \t\t\t3. Mostrar una película\n
                        \t\t\t4. Borrar una película\n
                        \t\t\t5. SALIR\n"""))
        
        if op == 1:
            nombre = input("Cual pelicula buscas? \n")
            inst.search_movie(nombre)
        elif op == 2:
            inst.show_all_movies()
        elif op == 3:
            name = input("Ingrese el nombre de la pelicula: \n")
            inst.show_a_movie(name)
        elif op == 4:
            name = input("Ingrese el ID de la pelicula que desea eliminar: \n")
            inst.delete_movie(name)
        elif op == 5:
            print("Hasta luego")
            exit()
        else:
            print("Elige una opcion del menu")


if __name__ == "__main__":
    main()
    

 