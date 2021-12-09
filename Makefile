# Makefile
# Group 27, 02-12-2021

# This driver script completes the data cleaning, 
# transformations, machine learning and report generation 
# for predicting the popularity of Spotify tracks. This script
# takes no arguments.

# example usage:
# make all

all : doc/spotify-track-predictor-report.md

# Download the data
data/raw/audio_audio_features.csv : 
	python src/download_data.py --url='https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-09-14/audio_features.csv' --out_file=data/raw/audio_audio_features.csv

# Data wrangling, cleaning, and splitting
data/processed/train_df.csv : data/raw/audio_audio_features.csv
	python src/clean_n_split.py --file_path=data/raw/audio_audio_features.csv --out_file=data/processed
data/processed/test_df.csv : data/raw/audio_audio_features.csv
	python src/clean_n_split.py --file_path=data/raw/audio_audio_features.csv --out_file=data/processed
	
# Generate Pandas_Profiling EDA report
eda/eda_report.html : data/processed/train_df.csv 
	python src/eda_profile.py data/processed/train_df.csv ./eda/eda_report.html

# Create the plots
results/paired_distribution_and_correlation.png : data/processed/train_df.csv
	Rscript src/eda_plots.r --train=data/processed/train_df.csv --out_dir=results
results/predict_vs_test.png : data/processed/train_df.csv
	Rscript src/eda_plots.r --train=data/processed/train_df.csv --out_dir=results


# Build machine learning models
results/best_hyperparameters.csv : data/processed/train_df.csv data/processed/test_df.csv
	python src/preprocess_n_model.py --file_path=data/processed --out_file=results
results/cv_df.csv : data/processed/train_df.csv data/processed/test_df.csv
	python src/preprocess_n_model.py --file_path=data/processed --out_file=results

	
# Write the report
doc/spotify-track-predictor-report.md : doc/spotify-track-predictor-report.Rmd results/paired_distribution_and_correlation.png results/predict_vs_test.png results/best_hyperparameters.csv results/cv_df.csv
	Rscript -e "rmarkdown::render('doc/spotify-track-predictor-report.Rmd')"
	
clean :
	rm -rf results/best_hyperparameters.csv results/cv_df.csv data/raw/audio_features.csv data/processed/train_df.csv data/processed/test_df.csv
	rm -rf results/paired_distribution_and_correlation.png results/predict_vs_test.png
	rm -rf doc/spotify-track-predictor-report.md
	
