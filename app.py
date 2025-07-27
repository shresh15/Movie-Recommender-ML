
import streamlit as st
import pickle
import pandas as pd

# Load the full movies DataFrame
movies_df = pickle.load(open('movies.pkl', 'rb'))

# Get the titles list for selectbox
movies_list = movies_df['title'].values

# Load the similarity matrix
simi = pickle.load(open('simi.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies_list
)

def recommend(movie):
    # Find the index of the selected movie
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    # Get similarity scores
    distances = simi[movie_index]
    # Sort movies by similarity (excluding the selected movie itself)
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movie_indices:
       

        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)


