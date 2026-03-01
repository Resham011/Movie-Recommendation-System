import pickle
import pandas as pd
import numpy as np
import streamlit as st
import requests
from typing import Tuple

# --- DATA LOADING ---
@st.cache_resource 
def load_data() -> Tuple[pd.DataFrame, np.ndarray]:
    """Loads local data files directly without downloading or showing spinners"""
    try:
        # These files must be in the same folder as app.py
        movies = pickle.load(open("movie_list.pkl", "rb"))
        similarity = pickle.load(open("similarity.pkl", "rb"))
        return movies, similarity
    except FileNotFoundError:
        st.error("❌ Error: 'movie_list.pkl' or 'similarity.pkl' not found in the project folder.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Data loading failed: {str(e)}")
        st.stop()

def fetch_poster(movie_id: int) -> str:
    """Fetch movie poster from TMDB API"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    except Exception:
        return None
    return None

def recommend(movie: str, movies: pd.DataFrame, similarity: np.ndarray) -> Tuple[list, list]:
    """Generate movie recommendations"""
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])

        names = []
        posters = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            names.append(movies.iloc[i[0]].title)
            posters.append(fetch_poster(movie_id))

        return names, posters
    except Exception as e:
        st.error(f"Recommendation error: {str(e)}")
        return [], []

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

def main():
    st.title("🎬 Movie Recommender System")
    st.markdown("Discover movies similar to your favorites!")

    # Load data silently behind the scenes
    movies, similarity = load_data()

    selected_movie = st.selectbox(
        "Select a movie you like:",
        movies['title'].values,
        index=None,
        placeholder="Start typing...",
        key="movie_select"
    )

    if st.button("Get Recommendations", type="primary"):
        if not selected_movie:
            st.warning("Please select a movie first!")
            return

        with st.spinner("Finding similar movies..."):
            names, posters = recommend(selected_movie, movies, similarity)

        if not names:
            st.error("No recommendations found.")
            return

        cols = st.columns(5)
        for idx, (name, poster) in enumerate(zip(names, posters)):
            with cols[idx]:
                st.text(name)
                st.image(poster if poster else "https://via.placeholder.com/300x450?text=No+Poster")

if __name__ == "__main__":
    main()