from string import punctuation
from nltk.corpus import stopwords
def clean_text(text):
    nopunc = [word for word in text.split() if word not in punctuation]
    clean_words = [word for word in nopunc if word.lower() not in stopwords.words('english')]
    return ' '.join(clean_words)