# 🎬 Movie Recommender System

A simple and interactive **Movie Recommender Web App** built with **Streamlit**. It recommends movies based on content similarity using a pre-trained machine learning model.

---

## 🚀 Demo

Try the live app here:  
🔗[https://movie-recommendation-system.com](https://movie-recommendation-system-e8pjs6dvu6pcx6ctfhd3hj.streamlit.app/)

---

## 📌 Features

- Recommend top 5 similar movies
- Fetch movie posters using **TMDB API**
- Trained with:
  - Content-based filtering
  - Cosine similarity
  - TMDB 5000 dataset

Built with:
- 🐍 Python
- 🧠 scikit-learn, pandas
- 🌐 Streamlit
- 🧵 Pickle (model storage)

---

## 🧠 How It Works

1. Data is cleaned and combined into a single feature "tags"
2. TF-IDF or CountVectorizer is used to convert text to numerical form
3. Cosine similarity is calculated between movies
4. Based on your selected movie, it recommends 5 most similar ones
5. Posters fetched dynamically from TMDB API

---
## 📊 Dataset Source

This project uses the **TMDB 5000 Movie Dataset** from Kaggle:

- 📂 [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Files used:
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`

---

## 🔐 TMDB API Key
The app uses the TMDB API to fetch movie posters.

## 🌐 Deployment 
✅ Streamlit Cloud

## ✍️ Author
Made with ❤️ by Resham

⭐️ Show Your Support
If you found this project useful, consider giving it a ⭐️ on GitHub 🙌


