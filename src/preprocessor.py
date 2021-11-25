# author : Group 27 
# date : 2021-11-24

"""Reads data and performs and data cleaning/pre-processing, transforming, and partitioning that needs to happen before exploratory data analysis or modeling takes place
Usage: preprocessor.py --file_path=<file_path> --out_file=<out_file>

Options:
--file_path=<file_path>   Path to data file for which to perform preprocessing on
--out_file=<out_file>     Path (including filename) of where to locally write the file
"""

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

opt = docopt(__doc__)

def main(file_path, out_file):
    df = pd.read_csv(file_path)
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=123)
    X_train, y_train = train_df.drop(columns=["spotify_track_popularity"]), train_df["spotify_track_popularity"]
    X_test, y_test = test_df.drop(columns=["spotify_track_popularity"]), test_df["spotify_track_popularity"]
    
    text_features = "song"
    numeric_features = ["spotify_track_duration_ms",
                        "danceability",
                        "energy",
                        "key",
                        "loudness",
                        "mode",
                        "speechiness",
                        "acousticness",
                        "instrumentalness",
                        "liveness",
                        "valence",
                        "tempo",
                        "time_signature"]
    binary_features = ["spotify_track_explicit"]
    categorical_features = ["performer"]
    drop_features = ["song_id","spotify_track_id","spotify_track_preview_url","spotify_track_album"]
    target = "spotify_track_popularity"
    
    most_frequent = X_train["performer"].value_counts().iloc[:30]
    preprocessor = make_column_transformer(
    (make_pipeline(SimpleImputer(strategy='mean'),StandardScaler()),
                  numeric_features),
    (OneHotEncoder(sparse=False, drop="if_binary", dtype=int),binary_features),
    (make_pipeline(SimpleImputer(strategy="constant", fill_value="missing"),
                  OneHotEncoder(handle_unknown="ignore", sparse=False,categories=[most_frequent.index.values])),
                    categorical_features),
    (CountVectorizer(max_features =1000, stop_words='english'),text_features))
    
    transformed = preprocessor.fit_transform(X_train)
    
    column_names = (
    numeric_features
    + preprocessor.named_transformers_["onehotencoder"].get_feature_names_out().tolist()
    + preprocessor.named_transformers_["pipeline-2"]["onehotencoder"].get_feature_names_out().tolist()
    + preprocessor.named_transformers_["countvectorizer"].get_feature_names_out().tolist()
    )
    
    processed_data = pd.DataFrame(transformed.toarray(), columns=column_names, index=X_train.index)

    processed_data.to_csv(out_file, index = False)
    

if __name__ == "__main__":
  main(opt["--file_path"], opt["--out_file"])
