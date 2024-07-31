from flask import Flask, render_template, request, jsonify
import pandas as pd
from difflib import get_close_matches
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load movie data
movies_data = pd.read_csv('movies.csv')

# Feature selection
selected_features = ['genres', 'keywords', 'title', 'cast', 'vote_average', 'vote_count']

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Combine features
combined_features = (
    movies_data['genres'] + ' ' +
    movies_data['keywords'] + ' ' +
    movies_data['title'] + ' ' +
    movies_data['cast'] + ' ' +
    movies_data['vote_average'].astype(str) + ' ' +
    movies_data['vote_count'].astype(str)
)

# Vectorize features
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Cosine similarity
similarity = cosine_similarity(feature_vectors)

def recommend_movies(movie_name):
    # Find close match
    close_match = get_close_matches(movie_name, movies_data['title'].tolist(), n=1)
    
    if not close_match:
        return []

    close_match = close_match[0]

    # Find index of the movie
    index_of_the_movie = movies_data[movies_data['title'] == close_match].index[0]

    # Get similarity scores
    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    # Sort by similarity
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    # Get recommended movies
    recommended_movies = []
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data.iloc[index]['title']
        recommended_movies.append(title_from_index)

    return recommended_movies[1:31]  # Exclude the input movie from recommendations

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_movie_info', methods=['POST'])
def get_movie_info():
    movie_name = request.form.get('movie_name')
    
    # Assuming your movies_data DataFrame has columns like 'genres', 'keywords', etc.
    movie_info = movies_data[movies_data['title'] == movie_name][['genres', 'keywords']].to_dict('records')[0]
    
    return jsonify(movie_info)


@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    movie_name = request.form.get('movie_name')
    recommended_movies = recommend_movies(movie_name)
    return jsonify(recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
