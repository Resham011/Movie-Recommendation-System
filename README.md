# 🎬 Movie Recommender System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://huggingface.co/spaces/Resham2987/Movie-Recommendation-System)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B.svg)](https://movie-recommendation-system-hn4hvhjrnwztxkirccax6e.streamlit.app/)

## 📖 Overview
This project is a **Content-Based Movie Recommender System** that analyzes movie metadata to suggest similar content. Using the TMDB 5000 Movies dataset, the system processes over 5,000 films to find meaningful connections between genres, cast, crew, and plot descriptions.

## 🧠 Machine Learning & NLP Workflow
To build this engine, I implemented a robust Natural Language Processing (NLP) pipeline:

### 1. Data Engineering
* **Feature Extraction**: Combined `overview`, `genres`, `keywords`, `cast` (top 3 actors), and `crew` (director) into a single "tags" column.
* **Text Preprocessing**: Applied lowercasing and handled special characters to ensure consistency.

### 2. Vectorization (Bag of Words)
* **Technique**: Used `CountVectorizer` from `scikit-learn`.
* **Strategy**: Converted text tags into 5,000-dimensional numerical vectors, removing standard English stop words to focus on unique movie identifiers.

### 3. Similarity Measurement (Cosine Similarity)
* Instead of Euclidean distance, I utilized **Cosine Similarity** to measure the distance between movie vectors.
* **The Logic**: In high-dimensional space, the angle between vectors (cosine) is a more accurate representation of content similarity than the straight-line distance.

## 🏗️ Engineering & Deployment Challenges
* **Git LFS Integration**: The similarity matrix (`similarity.pkl`) exceeded standard Git limits. I implemented **Git LFS** to track and version large model weights seamlessly.
* **Optimization**: Migrated the app from dynamic cloud downloading to local pre-bundled assets, reducing the application boot time by 90%.
* **API Integration**: Integrated the **TMDB API** to dynamically fetch movie posters based on ID, enhancing the visual experience.

## 📂 Project Structure
```text
├── app.py                # Main Streamlit UI & Logic
├── model.ipynb           # Data Analysis, Preprocessing & Model Training
├── movie_list.pkl        # Processed Movie DataFrame
├── similarity.pkl        # Pre-computed Similarity Matrix (via Git LFS)
├── requirements.txt      # Python Dependencies
└── README.md             # Project Documentation
```

## 🚀 How to Run Locally

1. **Clone the repository:**
```bash
git clone https://github.com/Resham011/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the Application:**
```bash
streamlit run app.py
```

## 🌐 Live Demos
| Platform | Link |
|----------|------|
| 🤗 Hugging Face Spaces | [Movie-Recommendation-System](https://huggingface.co/spaces/Resham2987/Movie-Recommendation-System) |
| ☁️ Streamlit Cloud | [Live App](https://movie-recommendation-system-hn4hvhjrnwztxkirccax6e.streamlit.app/) |

## 🛠️ Tech Stack
* **Core**: Python, Pandas, NumPy
* **Machine Learning**: Scikit-Learn (CountVectorizer, Cosine Similarity)
* **Web Framework**: Streamlit
* **Version Control**: Git & Git LFS
* **Hosting**: Hugging Face Spaces & Streamlit Cloud

## 👤 Author
**Resham**
* 💼 LinkedIn: [linkedin.com/in/resham-3b438a281](https://www.linkedin.com/in/resham-3b438a281/)
* 🐙 GitHub: [github.com/Resham011](https://github.com/Resham011)
