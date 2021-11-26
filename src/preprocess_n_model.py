# author : Group 27 
# date : 2021-11-25

"""Performs some statistical or machine learning analysis and summarizes the results as a figure(s) and a table(s)
Usage: preprocess_n_model.py --file_path=<file_path> --out_file=<out_file>

Options:
--file_path=<file_path>   Path to train processed data file for which to perform preprocessing on
--out_file=<out_file>     Path (including filename) of where to locally write the file
"""

import altair as alt
import pandas as pd
import os
from docopt import docopt
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import (
    OneHotEncoder,
    OrdinalEncoder,
    StandardScaler,
)

pt = docopt(__doc__)

def main(file_path, out_file):
    df = pd.read_csv(file_path)
    X_train, y_train = df.drop(columns=["spotify_track_popularity"]), df["spotify_track_popularity"]
    
    
    numeric_features  = [
        'spotify_track_duration_ms',
        'danceability',
        'energy','key',
        'loudness','mode',
        'speechiness',
        'acousticness',
        'instrumentalness',
        'liveness',
        'valence',
        'tempo',
        'time_signature']
    categorical_features = ['performer']
    binary_features = ['spotify_track_explicit']
    drop_features = ['song_id', 'spotify_track_id', 'spotify_track_album']


    preprocessor = make_column_transformer(
        (StandardScaler(), numeric_features),
        (OneHotEncoder(handle_unknown="ignore"), categorical_features),
        (OneHotEncoder(drop='if_binary', handle_unknown="ignore"), binary_features),
        (CountVectorizer(max_features = 20000, stop_words="english"), "spotify_genre"),
        (CountVectorizer(max_features = 20000, stop_words="english"), "song"),
        ("drop", drop_features)
    )







    y_test = np.random.randint(100, size=100)
    y_predicted = np.random.randint(100, size=100)

    df = pd.DataFrame({'y_test':y_test, 'y_predicted':y_predicted})
    p = alt.Chart(df).mark_point(filled=True).encode(
    alt.X('y_test', title='Predicted values of Spotify popularities'),
    alt.Y('y_predicted', title='True values of Spotify popularities')
    )

    p2 = p+p.transform_regression('y_test', 'y_predicted').mark_line()
    p2.save('test.png')

















if __name__ == "__main__":
  main(opt["--file_path"], opt["--out_file"])













