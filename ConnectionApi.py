import urllib
from Api_Interface import ApiConnect
from Movie import Movie
import http.client
import json


class APIMovie(ApiConnect):

    def __init__(self):
       self.id_imdb = ""

    # Funcion que busca el id, titulo y año de la pelicula
    def searchMovieTitle(self, nombre: str):
        conn1 = http.client.HTTPSConnection(
            "movies-tvshows-data-imdb.p.rapidapi.com")

        headers1 = {
            'x-rapidapi-key': "cbcf05ab5fmsh24801d50619d037p1b4742jsn25a4dc832034",
            'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
        }

        # Primer request que buscara la pelicula que se le ingrese en la funcion
        # Primero el request y despues getresponse, para evitar errores
        # urlib para parsear el texto ingresado sí es que tiene espacios o simbolos con urllib
        conn1.request("GET", "/?type=get-movies-by-title&title=" +
                      urllib.parse.quote(nombre), headers=headers1)

        # Se guarda en una variable, y se obtiene un objeto de tipo HTTPResponse
        res1 = conn1.getresponse()
        # Convertimos a texto el objeto anterior en una variable nueva, ahora es de tipo "bytes"
        data1 = res1.read()
        if res1.status != 200:               # Se comprueba si el status es correcto, si no, manda un error
            return "ERROR IN API CONNECTION"
        else:
            movies_list = []  # Lista para guardar datos obtenidos de la pelicula

            # Ahora convertimos a json el objeto de tipo "bytes"
            new_data_json1 = json.loads(data1)
            # Se extraen datos del primer request
            # Extraccion de datos de la API
            if new_data_json1["search_results"] == 0:  # Si tu busqueda no se encontro
                # movies_list.append("")
                return "Sin resultados"
            else:
                for movie in range(len(new_data_json1["movie_results"])):
                    if new_data_json1["movie_results"][movie]["imdb_id"] not in movies_list:
                        self.id_imdb = new_data_json1["movie_results"][movie]["imdb_id"]
                        if self.id_imdb == None or self.id_imdb == "":
                            movies_list.append("No hay ID para esta película")
                        else:
                            if len(self.id_imdb) == len(new_data_json1["movie_results"][movie]["imdb_id"]):
                                movies_list.append(self.id_imdb)

                    if new_data_json1["movie_results"][movie]["title"] not in movies_list:
                        names = new_data_json1["movie_results"][movie]["title"]
                        if names == None or names == "":
                            movies_list.append("No hay titulo para esta película")
                        else:
                            if len(names) == len(new_data_json1["movie_results"][movie]["title"]):
                                movies_list.append(names)

                    if new_data_json1["movie_results"][movie]["year"] not in movies_list:
                        yearr = new_data_json1["movie_results"][movie]["year"]
                        if yearr == None or names == "":
                            movies_list.append(
                                "No hay año de emision para esta película")
                        else:
                            movies_list.append(yearr)

            if len(movies_list) > 2:
                return movies_list[0:3]
            else:
                return movies_list

        

    
    def searchMovieDetails(self, idds=""): 
        
        conn2 = http.client.HTTPSConnection(
            "movies-tvshows-data-imdb.p.rapidapi.com")

        headers2 = {
            'x-rapidapi-key': "cbcf05ab5fmsh24801d50619d037p1b4742jsn25a4dc832034",
            'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
        }

        self.id_imdb = idds 
        # SEGUNDO REQUEST
        conn2.request("GET", "/?type=get-movie-details&imdb="+urllib.parse.quote(idds),
                      headers=headers2) 

        res2 = conn2.getresponse()  # Objeto de tipo HTTPResponse
        data2 = res2.read()  # Convertimos a texto el objeto anterior, ahora es de tipo "bytes"
        if res2.status != 200:  # Se comprueba si el status es correcto, si no, manda un error
            return "ERROR IN API CONNECTION"
        else:
            movies_list = []  # Lista para guardar datos obtenidos de la pelicula
            # Ahora convertimos a json el objeto de tipo "bytes"
            new_data_json2 = json.loads(data2)
            # Extraccion de datos de la API del segundo request
            if "description" in new_data_json2:
                description = new_data_json2["description"]
                
                if description is not None  or description != "":
                    #new_descrp = ', '.join(map(str, description))
                    movies_list.append(description)
                else:
                    movies_list.append("No hay descripción para esta película")
            if "directors" in new_data_json2:
                directors = new_data_json2["directors"]
                if directors is not None: # or directors != "":
                    new_directors = ', '.join(map(str, directors))
                    movies_list.append(new_directors)
                else:
                    movies_list.append("No hay directores para esta película")
            if "stars" in new_data_json2:
                stars = new_data_json2["stars"]
                if stars is not None: # or stars != "":
                    new_stars = ', '.join(map(str, stars))
                    movies_list.append(new_stars)
                else:
                    movies_list.append("No hay actores para esta película")
            if "genres" in new_data_json2:
                genres = new_data_json2["genres"]
                if genres is not None: # or genres != "":
                    new_gnres = ', '.join(map(str, genres))
                    movies_list.append(new_gnres)
                else:
                    movies_list.append("No hay generos para esta película")
        
            return movies_list

    def searchMovieImage(self, idds=""): 
        conn3 = http.client.HTTPSConnection(
            "movies-tvshows-data-imdb.p.rapidapi.com")
        
        #La variable self.id_imdb es la del constructor, y la igualamos al parametro de la funcion,
        #Que es la que toma el request
        #self.id_imdb = imageimdb

        headers3 = {
            'x-rapidapi-key': "cbcf05ab5fmsh24801d50619d037p1b4742jsn25a4dc832034",
            'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
        }
        # conn.request necesita el ID de la pelicula, este mismo se extrae del request anterior
        self.id_imdb  =   idds 
        
        conn3.request(
            "GET", "/?type=get-movies-images-by-imdb&imdb="+urllib.parse.quote(idds), headers=headers3) 
        res3 = conn3.getresponse()  # Objeto de tipo HTTPResponse
        # .decode("utf-8")  # Convertimos a texto el objeto anterior, ahora es de tipo "bytes"
        data3 = res3.read()
        if res3.status != 200:  # Se comprueba si el status es correcto, si no, manda un error
            return "ERROR IN API CONNECTION"
        else:
            movies_list = []  # Lista para guardar datos obtenidos de la pelicula

            # Ahora convertimos a json el objeto de tipo "bytes "
            new_data_json3 = json.loads(data3)

            # Extraccion de datos de la API del tercer request
            if "poster" in new_data_json3 and new_data_json3["poster"] != "":
                image = new_data_json3["poster"]
                movies_list.append(image)

            else:
                movies_list.append("No hay poster para esta pelicula")

        return movies_list

    # Este metodo se manda a llamar en la opcion de buscar pelicula en el menu de opciones
    # Y sirve solo para mostrar los resultados de una busqueda de peliculas, despues de hacer
    # Esta busqueda, se vuelve a buscar la pelicula que se quiere guardar
    def get_movie_titles(self, name_movie: str):
        conn4 = http.client.HTTPSConnection(
            "movies-tvshows-data-imdb.p.rapidapi.com")

        headers4 = {
            'x-rapidapi-key': "cbcf05ab5fmsh24801d50619d037p1b4742jsn25a4dc832034",
            'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
        }
        # Primer request que buscara la pelicula que se le ingrese en la funcion
        conn4.request("GET", "/?type=get-movies-by-title&title=" +
                      urllib.parse.quote(name_movie), headers=headers4)
        res4 = conn4.getresponse()
        data1 = res4.read()
        if res4.status != 200:
            return "ERROR IN API CONNECTION"
        else:
            movies_list = []
            new_data_json4 = json.loads(data1)
            if new_data_json4["search_results"] == 0:  # Si tu busqueda no se encontro
                # movies_list.append("")
                return "Sin resultados"
            else:
                if name_movie == None or name_movie == "" or name_movie == " ":
                    return "Ingresa un nombre correctamente"
                else:
                    for movie in range(len(new_data_json4["movie_results"])):
                        if new_data_json4["movie_results"][movie]["title"] not in movies_list:
                            names = new_data_json4["movie_results"][movie]["title"]
                            movies_list.append(names)

        return movies_list

    # Interface que regresa un objeto de tipo Movie()
    def getMovie(self, nombre: str):  # , id_movie:str
        id_title_year = self.searchMovieTitle(nombre)
        idd = id_title_year[0]
        details_movie = self.searchMovieDetails(idd)
        image_movie = self.searchMovieImage(idd) 
        new_object_movie = Movie(id_title_year[0], id_title_year[1], id_title_year[2],
                                 details_movie[0], details_movie[1], details_movie[2], details_movie[3],
                                 image_movie[0])
    
        return new_object_movie 


if __name__ == "__main__":
    pass
    

 