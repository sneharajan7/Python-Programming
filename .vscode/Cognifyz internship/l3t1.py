import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
import string

def analyze_reviews(csv_file_path):
    try:
        # Task 1: Read the CSV file
        df = pd.read_csv(csv_file_path)

        # Task 2: Tokenization and Text Processing
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        reviews = df['Reviews'].dropna().apply(lambda x: word_tokenize(x.lower()))
        reviews = reviews.apply(lambda x: [lemmatizer.lemmatize(word) for word in x if word not in stop_words and word not in string.punctuation])

        # Task 3: Sentiment Analysis
        sid = SentimentIntensityAnalyzer()
        reviews_sentiment = reviews.apply(lambda x: 'Positive' if sid.polarity_scores(' '.join(x))['compound'] > 0 else 'Negative')

        # Task 4: Keyword Extraction
        positive_keywords = []
        negative_keywords = []

        for review in reviews:
            for word in review:
                if sid.polarity_scores(word)['compound'] > 0:
                    positive_keywords.append(word)
                elif sid.polarity_scores(word)['compound'] < 0:
                    negative_keywords.append(word)

        positive_keywords_freq = pd.Series(positive_keywords).value_counts().head(10)
        negative_keywords_freq = pd.Series(negative_keywords).value_counts().head(10)

        # Task 5: Review Length Analysis
        review_lengths = df['Reviews'].dropna().apply(lambda x: len(word_tokenize(x)))
        avg_review_length = review_lengths.mean()

        return {
            "Positive Keywords": positive_keywords_freq,
            "Negative Keywords": negative_keywords_freq,
            "Average Review Length": avg_review_length,
            "Sentiment Analysis": reviews_sentiment.value_counts()
        }
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
csv_file_path = r"C:\Users\sneha\OneDrive\Desktop\Python\.vscode\Dataset .csv"  # Replace with the absolute path to your CSV file
review_analysis_results = analyze_reviews(csv_file_path)
if review_analysis_results is not None:
    print("Positive Keywords:")
    print(review_analysis_results["Positive Keywords"])
    print("\nNegative Keywords:")
    print(review_analysis_results["Negative Keywords"])
    print("\nAverage Review Length:", review_analysis_results["Average Review Length"])
    print("\nSentiment Analysis:")
    print(review_analysis_results["Sentiment Analysis"])
else:
    print("Failed to analyze reviews.")
