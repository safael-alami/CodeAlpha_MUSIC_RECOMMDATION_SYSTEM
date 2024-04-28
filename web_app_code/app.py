from flask import Flask, render_template
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

# Remplacez 'YOUR_CLIENT_ID' et 'YOUR_CLIENT_SECRET' par vos propres identifiants client Spotify

client_id = '70dd0df189844dcfbc1ac8b11518084c'
client_secret = 'd3dae35ae76c483ab59be3f3b270a4fc'

# Initialisation du gestionnaire d'authentification client Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

# Création d'une instance de l'API Spotipy
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


song_names = [
    "Bohemian Rhapsody", "Billie Jean", "Hotel California", "Imagine", "Stairway to Heaven", "Hey Jude", "Smells Like Teen Spirit", "Yesterday", "Every Breath You Take", "Sweet Child o' Mine", "Like a Rolling Stone", "Purple Rain", "Let It Be", "Wonderwall", "I Will Always Love You", "Dancing Queen", "Wonderful Tonight", "My Heart Will Go On", "Don't Stop Believin'", "Livin' on a Prayer", "I Want to Hold Your Hand", "Thriller", "What a Wonderful World", "Somewhere Over the Rainbow", "Hallelujah", "Sweet Home Alabama", "Hotel California", "Wish You Were Here", "The Sound of Silence", "Piano Man", "The Show Must Go On", "Comfortably Numb", "Hurt", "Let It Be", "Hey Jude", "Wish You Were Here", "Bohemian Rhapsody", "Don't Stop Me Now", "We Will Rock You", "Another Brick in the Wall", "Yellow Submarine", "Imagine", "Let It Be", "Rocket Man", "Sweet Caroline", "My Way", "Wonderwall", "Angie", "Bohemian Rhapsody", "Satisfaction", "Sultans of Swing", "Sympathy for the Devil", "Smells Like Teen Spirit", "Knockin' on Heaven's Door", "Under the Bridge", "Paint It Black", "Whole Lotta Love", "Come Together", "Hotel California", "Comfortably Numb", "Enter Sandman", "Sweet Home Alabama", "Bohemian Rhapsody", "Don't Stop Believin'", "Stairway to Heaven", "Imagine", "Every Breath You Take", "Hey Jude", "Wonderwall", "Smells Like Teen Spirit", "Billie Jean", "My Heart Will Go On", "The Sound of Silence", "Piano Man", "Angie", "Knockin' on Heaven's Door", "Under the Bridge", "Whole Lotta Love", "Come Together", "Paint It Black", "Enter Sandman", "Sweet Child o' Mine", "Like a Rolling Stone", "Purple Rain", "Let It Be", "Imagine", "Wish You Were Here", "Hallelujah", "Sweet Home Alabama", "Hotel California", "Another Brick in the Wall", "Yellow Submarine", "Rocket Man", "Sweet Caroline", "Wonderwall", "Angie", "Comfortably Numb", "Satisfaction", "Sultans of Swing", "Sympathy for the Devil", "Smells Like Teen Spirit", "Knockin' on Heaven's Door", "Under the Bridge", "Paint It Black", "Whole Lotta Love", "Come Together", "Hotel California", "Comfortably Numb", "Enter Sandman", "Sweet Home Alabama", "Bohemian Rhapsody", "Don't Stop Believin'", "Stairway to Heaven", "Imagine", "Every Breath You Take", "Hey Jude", "Wonderwall", "Smells Like Teen Spirit", "Billie Jean", "My Heart Will Go On", "The Sound of Silence", "Piano Man", "Angie", "Knockin' on Heaven's Door", "Under the Bridge", "Whole Lotta Love", "Come Together", "Paint It Black", "Enter Sandman", "Sweet Child o' Mine", "Like a Rolling Stone", "Purple Rain", "Let It Be", "Imagine", "Wish You Were Here", "Hallelujah", "Sweet Home Alabama", "Hotel California", "Another Brick in the Wall", "Yellow Submarine", "Rocket Man", "Sweet Caroline", "Wonderwall", "Angie", "Comfortably Numb", "Satisfaction", "Sultans of Swing", "Sympathy for the Devil", "Smells Like Teen Spirit", "Knockin' on Heaven's Door", "Under the Bridge", "Paint It Black", "Whole Lotta Love", "Come Together", "Hotel California", "Comfortably Numb", "Enter Sandman", "Sweet Home Alabama", "Bohemian Rhapsody", "Don't Stop Believin'", "Stairway to Heaven", "Imagine", "Every Breath You Take", "Hey Jude", "Wonderwall", "Smells Like Teen Spirit", "Billie Jean", "My Heart Will Go On", "The Sound of Silence", "Piano Man", "Angie", "Knockin' on Heaven's Door", "Under the Bridge", "Whole Lotta Love", "Come Together", "Paint It Black", "Enter Sandman", "Sweet Child o' Mine", "Like a Rolling Stone", "Purple Rain", "Let It Be", "Imagine", "Wish You Were Here", "Hallelujah", "Sweet Home Alabama", "Hotel California", "Another Brick in the Wall", "Yellow Submarine", "Rocket Man", "Sweet Caroline", "Wonderwall", "Angie", "Comfortably Numb", "Satisfaction", "Sultans of Swing", "Sympathy for the Devil", "Smells Like Teen Spirit", "Knockin' on Heaven's Door", "Under the Bridge", "Paint It Black", "Whole Lotta Love", "Come Together", "Hotel California", "Comfortably Numb", "Enter Sandman", "Sweet Home Alabama"]


# Fonction pour obtenir des suggestions de chansons aimées
def get_recommendations(song_names):
    suggestions = []
    random.shuffle(song_names)
    song_names_subset = song_names[:20]  # Utilisez une sous-liste pour éviter les délais d'exécution trop longs
    for song_name in song_names_subset:
        # Recherche de la chanson
        results = sp.search(q=song_name, limit=1)
        if results['tracks']['items']:
            track_info = results['tracks']['items'][0]
            # Récupérer les informations sur la chanson
            track_name = track_info['name']
            artist_name = track_info['artists'][0]['name']
            image_url = track_info['album']['images'][0]['url'] if track_info['album']['images'] else None
            # Ajouter la chanson à la liste des suggestions
            suggestions.append({'track': track_name, 'artist': artist_name, 'image_url': image_url})
    return suggestions

# Obtenir des suggestions de chansons aimées à partir de la liste pré-définie
recommended_songs = get_recommendations(song_names)

@app.route('/')
def index():
    return render_template('index.html', recommended_songs=recommended_songs)

if __name__ == '__main__':
    app.run(debug=True)
