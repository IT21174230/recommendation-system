from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

def train_doc2vec_model(X, model_path):
    tagged_data = [TaggedDocument(words=word_tokenize(doc.lower()), tags=[i]) for i, doc in enumerate(X)]
    model = Doc2Vec(vector_size=50, min_count=2, epochs=50)
    model.build_vocab(tagged_data)
    model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)
    model.save('../models/doc.model')
    return model
