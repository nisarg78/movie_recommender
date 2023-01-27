import streamlit as st
import pickle
import pandas as pd
import requests



def fetch_poster(movie_id):
    response =requests.get('https://api.themoviedb.org/3/movie/{}?api_key=52ba615e4c12f1da2dedb78f9c9b749f&language=en-US'.format(movie_id))
    data = response.json()
    # st.text(data)
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_lst = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:11]

    recommend_movies = []
    recommend_movies_poster = []
    for i in movie_lst:
        movie_id = movies.iloc[i[0]].movie_id
        
        recommend_movies.append(movies.iloc[i[0]].title)
        
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_poster

similarity = pickle.load(open('similarity1.pkl','rb'))
movie_lst = pickle.load(open('movies_dict.pkl','rb'))
# movie_lst = movie_lst['title'].values
movies = pd.DataFrame(movie_lst)


st.title('Movie Recommendation By Nisarg Zaveri')
st.write('Hello, *Devs!* :sunglasses:')
# selected_movies = st.selectbox(
#     'Wich type of movie you want to watch?',
#     (movies['title'].values))


selected_movies = st.multiselect(
    'What are your favorite colors (Only one Movie Allowed)',
    (movies['title'].values),[])
if selected_movies:
    st.text(selected_movies[0])

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# def remote_css(url):
#     st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

# local_css("style.css")
# remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# selected = st.text_input('Search Movies Here', "")
# button_clicked = st.button("OK")

# title = st.text_input('Movie Name','')
# st.write('The current movie title is', title)

if st.button('Recommend'):
    name,poster = recommend(selected_movies[0])
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:
        st.text(name[4])
        st.image(poster[4])

    # with col6:
    #     st.text(name[5])
    #     st.image(poster[5])

    # with col7:
    #     st.text(name[6])
    #     st.image(poster[6])

    # with col8:
    #     st.text(name[7])
    #     st.image(poster[7])

    # with col9:
    #     st.text(name[8])
    #     st.image(poster[8])

    # with col10:
    #     st.text(name[9])
    #     st.image(poster[9])                                                

# st.write('You selected:', selected_movies)
