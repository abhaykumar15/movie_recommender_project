import streamlit as st
import pandas as pd
import pickle

#def fetch_poster:

def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    # sorting with holding the index position using enumerates fun
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        movies_id = i[0] #collecting movie id
        #fetch poster from api of tmdb
        recommended_movies.append(movies.iloc[i[0]].original_title)
    return recommended_movies


movies_dict= pickle.load(open('movies_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title("movie recommender system")
selected_movie_name = st.selectbox('enter the movie you to get more movies like this'
                      ,movies['original_title'].values)
if st.button("Recommend"):
    recommendation=recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)