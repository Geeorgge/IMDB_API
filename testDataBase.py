import unittest
from Database import DataBase 
from Movie import Movie

class testDatabase(unittest.TestCase):
    maxDiff = None

    def testSaveMovie(self):

        #Caso de prueba recibe un objeto de tipo movie, 
                            #Agregar para hacer pruebas
        cases = ( ( Movie("tt12338276","Alien Contactee: A Conversation with Dr.Louis Turi", 2020, 
                        """Contactees are people who have experienced contact with extraterrestrials. Dr. Louis Turi had four such encounters.
                            This documentary exams his encounters, his relationship with Astrology, 
                                and how he has accurately predicted several major world events.ri""",
                                    "Jeremy Norrie", "Louis Turi", "Documentary", 
                                            "http://image.tmdb.org/t/p/original/xnwNfj7Og5GYy9IQ4vewohjGhTl.jpg") , 'Esta pelicula ya fue guardada en la DB'),
                        #Agregar para hacer pruebas
                  (Movie("tt9893250", "I Care a Lot", 2021,                                 
                        """A court-appointed legal guardian defrauds her older clients and traps them under her care. But her latest mark comes with some unexpected baggage.""",
                                "J Blakeson", """Rosamund Pike, Peter Dinklage, Eiza González, Dianne Wiest, Chris Messina, Isiah Whitlock Jr., Macon Blair, Alicia Witt, Damian Young, Nicolas Logan, Kevin McCormick, Michael Malvesti, Liz Eng""",
                                        "Thriller, Drama, Comedy, Crime", "http://image.tmdb.org/t/p/original/gKnhEsjNefpKnUdAkn7INzIFLSu.jpg"), 'Esta pelicula ya fue guardada en la DB' ),
                    #Borrar para hacer pruebas
                    (Movie("tt0373889","Harry Potter and the Order of the Phoenix", 2007, 
                        """ Returning for his fifth year of study at Hogwarts, Harry is stunned to find that his warnings about the return of Lord Voldemort have been ignored. Left with no choice, Harry takes matters into his own hands, training a small group of students – dubbed 'Dumbledore's Army' – to defend themselves against the dark arts.""",
                                    "David Yates", """Daniel Radcliffe, Rupert Grint, Emma Watson, Michael Gambon, Ralph Fiennes, Tom Felton, Alan Rickman, Robbie Coltrane, Maggie Smith, Helena Bonham Carter, Brendan Gleeson, Gary Oldman, Jason Isaacs, Imelda Staunton, Matthew Lewis, Bonnie Wright, James Phelps, Oliver Phelps, Evanna Lynch, Richard Griffiths, Fiona Shaw, Robert Hardy, Emma Thompson, Julie Walters, David Thewlis, Natalia Tena, Harry Melling, David Bradley, Mark Williams, Katie Leung, Chris Rankin, Devon Murray, Alfred Enoch, Warwick Davis, Jamie Waylett, Josh Herdman, Shefali Chowdhury, Afshan Azad, Geraldine Somerville, Adrian Rawlins, Kathryn Hunter, George Harris, Peter Cartwright, Brigitte Millar, Sian Thomas, Apple Brook, William Melling, Jim McManus, Nick Shirm, Ryan Nelson, Sam Beazley, John Atterbury, Richard Leaf, Timothy Spall, Lauren Shotton, Nicholas Blane, Jason Boyd, Richard Macklin, Christopher Rithin, Tony Maudsley, Timothy Bateson, Jessica Hynes, Michael Wildman, Jason Piper, Arben Bajraktaraj, Peter Best, Richard Trinder, Richard Cubison, Tav MacDougall, Alec Hopkins, Robbie Jarvis, James Walters, Charles Hughes, James Utechin, James Payton, Lisa Wood, Cliff Lanning, Miles Jupp, Jamie Wolpert, Daisy Haggard, Nathan Clarke, Alfie Enoch, Robert Pattinson, Martin Alexander, Katie Amess, Jamie Anderson, Poppy Carter, Ray Donn, Clive Elkington, Reshad Esmail, Samuel Gaukroger, Rusty Goffe, Natalie Hallam, Sarah Harrison, Kevin Hudson, Ashley Hull, Elliot James Langridge, Christopher O'Shea, Chloe Rich, Paije Richardson, Peter Roy, Tabatha St. Vincent, Jongeorge Stephenson, Albert Tang, Nick Thomas-Webster, Siobhan Ellen Williams""",
                                                    "Adventure, Fantasy, Mystery, Action, Family", "http://image.tmdb.org/t/p/original/s836PRwHkLjrOJrfW0eo7B4NJOf.jpg"), '¡¡¡ Datos guardados :D !!!'),
                    #Borrar para hacer pruebas                          
                    (Movie("tt4963998", "Hell on Earth: The Story of Hellraiser III", 2015, """The Story of Hellrasier III" offers a half-hour discussion of the overhaul involved in the making of the delayed third film in the Hellraiser franchise, in which a cult horror format was consciously transformed into a mass-market product with an eye on the teen market and a sense of disappointment from the British crew of the first two films. Frank Harrison""",
                                "Kevin McDonagh, Christopher Griffiths, K. John McDonagh",
                                    "Peter Atkins, Simon Bamford, Doug Bradley, Ken Carpenter, Bob Keen, Tony Randel, Kenneth Cranham",
                                        "Documentary, Short", "No hay poster para esta pelicula"), '¡¡¡ Datos guardados :D !!!'))                    
                                                                            

        for movie, esp in cases:
            a = DataBase().saveMovie(movie)  
            self.assertEqual(str(a), esp)

    def testShowMovie(self):    

        cases = (   ("A Dark Matter",       "No existe ésta pelicula en la DB"), #Borrar para hacer pruebas
                    ("A Passport to Hell",  "No existe ésta pelicula en la DB"), #Borrar para hacer pruebas
                    
                    ("A Fantastic Fear of Everything",      Movie("tt2006040", "A Fantastic Fear of Everything", 2012,
                                                            "Jack is a children's author turned crime novelist whose detailed research into the lives of Victorian serial killers has turned him into a paranoid wreck, persecuted by the irrational fear of being murdered. When Jack is thrown a life-line by his long-suffering agent and a mysterious Hollywood executive takes a sudden and inexplicable interest in his script, what should be his big break rapidly turns into his big breakdown, as Jack is forced to confront his worst demons; among them his love life, his laundry and the origin of all fear.",
                                                                "Crispian Mills, Chris Hopewell, Crispian Mills, Chris Hopewell(co-director)",
                                                                    """Simon Pegg, Paul Freeman, Clare Higgins, Amara Karan, Alan Drake, Michael Feast, Mo Idriss, Elliot Greene, Harley Kierans, Kamal Onyiukah, Bernard Cribbins, Henry Lloyd-Hughes, Anna Madeley, Pamela Cundell, Jane Stanness, Tuyet Le, Kiran Shah, Jack Jaikol Situn, Henry Bowers-Broadbent, Doug Tulloch, Josh Warner-Campbell, Millie Hagland, Baxter Westby, Teresa Churcher, Karan Plah, Don McCulloch, Golda John, Tamzin Griffin, Jacqueline Chan, Simon Kunz, Jay Taylor, Zaak Conway, Mara Ashton, Charlie Covell, Johnny Alston, Lieve Carchon, Gary Golding, Alice Orr-Ewing, Keshava Mills, Kerry Shale, Bhanu Alley, Fabio Vollono""",
                                                                        "Comedy, Thriller, Horror, Action",
                                                                            "http://image.tmdb.org/t/p/original/eVfQCC2QIx2YuionhKLNs4nCj4i.jpg")),
                    
                    ("Paranormal Activity 4",               Movie("tt2109184", "Paranormal Activity 4", 2012,
                                                                        "It has been five years since the disappearance of Katie and Hunter, and a suburban family witness strange events in their neighborhood when a woman and a mysterious child move in.",
                                                                            "Diane Weiss, Ariel Schulman, Henry Joost, Tracy L. Moody, Jenny Siff, Henry Joost, Ariel Schulman",
                                                                                """Katie Featherston, Kathryn Newton, Matt Shively, Aiden Lovekamp, Brady Allen, Stephen Dunham, Alexondra Lee, Georgica Pettus, Alisha Boe, Brendon Eggertsen, Sprague Grayden, Brian Boland, William Juan Prieto, Sara Mornell, Constance Esposito, Ty Dawson, Jennifer Hale, Jonah Pasco, Rightor Doyle, Tamara Bersane, Robert Clotworthy, Esther Austin, Mary Payne Moran, Taj, John Duerler, Jake Plotkin, Jorga Caye, Jamieson Deacy, Kate Stephens-Miller""",
                                                                                    "Horror, Action, Fantasy, Mystery, Thriller",
                                                                                        "http://image.tmdb.org/t/p/original/8Devidv1ujbw1uCa1Dn3qVujHTg.jpg")))

        for name, esp in cases:
            d = DataBase().showMovie(name)
            self.assertEqual(str(d), str(esp))       


    def testDeleteMovie(self):
                                                            #Agregar estas peliculas para hacer pruebas
        cases = (   ("tt0362417",   "Pelicula borrada :O"),  # Aragami
                    ("tt0277909",  "Pelicula borrada :O"),  # Mutant Aliens
                    (None,          "Esta pelicula no esta en la base de datos!!!"),
                    ("",            "Esta pelicula no esta en la base de datos!!!"))


        for movie_id, esp in cases:  
            b = DataBase().deleteMovie(movie_id)
            self.assertEqual(b, esp)


if __name__ == "__main__":
    unittest.main()