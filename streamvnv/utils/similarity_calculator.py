from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from gensim.models import Doc2Vec
import numpy as np


model_path='models\doc.model'

loaded_model=Doc2Vec.load(model_path)

def get_similarity(user_in, X, model=loaded_model):
    similarities=[]
        
    new_doc_vec=model.infer_vector(word_tokenize(user_in.lower()))

    for i,x in enumerate(X):
        cos_sim=cosine_similarity([model.dv[i]], [new_doc_vec])
        similarities.append(cos_sim[0][0])
    
    similarities=np.array(similarities)
    highest_sim=np.argsort(-similarities)[:5]
    print(highest_sim)
    
    return highest_sim
  
    
    

