# 🎬 Movie Recommender System

A Streamlit-powered web app that recommends similar movies based on user preferences, using collaborative filtering and TMDB API for posters.

![Demo]([https://via.placeholder.com/800x400?text=Movie+Recommender+Demo](https://movie-recommendation-system-e8pjs6dvu6pcx6ctfhd3hj.streamlit.app/))

## 🚀 Features
- Recommends 5 similar movies based on user selection
- Fetches high-quality movie posters from TMDB
- Fast and lightweight with caching
- Works with both public and private datasets

## 📦 Installation
1. Clone the repository:
    git clone [https://github.com/yourusername/movie-recommender](https://github.com/Resham011/Movie-Recommendation-System).git
2. Install dependencies:
    pip install -r requirements.txt
3. Create and activate virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

🖥️ Usage
Run the app locally:
  streamlit run app.py

🌐 Live Demo
[https://static.streamlit.io/badges/streamlit_badge_black_white.svg](https://movie-recommendation-system-e8pjs6dvu6pcx6ctfhd3hj.streamlit.app/)

🛠️ Project Structure
text
movie-recommender/
├── app.py                # Main application code
├── model.ipynb           # Notebook to train model
├── requirements.txt      # Python dependencies
└── README.md             # This file

🧠 How It Works
  Uses content-based filtering (based on movie tags & metadata)
  Trained on TMDB 5000 Movies & Credits
  Uses cosine similarity for recommendations
  Shows movie posters and names using TMDB API

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

📜 License
MIT

⭐️ Show Some Love
If you found this helpful, please consider giving it a ⭐️ on GitHub!
