🎬 Movies Recommendation System

📌 Overview

The Movies Recommendation System is a web application built with Streamlit that suggests similar movies based on user-selected input. The recommendation is powered by machine learning algorithms using a precomputed similarity matrix.

🚀 Features

🔍 Movie Search: Select a movie from the dropdown.

🎭 Personalized Recommendations: Get 5 similar movies based on the selected title.

📷 Movie Posters: Fetches posters from The Movie Database (TMDb) API.

⚡ Fast & Optimized: Uses cached recommendations for better performance.

🛠️ Technologies Used

Python (for backend logic)

Streamlit (for UI/UX)

Pandas (for data processing)

Scikit-learn (for similarity calculations)

Requests (for API calls to TMDb)

Pickle (for storing precomputed similarity matrices)

📂 Project Structure

📂 Movies-Recommend-System
│── app.py               # Main Streamlit application
│── movies_dict.pkl      # Movie dataset (Pickle file)
│── similarity.pkl       # Precomputed similarity matrix (Pickle file)
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation

🎯 How to Run Locally

1️⃣ Clone the Repository

git clone https://github.com/Abdullah-Khawar/Movies-Recommend-System.git
cd Movies-Recommend-System

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Streamlit App

streamlit run app.py

📌 Credits

The Movie Database (TMDb) for movie data.

Streamlit for an interactive UI.

📢 Star⭐ this repo if you find it useful! 🙌

