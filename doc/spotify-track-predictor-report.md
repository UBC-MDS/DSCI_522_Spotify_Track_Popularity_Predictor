Predicting Spotify track popularity based on certain audio features
================
#### Group 27 members</br>
* Victor Francis 
* Reza Mirzazadeh 
* Qingqing Song 
* Jessie Wong

2021/11/25 (updated: 2021-12-11)


-   [Summary](#summary)
-   [Introduction](#introduction)
-   [Methods](#methods)
    -   [Data](#data)
    -   [Analysis](#analysis)
-   [Results & Discussion](#results--discussion)
-   [References](#references)




# Summary

We use Ridge algorithm here to build a regression model to predict the
popularity of spotify tracks based on features like danceability,
loudness, tempo etc. The popularity score ranges from 0 to 100. A
popularity score of 0 means the the song has minute popularity and a
popularity score of 100 means the song is extremely popular.

# Introduction

Some songs sit atop popularity charts like the Billboard charts while
certain other songs comfortably sit at the bottom of the charts. Some
songs don’t even chart at all. This pose an interesting question to us
on what exactly makes a song popular and we ask if we can be able to
predict how popular a song will get. based on certain features. Some
songs are unexceptionally popular while some other songs are not as
popular. This is an attempt to answer this interesting question. We
attempt here to make a prediction on the popularity of a song based on
certain features.

According to this
[report](https://www.musicbusinessworldwide.com/over-60000-tracks-are-now-uploaded-to-spotify-daily-thats-nearly-one-per-second/ "www.musicbusinessworldwide.com"),
approximately 137 million new songs are released every year, and only
about 14 records have sold 15 million physical copies or more in global
history. Therefore, it is important to determine what exactly determines
a track popularity and specifically make predictions on how popular a
song will get based on based on features like danceability, loudness,
tempo etc.

# Methods

## Data

The dataset used in this project was sourced from Tidy Tuesday’s github
repo
[here](https://github.com/rfordatascience/tidytuesday/blob/master/data/2021/2021-09-14/readme.md),
and particularly
[here](https://query.data.world/s/gvgzoh3hhfj4lg4rbv3x4ah6rm6ta4). The
data, however, originally comes from
[Data.World](https://data.world/kcmillersean/billboard-hot-100-1958-2017#),
[Billboard.com](http://billboard.com/) and Spotify. Each row from the
dataset represents a song’s features and a target column specifying the
song’s popularity on a scale of 0 (least popularity) to 100 (most
popularity).

## Analysis

Ridge model was built to answer our research question (to predict
spotify tracks popularity). This is a regression solution and
predictions range from 0 (least popularity) to 100 (most popularity).
All features in the original dataset were used to fit the model with the
exceptions of ‘song_id,’ ‘spotify_track_id,’ ‘spotify_track_album’
features. A 10-fold cross-validation was used for hyperparameter
optimization. The code used to perform this analysis can be found
[here](https://github.com/UBC-MDS/DSCI_522_Spotify_Track_Popularity_Predictor/blob/main/src/preprocess_n_model.py).

# Results & Discussion

It is usually very important to look at how the features are co-related
and to see what their pairwise distributions look like. Here, the blue
plots (and a fitting line) represents the paired distributions of the
features, and the other boxes are the paired correlations of the
features. As can be seen, the correlations are fair and not
unreasonable, hence the features can be used together for building the
Ridge model that seeks to answer the predictive question.

<img src="../results/paired_distribution_and_correlation.png" title="Figure 1. Pairwise distributions and correlations of all features" alt="Figure 1. Pairwise distributions and correlations of all features" width="100%" />

We adopted a simple linear regression model - Ridge algorithm. Our
choice of Ridge stems from the fact it it is regularized and take care
of the multi-collinearity problem. A 10-fold cross validation was
carried out and the train and validation *R*<sup>2</sup> scores reported
in the table below from cross-validation

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>
Table 1. Train and validation scores from cross-validation
</caption>
<thead>
<tr>
<th style="text-align:right;">
fit_time
</th>
<th style="text-align:right;">
score_time
</th>
<th style="text-align:right;">
test_score
</th>
<th style="text-align:right;">
train_score
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:right;">
0.6432571
</td>
<td style="text-align:right;">
0.0582726
</td>
<td style="text-align:right;">
0.4782156
</td>
<td style="text-align:right;">
0.7925252
</td>
</tr>
<tr>
<td style="text-align:right;">
0.6447966
</td>
<td style="text-align:right;">
0.0585334
</td>
<td style="text-align:right;">
0.4740333
</td>
<td style="text-align:right;">
0.7918603
</td>
</tr>
<tr>
<td style="text-align:right;">
0.6070879
</td>
<td style="text-align:right;">
0.0596128
</td>
<td style="text-align:right;">
0.5033566
</td>
<td style="text-align:right;">
0.7890991
</td>
</tr>
<tr>
<td style="text-align:right;">
0.6175146
</td>
<td style="text-align:right;">
0.0581553
</td>
<td style="text-align:right;">
0.4766368
</td>
<td style="text-align:right;">
0.7928274
</td>
</tr>
<tr>
<td style="text-align:right;">
0.6207914
</td>
<td style="text-align:right;">
0.0589225
</td>
<td style="text-align:right;">
0.4459885
</td>
<td style="text-align:right;">
0.7938532
</td>
</tr>
<tr>
<td style="text-align:right;">
0.6111379
</td>
<td style="text-align:right;">
0.0589015
</td>
<td style="text-align:right;">
0.4791355
</td>
<td style="text-align:right;">
0.7909243
</td>
</tr>
<tr>
<td style="text-align:right;">
0.6139162
</td>
<td style="text-align:right;">
0.0656796
</td>
<td style="text-align:right;">
0.4707675
</td>
<td style="text-align:right;">
0.7920449
</td>
</tr>
<tr>
<td style="text-align:right;">
0.6158381
</td>
<td style="text-align:right;">
0.0594504
</td>
<td style="text-align:right;">
0.4846590
</td>
<td style="text-align:right;">
0.7931858
</td>
</tr>
<tr>
<td style="text-align:right;">
0.6065817
</td>
<td style="text-align:right;">
0.0584295
</td>
<td style="text-align:right;">
0.4647415
</td>
<td style="text-align:right;">
0.7921520
</td>
</tr>
<tr>
<td style="text-align:right;">
0.6169782
</td>
<td style="text-align:right;">
0.0587053
</td>
<td style="text-align:right;">
0.5039069
</td>
<td style="text-align:right;">
0.7905965
</td>
</tr>
</tbody>
</table>

The following table shows the results of RandomizedSearchCV for
determining the best hyperparameters for the Ridge model.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>
Table 2. Best hyperparameters from RandomizedSearchCV
</caption>
<thead>
<tr>
<th style="text-align:right;">
mean_test_score
</th>
<th style="text-align:right;">
param_ridge\_\_alpha
</th>
<th style="text-align:right;">
param_columntransformer\_\_countvectorizer-1\_\_max_features
</th>
<th style="text-align:left;">
param_columntransformer\_\_countvectorizer-1\_\_binary
</th>
<th style="text-align:right;">
param_columntransformer\_\_countvectorizer-2\_\_max_features
</th>
<th style="text-align:left;">
param_columntransformer\_\_countvectorizer-2\_\_binary
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:right;">
0.4971355
</td>
<td style="text-align:right;">
1e+00
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
TRUE
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
</tr>
<tr>
<td style="text-align:right;">
0.4943319
</td>
<td style="text-align:right;">
1e+00
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
</tr>
<tr>
<td style="text-align:right;">
0.4933197
</td>
<td style="text-align:right;">
1e+01
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
TRUE
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
</tr>
<tr>
<td style="text-align:right;">
0.4552179
</td>
<td style="text-align:right;">
1e-01
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
TRUE
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
</tr>
<tr>
<td style="text-align:right;">
0.4523615
</td>
<td style="text-align:right;">
1e-01
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
</tr>
<tr>
<td style="text-align:right;">
0.4517998
</td>
<td style="text-align:right;">
1e-01
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
TRUE
</td>
</tr>
<tr>
<td style="text-align:right;">
0.4408479
</td>
<td style="text-align:right;">
1e+02
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
TRUE
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
</tr>
<tr>
<td style="text-align:right;">
0.4402483
</td>
<td style="text-align:right;">
1e+02
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
</tr>
<tr>
<td style="text-align:right;">
0.4384227
</td>
<td style="text-align:right;">
1e-03
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
TRUE
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
TRUE
</td>
</tr>
<tr>
<td style="text-align:right;">
0.4363332
</td>
<td style="text-align:right;">
1e-03
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
<td style="text-align:right;">
1000
</td>
<td style="text-align:left;">
FALSE
</td>
</tr>
</tbody>
</table>

In order to evaluate the performance of our model, we made some
predictions and compared the predicted values with the actual values. We
have plotted this below. The Goodness of Fit below is not unreasonable
and shows the viability of the ridge model.

<img src="../results/predict_vs_test.png" title="Figure 2. Comparison of actual vs. predicted values" alt="Figure 2. Comparison of actual vs. predicted values" width="100%" />

In order to improve this model in the future where we can have excellent
reliability on the model predictions, we will need the right combination
of data. The data used here are mostly Spotify and Billboard-based. In
the future, we’ll look at aggregating data from other sources as well.
Also, the ridge model deployed did not perform greatly, we’ll look into
more sophisticated feature engineering and model training in the future.

# References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-ccsac" class="csl-entry">

Canadian Cancer Statistics Advisory Committee. 2019. “Canadian Cancer
Statistics.” *Canadian Cancer Society*.
<http://cancer.ca/Canadian-Cancer-Statistics-2019-EN>.

</div>

<div id="ref-docopt" class="csl-entry">

de Jonge, Edwin. 2018. *Docopt: Command-Line Interface Specification
Language*. <https://CRAN.R-project.org/package=docopt>.

</div>

<div id="ref-caret" class="csl-entry">

Jed Wing, Max Kuhn. Contributions from, Steve Weston, Andre Williams,
Chris Keefer, Allan Engelhardt, Tony Cooper, Zachary Mayer, et al. 2019.
*Caret: Classification and Regression Training*.
<https://CRAN.R-project.org/package=caret>.

</div>

<div id="ref-docoptpython" class="csl-entry">

Keleshev, Vladimir. 2014. *Docopt: Command-Line Interface Description
Language*. <https://github.com/docopt/docopt>.

</div>

<div id="ref-R" class="csl-entry">

R Core Team. 2019. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

</div>

<div id="ref-Python" class="csl-entry">

Van Rossum, Guido, and Fred L. Drake. 2009. *Python 3 Reference Manual*.
Scotts Valley, CA: CreateSpace.

</div>

<div id="ref-tidyverse" class="csl-entry">

Wickham, Hadley. 2017. *Tidyverse: Easily Install and Load the
’Tidyverse’*. <https://CRAN.R-project.org/package=tidyverse>.

</div>

</div>
