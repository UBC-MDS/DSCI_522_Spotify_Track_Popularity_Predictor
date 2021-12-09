# Docker file for the Spotify Track Popularity Predictor project     
# Group 27, Dec 7 2021

# use rocker/tidyverse as the base image
FROM rocker/tidyverse

RUN dpkg --add-architecture i386
RUN apt-get update

# install the R packages using install.packages
RUN Rscript -e "install.packages('kableExtra')"
RUN Rscript -e "install.packages('docopt')"
RUN Rscript -e "install.packages('ggthemes')"
RUN Rscript -e "install.packages('GGally')"
RUN Rscript -e "install.packages('knitr')"
RUN Rscript -e "install.packages('caret')"
RUN Rscript -e "install.packages('ggplot2')"
RUN apt-get install libxrender1:i386 libxtst6:i386 libxi6:i386 -y 


# install the anaconda distribution of python
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/conda update -n base -c defaults conda

# put anaconda python in path
ENV PATH="/opt/conda/bin:${PATH}"

# install python packages
RUN conda install -y -c anaconda \ 
    docopt \
    requests
    
RUN pip install \
    requests\
    altair_saver

# install python packages
RUN pip install \
    "altair-data-server==0.4.*" \
    "numpy==1.21.*" \
    "pandas" \
    "altair==4.1.*" \
    "scikit-learn==1.0.*" \
    "scipy==1.7.*" \
    "ipykernel==6.5.*" \
    "ipython>=7.15" \
    "pandas-profiling==1.4.*" 

RUN conda config --add channels conda-forge
RUN conda install -c conda-forge altair_saver

