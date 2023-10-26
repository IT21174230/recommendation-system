import pandas as pd

def get_data():
    df=pd.read_csv('data_dir\imdb_top_1000.csv')
    dataf=df[['Poster_Link', 'Series_Title', 'Genre', 'Overview']].copy()
    dataf.dropna()

    X=dataf['Overview']
    return dataf,X