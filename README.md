Sentiment Analysis on Product Reviews

Description
This project is aimed at performing sentiment analysis on a dataset of product reviews. It utilises natural language processing (NLP) techniques to analyse the sentiment expressed in the reviews. By identifying positive and negative sentiments, the project provides insights into the overall perception of products based on customer reviews.

Table of Contents
- Installation
- Usage
- Credits

Installation
To run this project locally, follow these steps:
1. Clone the repository from GitHub:
    git clone https://github.com/yourusername/your-repository.git

2. Navigate to the project directory:
    cd your-repository

3. Install the required dependencies. You can use ‘pip’ to install them:
    pip install pandas, numpy, spacy, textblob, wordcloud, matplotlib

4. Download the spaCy English model:
    python -m spacy download en_core_web_sm

5. Download the dataset file (‘amazon_product_reviews.csv’) and place it in the project directory.

Usage
Once you have installed the project and its dependencies, you can use it as follows:
1. Run the Python script ‘sentiment_analysis.py’.
2. The script will load the Amazon product reviews dataset and perform sentiment analysis on the reviews.
3. After processing the data, the script will generate word clouds for positive and negative words, providing visual representations of the sentiment distribution.
4. Interpret the word clouds to understand the prevalent sentiments in the product reviews.

Credits
This project was created by me as part of my bootcamp tasks. Special thanks to my lecturers who helped me get this fare in coding and the developers of the libraries used in this project:
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [spaCy](https://spacy.io/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [WordCloud](https://github.com/amueller/word_cloud)
- [matplotlib](https://matplotlib.org/)
