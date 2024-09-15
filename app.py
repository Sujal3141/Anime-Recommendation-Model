import streamlit as st
import pickle
import pandas as pd
from jikanpy import Jikan
from jikanpy.exceptions import APIException

jikan = Jikan()
def recommend(anime_name):
    anime_index = anime[anime['Title']==anime_name].index[0]
    distances = similar[anime_index]
    anime_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_anime = []
    for i in anime_list:
        recommended_anime.append(anime.iloc[i[0]].Title)
    return recommended_anime
 
anime_dict = pickle.load(open('anime.pkl','rb'))
anime = pd.DataFrame(anime_dict)


similar = pickle.load(open('similar.pkl','rb'))

st.title('Anime Recommender System')

selected_anime = st.selectbox(
    'Select your favourite anime ',
    anime['Title'].values)

if st.button('Recommend anime '):
    recommendation = recommend(selected_anime)
    for i in recommendation:
        
        st.write(i)
        
