# App 
import pickle
import streamlit as st

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies=[]
   
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
       


st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",movies
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    #col1, col2, col3, col4, col5 = st.columns(5)
    col=st.columns(1)[0]
    with col: 
        st.text(recommended_movie_names[0])
        st.text(recommended_movie_names[1])
        st.text(recommended_movie_names[2])
        st.text(recommended_movie_names[3])
        st.text(recommended_movie_names[4])