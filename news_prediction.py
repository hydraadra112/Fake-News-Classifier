from text_preprocessing import clean_text
def predict_news(classifier, vectorizer, input_text):
    preprocessed_text = clean_text(input_text)
    input_vector = vectorizer.transform([preprocessed_text])
    prediction = classifier.predict(input_vector)
    return prediction