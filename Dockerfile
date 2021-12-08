# Docker file for the group project  
# Group 27 Qingqing Song, Dec, 2021

# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# install R packages
RUN apt-get update -qq && apt-get -y --no-install-recommends install \
  && install2.r --error \
    --deps TRUE \
    docopt \
    GGally \
    ggplot2 \
    ggridges \
    ggthemes \
    caret 

# install the kableExtra package using install.packages 
RUN Rscript -e "install.packages('kableExtra')"

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

# Install Python 3 packages
RUN pip install \
    "jupyter-book==0.12.*" \
    "altair-data-server==0.4.*" \
    "numpy==1.21.*" \
    "pandas" \
    "docopt==0.6.*" \
    "altair==4.1.*" \
    "scikit-learn==1.0.*" \
    "scipy==1.7.*" \
    "requests==2.24.*" \
    "ipykernel==6.5.*" \
    "ipython>=7.15" \
    "pandas-profiling==1.4.*" \

RUN conda install -c conda-forge altair_saver

