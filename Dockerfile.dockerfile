# Docker file for the group project
# Group 27 Qingqing Song, Dec, 2021

# use jupyter/scipy-notebook as the base image
FROM jupyter/scipy-notebook

# install python packages
RUN conda install --quiet --yes \
    'docopt=3.2.*' \
    'numpy' \
    'os' \
    'sklearn' \
    'requests' \
    'pandas_profiling ' |

# install r and r-studio
RUN apt-get install r-base r-base-dev -y 

RUN apt-get install gdebi-core -y

# install R packages
RUN apt-get update -qq && install2.r --error \
    --deps TRUE \
    tidyverse \
    docopt \
    ggthemes \
    GGally \
    ggplot2 \
    kableExtra \
    caret \
