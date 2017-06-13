import media
import fresh_tomatoes
# Javi's Stage 3 Submission

the_secret_life_of_pets = media.Movie('The Secret Life of Pets',
                                     media.Movie.VALID_RATINGS[4],
                                     'A movie about what your pets do in the time between when you leave for work and return home.',
                                     'http://www.gstatic.com/tv/thumb/movieposters/11924889/p11924889_p_v7_aa.jpg',
                                     'https://www.youtube.com/watch?v=i-80SGWfEjM')

#print the_secret_life_of_pets.storyline

deadpool = media.Movie('Deadpool',
                      media.Movie.VALID_RATINGS[3],
                      'A former Special Forces operative turned mercenary is subjected to a rogue experiment and becomes Deadpool.',
                      'https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg',
                      'https://www.youtube.com/watch?v=FyKWUTwSYAs')

#print deadpool.storyline

#deadpool.show_trailer()

airplane = media.Movie('Airplane',
                      media.Movie.VALID_RATINGS[1],
                      'Disaster Movie about an Airplane in trouble',
                      'https://upload.wikimedia.org/wikipedia/en/f/f5/Airplane%21.jpg',
                      'https://www.youtube.com/watch?v=rzRJWy-3_Dc')

#airplane.show_trailer()

zoolander_2 = media.Movie('Zoolander 2',
                        media.Movie.VALID_RATINGS[4],
                        'Derek and Hansel are modelling again when an opposing company attempts to take them out from the business.',
                        'http://www.movienewz.com/img/films/zoolander-2-movie-poster.jpg',
                        'https://www.youtube.com/watch?v=09nTwccQTUA')

london_has_fallen = media.Movie('London Has Fallen',
                               media.Movie.VALID_RATINGS[4],
                               'U.S. Secret Service agent Mike Banning springs into action when terrorists attack London.',
                               'https://upload.wikimedia.org/wikipedia/en/2/26/London_Has_Fallen_poster.jpg',
                               'https://www.youtube.com/watch?v=q9y3z-lx-ZE')

super_sparkle_janil = media.Movie('Super Sparkle Janil',
                                 media.Movie.VALID_RATINGS[0],
                                 'The story of a Smart Girl by day and a Super Girl at night.',
                                 'http://i51.photobucket.com/albums/f392/techno-logic/Super%20Janil.jpg',
                                 'https://www.youtube.com/watch?v=pR6QibJ68qM')


movies = [the_secret_life_of_pets, deadpool, airplane, zoolander_2, london_has_fallen, super_sparkle_janil]

fresh_tomatoes.open_movies_page(movies)
#print zoo

#print media.Movie.__doc__
#print media.Movie.__name__
#print media.Movie.__module__