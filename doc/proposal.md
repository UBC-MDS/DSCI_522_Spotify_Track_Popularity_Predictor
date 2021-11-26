# Song Popularity Predictor
Data analysis project for DSCI 522 (Data Science workflows); a course in the Master of Data Science program at the University of British Columbia.

Team Members:
* Victor Francis
* Reza Mirzazadeh
* Qingqing Song
* Jessie Wong

# Project Description
This project will use the audio_features dataset, which contains information from spotify tracks, such as performer, genre, duration, loudness, etc. The data is from tidytuesday and was obtained [here](https://github.com/rfordatascience/tidytuesday/blob/master/data/2021/2021-09-14/readme.md).
The research question that we aim to answer through this project is to predict the popularity of a song, given various features such as genre, duration, energy, tempo and acousticness. 

The first step is that we need to wrangle the raw data to only include the informative and relevant columns, and to tidy the data in a way that makes analysis possible. Some exploratory data questions we will answer are what pairs of features have strong correlations, and which columns contain the largest number of missing values. One exploratory data analysis figure that we will create is a correlation plot or heatmap to show which pairs of features are correlated. The exploratory data analysis can be found  [here](https://github.com/jessie14/DSCI_522_Spotify_Track_Popularity_Predictor/tree/main/eda).

Finally, after completing all necessary analysis to answer our research question, we will share the results as a table and as multiple plots, showing the predicted distribution of song popularity for each feature.

