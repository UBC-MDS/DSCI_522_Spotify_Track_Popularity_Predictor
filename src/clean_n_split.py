# author : Group 27 
# date : 2021-11-25

""""Cleans data csv data from a data file audio_features.csv and save it to a local filepath as csv format"

Usage: clean_n_split.py --file_path=<file_path> --out_train_df=<out_file> --out_test_df=<out_file>

Options:
--file_path=<file_path>   Path to data file for which to perform preprocessing on
--out_train_df=<out_file>     Path (including filename) of where to locally write the train data
--out_test_df=<out_file>     Path (including filename) of where to locally write the test data
"""

import pandas as pd
import os
from docopt import docopt
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split

opt = docopt(__doc__)

def main(file_path, out_train_df, out_test_df ):
    data= pd.read_csv(file_path)

    data = data.drop(columns = ["spotify_track_preview_url"]) #drop the URL columns as it has so many NA and does not have useful information
    data = data.dropna()                                      #drop the NA rows
    data['spotify_genre'] = data['spotify_genre'].str[1:-1].str.replace("'","") # convert the spotify_genre to string 
    

    train_df, test_df = train_test_split(data, test_size=0.2, random_state=123)


    try:
        train_df.to_csv(out_train_df, index = False)
    except:
        os.makedirs(os.path.dirname(out_train_df))
        data.to_csv(out_train_df, index = False)
    
    try:
        test_df.to_csv(out_test_df, index = False)
    except:
        os.makedirs(os.path.dirname(out_test_df))
        test_df.to_csv(out_test_df, index = False)

if __name__ == "__main__":
    main(opt["--file_path"], opt["--out_train_df"], opt["--out_test_df"])