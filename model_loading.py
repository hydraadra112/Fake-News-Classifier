from joblib import load
def load_classifier(filename):
    return load(filename)

def load_vectorizer(filename):
    return load(filename)