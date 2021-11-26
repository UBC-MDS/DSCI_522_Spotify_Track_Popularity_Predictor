# Group 27
# 2021/11/26
#
# Driver script/pipeline for Spotify Track Prediction project
#
# usage: bash doc/runall.sh

# Download dataset
python src/download_data.py --url='https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-09-14/audio_features.csv' --out_file=data/raw/audio_audio_features.csv

# Data wrangling, cleaning, and splitting
python src/clean_n_split.py --file_path=data/raw/audio_audio_features.csv --out_file=data/processed

# Generate Pandas_Profiling EDA report
python src/eda_profile.py data/processed/train_df.csv ./eda/eda_report.html

# Generate EDA plots in R
Rscript src/eda_plots.r --train=data/processed/train_df.csv --out_dir=results

# Build Machine Learning model
python src/preprocess_n_model.py --file_path=data/processed --out_file=results