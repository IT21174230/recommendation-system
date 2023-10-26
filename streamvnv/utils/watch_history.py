from utils.data_loader import get_data
from utils.similarity_calculator import get_similarity
import pandas as pd
import random

dataf,X=get_data()

def watch_history_generator(df=dataf):
    movies_history = dataf.sample(n=20, random_state=42).reset_index(drop=True)
    for i in movies_history:
        print(i)
    return movies_history


def get_recs_on_history():
    history=watch_history_generator()
    
    recommendations=[]
    
    for i in history['Overview']:
    #    print(i)
    
        rec=get_similarity(i,X)
        recommendations.extend(rec)
        
    random_recs = random.sample(recommendations, 10)
    return random_recs
    


    