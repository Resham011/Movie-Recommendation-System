# 🎬 Movie Recommender System

A simple and interactive **Movie Recommender Web App** built with **Streamlit**. It recommends movies based on content similarity using a pre-trained machine learning model.

---

## 🚀 Demo

Try the live app here:  
🔗 [https://your-deployment-link.com]([https://your-deployment-link.com](https://movie-recommendation-system-e8pjs6dvu6pcx6ctfhd3hj.streamlit.app/))

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

## 📁 Project Structure
movie-recommendation-system-app/
├── app.py # Streamlit app
├── model.ipynb # Notebook for training model
├── requirements.txt # All Python dependencies
├── README.md # This file


🔐 TMDB API Key
The app uses the TMDB API to fetch movie posters.

You can replace the API key inside the fetch_poster() function in app.py with your own.

🌐 Deployment Options
You can deploy this app using:
✅ Streamlit Cloud (Recommended)
☁️ Heroku
🌍 Render

✍️ Author
Made with ❤️ by Resham

⭐️ Show Your Support
If you found this project useful, consider giving it a ⭐️ on GitHub 🙌


