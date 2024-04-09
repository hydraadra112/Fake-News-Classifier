from text_preprocessing import clean_text
from model_loading import load_classifier, load_vectorizer
from news_prediction import predict_news

# Import classifier and vectorizer
classifier = load_classifier('models/fake_news_classifier.joblib')
vectorizer = load_vectorizer('models/vectorizer.joblib')

# Sample text to classify
sample_text = "New Study Claims Eating Chocolate Every Day Can Lead to Weight Loss!"

prediction = predict_news(classifier, vectorizer, sample_text)[0]

print("Not Fake News") if prediction != 0 else print("Fake News")