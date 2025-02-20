import streamlit as st
import pandas as pd
import pickle
import requests
import numpy as np

# API Key
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

# Load Data
similarity = pickle.load(open("similarity.pkl", "rb"))
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

# Precompute movie index for O(1) lookup
movie_index_map = {title: index for index, title in enumerate(movies['title'])}

@st.cache_data
def fetchPoster(movie_title):
    # Check if poster is preloaded
    movie_row = movies[movies['title'] == movie_title]
    if not movie_row.empty and 'poster_path' in movie_row:
        return "https://image.tmdb.org/t/p/w500/" + movie_row.iloc[0]['poster_path']
    
    # Fetch from API if not found
    try:
        response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}")
        data = response.json()
        if data['results']:
            return "https://image.tmdb.org/t/p/w500/" + data['results'][0]['poster_path']
    except:
        return "https://via.placeholder.com/500x750?text=Error+Fetching+Image"

    return "https://via.placeholder.com/500x750?text=No+Image"

@st.cache_data
def recommend(movie_title):
    movie_index = movie_index_map.get(movie_title)
    if movie_index is None:
        return []

    distances = similarity[movie_index]

    # Fast sorting using NumPy
    sorted_indices = np.argsort(-distances)[1:6]  

    recommended_movies = [movies.iloc[i].title for i in sorted_indices]
    # recommended_movies_poster = [fetchPoster(movie) for movie in recommended_movies]

    return recommended_movies

st.title("🎬 Movie Recommender System")

# Select Movie
option = st.selectbox("Select a movie from the dropdown", movies['title'].values)

# Recommendation Button
if st.button("Recommend"):
    recommended_movies = recommend(option)
    
    st.subheader("📽️ Recommended Movies:")
    
    for movie in recommended_movies:
        st.write(f"🎥 {movie}")
