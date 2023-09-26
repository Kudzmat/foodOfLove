import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

TINASHE_DATA = pd.read_csv('data/tinashe.csv')


# Get album lyrics from user input
def get_album_lyrics(album):
    album_lyrics = []  # empty list will hold all the lyrics from an album by track

    for index, row in TINASHE_DATA.iterrows():
        if row['album'] == album:
            lyrics = row['lyrics']
            album_lyrics.append(lyrics)

    return album_lyrics


def get_project_lyrics():
    proj_lyrics = []  # empty list will hold all the lyrics from an album by track

    for index, row in TINASHE_DATA.iterrows():
        lyrics = row['lyrics']
        if lyrics:
            proj_lyrics.append(lyrics)

    return proj_lyrics


# Processing the lyrics by cleaning the up
def process_lyrics(lyrics_list):
    processed = []
    custom_stopwords = ['yeah', 'ooh', 'nigga', 'ca', 'ai', 'shot', 'niggas', 'na', 'wan']
    for lyrics in lyrics_list:
        new_lyrics = lyrics.lower()
        tokens = word_tokenize(new_lyrics)
        # Remove punctuation and stopwords (both English and custom)
        tokens = [word for word in tokens if word.isalpha() and word.lower() not in stopwords.words(
            'english') and word.lower() not in custom_stopwords]
        processed.extend(tokens)  # Extend the list with the tokens
    return processed


def check_frequency(tokens):
    lyrics_count = {}  # This dictionary will hold a word and the number of times it appears
    word_frequency = Counter(tokens)
    # Find the 10 most common words
    most_common_words = dict(word_frequency.most_common(20))

    # Print the most common words and their frequencies
    for word, num in most_common_words.items():
        lyrics_count[word] = num

    return lyrics_count


def create_word_cloud(words):
    # Combine the words into a single string
    text = " ".join([word for word in words.keys()])

    # Generate the word cloud
    word_cloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate_from_frequencies(words)

    return word_cloud
