import pickle
import pandas as pd
import numpy as np
import zipfile
import os
import gdown
import streamlit as st
import requests
import time
from typing import Tuple

# Configuration - REPLACE WITH YOUR ACTUAL GOOGLE DRIVE IDs
MOVIE_LIST_URL = "https://drive.google.com/uc?id=1NK5sFyJ8W_45g2-Q83yY2bCJdTjxHWJS"
SIMILARITY_URL = "https://drive.google.com/uc?id=1QkZIj-Cjtpi60CLmyBGdlXtggLFR1VUW"


def safe_remove(filepath: str, max_retries: int = 3) -> bool:
    """Safely remove a file with retries and delays"""
    for attempt in range(max_retries):
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                return True
        except PermissionError:
            if attempt < max_retries - 1:
                time.sleep(0.5 * (attempt + 1))
    return False


def download_file(url: str, output: str, max_retries: int = 3) -> bool:
    """Download file with retry logic and progress"""
    for attempt in range(max_retries):
        try:
            with st.spinner(f"Downloading {output} (attempt {attempt + 1}/{max_retries})..."):
                gdown.download(url, output, quiet=False)
                if os.path.exists(output) and os.path.getsize(output) > 0:
                    return True
                safe_remove(output)
        except Exception as e:
            st.warning(f"Download failed: {str(e)}")
            time.sleep(1)
    return False


@st.cache_data(ttl=24*3600)  # Cache for 24 hours
def load_data() -> Tuple[pd.DataFrame, np.ndarray]:
    """Download, extract and load data files with proper cleanup"""
    # Cleanup any existing temp files
    safe_remove("movie_list.zip")
    safe_remove("similarity.zip")

    # Load or download movie data
    if not os.path.exists("movie_list.pkl"):
        if not download_file(MOVIE_LIST_URL, "movie_list.zip"):
            st.error("❌ Failed to download movie data!")
            st.stop()

        with zipfile.ZipFile("movie_list.zip", "r") as zip_ref:
            zip_ref.extractall(".")
        safe_remove("movie_list.zip")

    # Load or download similarity data
    if not os.path.exists("similarity.pkl"):
        if not download_file(SIMILARITY_URL, "similarity.zip"):
            st.error("❌ Failed to download similarity data!")
            st.stop()

        with zipfile.ZipFile("similarity.zip", "r") as zip_ref:
            zip_ref.extractall(".")
        safe_remove("similarity.zip")

    # Load the data files
    with st.spinner("Loading data..."):
        try:
            movies = pickle.load(open("movie_list.pkl", "rb"))
            similarity = pickle.load(open("similarity.pkl", "rb"))
            return movies, similarity
        except Exception as e:
            st.error(f"Data loading failed: {str(e)}")
            st.stop()


def fetch_poster(movie_id: int) -> str:
    """Fetch movie poster from TMDB API with error handling"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    except Exception as e:
        st.warning(f"Couldn't fetch poster for movie ID {movie_id}: {str(e)}")
    return None


def recommend(movie: str, movies: pd.DataFrame, similarity: np.ndarray) -> Tuple[list, list]:
    """Generate movie recommendations with error handling"""
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])

        names = []
        posters = []
        for i in distances[1:6]:  # Top 5 similar movies
            movie_id = movies.iloc[i[0]].movie_id
            names.append(movies.iloc[i[0]].title)
            posters.append(fetch_poster(movie_id))

        return names, posters
    except Exception as e:
        st.error(f"Recommendation error: {str(e)}")
        return [], []


# Streamlit UI Configuration
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")


# Main App
def main():
    st.title("🎬 Movie Recommender System")
    st.markdown("Discover movies similar to your favorites!")

    # Load data (with caching)
    movies, similarity = load_data()

    # Movie selection
    selected_movie = st.selectbox(
        "Select a movie you like:",
        movies['title'].values,
        index=None,
        placeholder="Start typing...",
        key="movie_select"
    )

    # Recommendation button
    if st.button("Get Recommendations", type="primary"):
        if not selected_movie:
            st.warning("Please select a movie first!")
            return

        with st.spinner("Finding similar movies..."):
            names, posters = recommend(selected_movie, movies, similarity)

        if not names:
            st.error("No recommendations found. Try another movie.")
            return

        # Display results in columns
        cols = st.columns(5)
        for idx, (name, poster) in enumerate(zip(names, posters)):
            with cols[idx]:
                st.subheader(name)
                st.image(poster if poster else "https://via.placeholder.com/300x450?text=No+Poster",
                         width=200, caption=name)


if __name__ == "__main__":
    main()