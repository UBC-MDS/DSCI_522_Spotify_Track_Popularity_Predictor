# Song Popularity Predictor
Data analysis project for DSCI 522 (Data Science workflows); a course in the Master of Data Science program at the University of British Columbia.

Team Members:
* Victor Francis
* Reza Mirzazadeh
* Qingqing Song
* Jessie Wong

## Project Description
This project will use the audio_features dataset, which contains information from spotify tracks, such as performer, genre, duration, loudness, etc. The data is from tidytuesday and was obtained [here](https://github.com/rfordatascience/tidytuesday/blob/master/data/2021/2021-09-14/readme.md).
The research question that we aim to answer through this project is to predict the popularity of a song, given various features such as genre, duration, energy, tempo and acousticness. 

Exploratory data analysis (EDA)

Each row of the data set represents a song with its features and its popularity. we are intrested in predicting songs popularity given song features. Data wrangling was necessary to keep the infomrative and relavant columns to our target.

Prior to analysis, we performed EDA on the features to assess the correlation betweeen features themselves and each feature with the popularity of songs. As a result, we dropped missing values and features that do not contribute to the predictve quality of the ridge model such as spotify_track_preview_url, song_id and time_signature, and we focused on columns such as energy, danceability, speechiness, and loudness.  

Some exploratory data questions we will answer are what pairs of features have strong correlations, and which columns contain the largest number of missing values. One exploratory data analysis figure that we will create is a correlation plot or heatmap to show which pairs of features are correlated. The exploratory data analysis can be found  [here](https://github.com/jessie14/DSCI_522_Spotify_Track_Popularity_Predictor/tree/main/eda).

Finally, after completing all necessary analysis to answer our research question, we will share the results as a table and as multiple plots, showing the predicted distribution of song popularity for each feature.

The steps we run our analysis will follow the flowchart below.
![](images/Makefile.png)


# Report
The final report can be found [here](https://github.com/UBC-MDS/DSCI_522_Spotify_Track_Popularity_Predictor/blob/main/doc/spotify-track-predictor-report.md)

# Usage
There are two suggested ways to run this analysis:

#### 1. Using Docker  
To replicate the analysis, install Docker. 
Then clone this GitHub repository and run the following command at the command line/terminal from the root directory of this project:
```
docker run --rm -v /$(pwd):/home/spotify qq1207/spotify_track_popularity_predictor make -C /../home/spotify all
```

To reset the repo to a clean state, with no intermediate or results files, run the following command at the command line/terminal from the root directory of this project:
```
docker run --rm -v /$(pwd):/home/spotify qq1207/spotify_track_popularity_predictor make -C /../home/spotify clean
```

#### 2. Without using Docker  
To replicate the analysis, clone this GitHub repository, install the dependencies listed below, and run the following command at the command line/terminal from the root directory of this project:

```
make all
```

To reset the repo to a clean state, with no intermediate or results files, run the following command at the command line/terminal from the root directory of this project:

```
make clean
```

# Dependencies
* Python 3.9.7 and Python packages:
    * docopt=0.6.2
    * pandas=1.3.4
    * numpy=1.21.4
    * sklearn=1.0.1
    * altair=4.1.0

* R version 4.1.1 and R packages:
    * knitr=1.3
    * tidyverse=1.3.1
    * dplyr=1.0.7
    

# References

de Jonge, Edwin. 2018. Docopt: Command-Line Interface Specification Language. https://CRAN.R-project.org/package=docopt.

Jed Wing, Max Kuhn. Contributions from, Steve Weston, Andre Williams, Chris Keefer, Allan Engelhardt, Tony Cooper, Zachary Mayer, et al. 2019. Caret: Classification and Regression Training. https://CRAN.R-project.org/package=caret.

Keleshev, Vladimir. 2014. Docopt: Command-Line Interface Description Language. https://github.com/docopt/docopt.

R Core Team. 2019. R: A Language and Environment for Statistical Computing. Vienna, Austria: R Foundation for Statistical Computing. https://www.R-project.org/.

Van Rossum, Guido, and Fred L. Drake. 2009. Python 3 Reference Manual. Scotts Valley, CA: CreateSpace.

Wickham, Hadley. 2017. Tidyverse: Easily Install and Load the ’Tidyverse’. https://CRAN.R-project.org/package=tidyverse.
