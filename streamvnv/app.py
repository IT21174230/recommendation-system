import streamlit as st

from utils.data_loader import get_data
from utils.model_trainer import train_doc2vec_model
from utils.similarity_calculator import get_similarity
from utils.watch_history import get_recs_on_history

    
dataf,X=get_data()

def process_input(user_in, dataf, X):
    
    filtered_data = dataf.loc[dataf['Series_Title'].str.lower() == user_in.lower(), 'Overview'].values

    if len(filtered_data) > 0:
        user_in = filtered_data[0]

        return(get_similarity(user_in, X))
        
    else:
        st.write('error occured')
    
  
st.title("My Movie List")
st.write ('Never lose track of what you watched')

  
  
col1, col2 = st.columns(2)

with col1:
    user_input = st.text_input("Enter what you last watched (or even your favourite!):")

    submitted=st.button('See more like this!')

highest_sim=[]
if submitted:
    highest_sim.extend(process_input(user_input, dataf, X))
    
    with col2:
        st.write(f"here's some more like {user_input}")
            
        for i in highest_sim:
            row=dataf.iloc[i]
            st.image(row[0])
            st.write(row[1:4])

hist_rec=get_recs_on_history()

st.write('Here are more based on what you have watched:') 
for i in hist_rec:
            row=dataf.iloc[i]
            st.image(row[0])
            st.write(row[1:4])