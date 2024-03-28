#  Program that performs sentiment analysis on a dataset of product reviews.
# Importing required libraries.
import pandas as pd
import numpy as np
import spacy
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import defaultdict

# Loading spaCy model.
nlp = spacy.load("en_core_web_sm")

# Loading amazon product reviews dataset.
amazon_df = pd.read_csv("amazon_product_reviews.csv")

# Selecting the 'review.text' column.
reviews_data = amazon_df[["reviews.text"]]

# Removing missing values.
reviews_data.isnull().sum()

text = reviews_data["reviews.text"]

# Preprocessing function to clean text.
def preprocess(text):
    # Removing stopwords, punctuation, tokenize, convert to lowercase and perform basic text cleaning.
    doc = nlp(text.lower().strip())
    processed = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(processed)

# Applying preprocessing to the reviews.
reviews_data["processed.text"] = reviews_data["reviews.text"].apply(preprocess)

# Initialise dictionaries to hold positive and negative words.
positive_words = defaultdict(int)
negative_words = defaultdict(int)

# Function for sentiment analysis using spaCyTextBlob.
for sentence in reviews_data["processed.text"]:
    doc = nlp(sentence)
    tokens = [token.lemma_.lower().strip() for token in doc if not token.is_stop and token.is_alpha]
    for token in tokens:
        blob = TextBlob(str(token))
        polarity = blob.sentiment.polarity
        if polarity > 0:
            positive_words[token.lower()] += 1
        if polarity < 0:
            negative_words[token.lower()] += 1

# Generating word clouds for positive and negative words.
pos_wordcloud = WordCloud(width=600, height=400, background_color ='white').generate_from_frequencies(positive_words)
neg_wordcloud = WordCloud(width=600, height=400, background_color ='white').generate_from_frequencies(negative_words)
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Displaying positive word cloud.
ax[0].imshow(pos_wordcloud, interpolation='bilinear')
ax[0].set_title('Positive Words')
ax[0].axis('off')

# Displaying negative word cloud.
ax[1].imshow(neg_wordcloud, interpolation='bilinear')
ax[1].set_title('Negative Words')
ax[1].axis('off')

plt.show()
