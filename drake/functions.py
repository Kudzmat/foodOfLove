import pandas as pd
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

DRAKE_DATA = pd.read_csv('data/drake_data.csv')
NEW_DRAKE = pd.read_csv('data/dogs.csv')


# Get album lyrics from user input
def get_album_lyrics(album):
    other_albums = ['Her Loss', 'For All The Dogs', 'Honestly Nevermind']  # albums not in DRAKE_DATA
    album_lyrics = []  # empty list will hold all the lyrics from an album by track

    if album in other_albums:
        for index,row in NEW_DRAKE.iterrows():
            if row['album'] == album:
                lyrics = row['lyrics']
                album_lyrics.append(lyrics)
    else:

        # check for album data in DRAKE_DATA
        for index, row in DRAKE_DATA.iterrows():
            if row['album'] == album:
                lyrics = row['lyrics']
                album_lyrics.append(lyrics)

    return album_lyrics


def get_project_lyrics():
    proj_lyrics = []  # empty list will hold all the lyrics from an album by track

    for index, row in DRAKE_DATA.iterrows():
        lyrics = row['lyrics']
        if lyrics:
            proj_lyrics.append(lyrics)

    return proj_lyrics


# Processing the lyrics by cleaning the up
def process_lyrics(lyrics_list):
    processed = []
    custom_stopwords = ['yeah', 'oh', 'nigga', 'chorus', 'verse', 'Drake', 'drake', 'niggas', 'started', 'bottom', 'ai',
                        'wan', 'na', 'ca', "fuck", "shit", "bitch", "ass", "ayy"]
    for lyrics in lyrics_list:

        if type(lyrics) == str:
            new_lyrics = lyrics.lower()
            tokens = word_tokenize(new_lyrics)

            # Remove punctuation and stopwords (both English and custom)
            tokens = [word for word in tokens if word.isalpha() and word.lower() not in stopwords.words(
                'english') and word.lower() not in custom_stopwords]
            processed.extend(tokens)  # Extend the list with the tokens

        else:
            pass

    return processed


def check_frequency(tokens):
    lyrics_count = {}  # This dictionary will hold a word and the number of times it appears
    word_frequency = Counter(tokens)
    # Find the 10 most common words
    most_common_words = dict(word_frequency.most_common(25))

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
