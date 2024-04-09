# Fake News Classifier with Multinomial Naive Bayes

Welcome to the Fake News Classifier, an NLP model designed to distinguish between real and fake news articles. 
Leveraging the power of Multinomial Naive Bayes, this model is trained to analyze text data and make accurate 
predictions regarding the authenticity of news content. Whether you're concerned about misinformation or simply want 
to verify the credibility of news articles, our classifier is here to help. Join us in the fight against fake news with 
the precision and reliability of Multinomial Naive Bayes.  

### Dependencies
* sklearn: 1.2.1
* matplotlib: 3.6.3
* seaborn: 0.12.2
* pandas: 1.5.3
* nltk: 3.8.1
* joblib: 1.2.1 (under sklearn)

### Installation:
> `git clone https://github.com/hydraadra112/Fake-News-Classifier.git`

### How to Use:
* Load the classifier and vectorizer in the models folder, by using `model_loading.py` script
* Then input your text to the `predict_news(classifier, vectorizer, text)` method, from the *news_prediction* module.
* If it returns 0, the text is classified as fake news, otherwise, no.
* Users can use the `main_script.py` as a reference point to create their own script to classify fake news.

# Thank you!
For questions, you can email me at `carado.johnp11q@gmail.com`
