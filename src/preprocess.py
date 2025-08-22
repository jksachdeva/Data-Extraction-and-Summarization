import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import nltk
from nltk.corpus import stopwords
import string

# Ensure stopwords are downloaded
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

def basic_info(df: pd.DataFrame):
    """
    Displays basic information about the DataFrame.
    """
    print("DataFrame shape:", df.shape)
    print("Sample records:\n", df.head())
    print("Missing values by column:\n", df.isnull().sum())

def plot_category_distribution(df: pd.DataFrame):
    """
    Plots the distribution of news categories.
    """
    plt.figure(figsize=(12, 6))
    sns.countplot(
        y='category',
        data=df,
        order=df['category'].value_counts().index
    )
    plt.title('Distribution of News Categories')
    plt.tight_layout()
    plt.show()

def plot_description_length(df: pd.DataFrame, col: str = 'short_description'):
    """
    Adds a 'desc_length' column and plots its distribution.
    """
    df['desc_length'] = df[col].apply(lambda x: len(str(x).split()))
    plt.figure(figsize=(8, 4))
    sns.histplot(df['desc_length'], bins=30, kde=True)
    plt.title('Distribution of Short Description Length')
    plt.xlabel('Number of Words')
    plt.tight_layout()
    plt.show()

def get_top_words(texts, n=10):
    """
    Returns top n words (excluding stopwords and punctuation) from a list of texts.
    """
    words = []
    for txt in texts:
        words.extend([
            word.lower() for word in str(txt).split()
            if word.lower() not in stop_words and word not in string.punctuation
        ])
    return Counter(words).most_common(n)

def category_top_words_report(df: pd.DataFrame, n: int = 10, limit: int = 5, desc_col: str = 'short_description'):
    """
    Prints top words for the first `limit` categories based on the description column.
    """
    categories = df['category'].unique()[:limit]
    for cat in categories:
        top_words = get_top_words(df[df['category'] == cat][desc_col], n=n)
        print(f"Top words for category '{cat}':")
        for word, count in top_words:
            print(f"{word}: {count}")
        print("-" * 30)