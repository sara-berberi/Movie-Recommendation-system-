# Movie Recommendation System 🎬🍿

Welcome to the Movie Recommendation System! This Flask-based web application suggests movies based on your input. Utilizing a content-based recommendation engine, it leverages movie data to provide personalized suggestions. The system is built using Python and leverages TF-IDF vectorization and cosine similarity for accurate recommendations.

## 🛠️ Features

- **Movie Recommendations**: Get personalized movie suggestions based on your input movie title.
- **Movie Information**: Retrieve details about a specific movie, including genres and keywords.
- **Content-Based Filtering**: Uses TF-IDF and cosine similarity to recommend similar movies.

## 🚀 Getting Started

### Prerequisites

To run this application, you'll need:

- Python 3.x
- Flask
- pandas
- scikit-learn

### Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare the Data**:

    Ensure you have a `movies.csv` file with the appropriate columns (e.g., genres, keywords, title, cast, vote_average, vote_count) in the root directory.

### Running the App

1. **Start the Flask Server**:

    ```bash
    python app.py
    ```

2. **Open in Browser**:

    Navigate to `http://127.0.0.1:5000/` in your web browser to access the app.

### Usage

- **Home Page**: Enter a movie title to get recommendations or information about the movie.
- **Get Movie Info**: Submit a movie title to receive details about genres and keywords.
- **Get Recommendations**: Submit a movie title to receive a list of recommended movies based on your input.

## 📜 API Endpoints

- **GET /**: Renders the homepage.
- **POST /get_movie_info**: Retrieves movie information (genres, keywords) for the provided movie title.
- **POST /get_recommendations**: Provides a list of recommended movies based on the given movie title.

## 🤝 Contributing

Contributions are welcome! If you'd like to add features or improve the app, please fork the repository and submit a pull request. For significant changes, please open an issue to discuss your ideas.

## 📬 Contact

For questions or support, please reach out by opening an issue on the repository.

## 🙏 Acknowledgments

- **Flask**: Web framework used for building the application.
- **pandas**: Data manipulation library for handling movie data.
- **scikit-learn**: Machine learning library used for TF-IDF vectorization and cosine similarity.

Thank you for checking out this project! 🎉 Enjoy discovering your next favorite movie!
