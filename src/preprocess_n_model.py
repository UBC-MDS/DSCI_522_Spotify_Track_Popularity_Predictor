# author : Group 27 
# date : 2021-11-25

"""Performs some statistical or machine learning analysis and summarizes the results as a figure(s) and a table(s)
Usage: preprocess_n_model.py --file_path=<file_path> --out_file=<out_file>

Options:
--file_path=<file_path>   Path to train processed data file for which to perform preprocessing on
--out_file=<out_file>     Path (including filename) of where to locally write the file
"""

import altair as alt
import numpy as np
import pandas as pd
import os
from docopt import docopt
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression, Ridge, RidgeCV
from sklearn.preprocessing import (
    OneHotEncoder,
    OrdinalEncoder,
    StandardScaler,
)
from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV,
    ShuffleSplit,
    cross_val_score,
    cross_validate,
    train_test_split,
)

opt = docopt(__doc__)

def main(file_path, out_file):

    df_train = pd.read_csv(f'{file_path}/train_df.csv')
    df_test = pd.read_csv(f'{file_path}/test_df.csv')
    X_train, y_train = df_train.drop(columns=["spotify_track_popularity"]), df_train["spotify_track_popularity"]
    X_test, y_test = df_test.drop(columns=["spotify_track_popularity"]), df_test["spotify_track_popularity"]
    
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

    pipe = make_pipeline(preprocessor, Ridge())
    cv_df = pd.DataFrame(cross_validate(pipe, X_train, y_train, cv=10, return_train_score=True))

    try:
        cv_df.to_csv(f'{out_file}/cv_df.csv', index = False)    # save the cv file 
    except:
        os.makedirs(os.path.dirname(f'{out_file}/cv_df.csv'))
        cv_df.to_csv(f'{out_file}/cv_df.csv', index = False)
    

    #random seach hyperparameters model tunning
    
    param_grid = {
        "ridge__alpha": np.logspace(-3,2,6),
        "columntransformer__countvectorizer-1__binary": np.array([True, False]),
        "columntransformer__countvectorizer-1__max_features": np.arange(1000, 10000, 20000),
        "columntransformer__countvectorizer-2__binary": np.array([True, False]),
        "columntransformer__countvectorizer-2__max_features": np.arange(1000, 10000, 20000)
    }

    random_search = RandomizedSearchCV(
        pipe, param_distributions=param_grid, n_jobs=-1, n_iter=10, cv=5
    )
    
    random_search.fit(X_train, y_train)

    random_search_results = pd.DataFrame(random_search.cv_results_)[
        [
            "mean_test_score",
            "param_ridge__alpha",
            "param_columntransformer__countvectorizer-1__max_features",
            "param_columntransformer__countvectorizer-1__binary",
            "param_columntransformer__countvectorizer-2__max_features",
            "param_columntransformer__countvectorizer-2__binary",
            "rank_test_score",
        ]
    ].set_index("rank_test_score").sort_index()
  
    try:
        random_search_results.to_csv(f'{out_file}/best_hyperparameters.csv', index = False)   # save the random_search results
    except:
        os.makedirs(os.path.dirname(f'{out_file}/best_hyperparameters.csv'))
        random_search_results.to_csv(f'{out_file}/best_hyperparameters.csv', index = False)
    

    #Evaluating on the test set 
    y_predicted = random_search.predict(X_test)
    df = pd.DataFrame({'y_test':y_test, 'y_predicted':y_predicted})

    plot = alt.Chart(df, title= "Predicted versus true Spotify popularities").mark_point(filled=True, clip=True).encode(
        alt.X('y_test', title='Predicted values of Spotify popularities'),
        alt.Y('y_predicted', title='True values of Spotify popularities', scale=alt.Scale(domain=(0, 100)))
    )
    plot_2 = plot + plot.mark_line(color = 'black').encode(
        alt.Y('y_test')
    )
    
    try:
        plot_2.save(f'{out_file}/predict_vs_test.png')   #needs altair_saver package
    except:
        os.makedirs(os.path.dirname(f'{out_file}/predict_vs_test.png'))
        plot_2.to_csv(f'{out_file}/predict_vs_test.png', index = False)

    





if __name__ == "__main__":
  main(opt["--file_path"], opt["--out_file"])













