# author: Group 27
# date: 2021-11-25

"Creates eda plots for the pre-processed training data from the spotify data (from https://github.com/rfordatascience/tidytuesday/blob/master/data/2021/2021-09-14/audio_features.csv).
Saves the plots as a png file.
Usage: src/eda_plots.r --train=<train> --out_dir=<out_dir>
  
Options:
--train=<train>     Path (including filename) to training data (which needs to be saved as a feather file)
--out_dir=<out_dir> Path to directory where the plots should be saved
" -> doc

library(tidyverse)
library(docopt)
library(ggthemes)
library(GGally)
theme_set(theme_minimal())

opt <- docopt(doc)

main <- function(train, out_dir) {
  
  # visualize predictor distributions by class
  numeric_cor <- read_csv(train) |> 
    select_if(is.numeric) |> 
    ggpairs(lower=list(continuous=wrap(ggally_smooth, size = 1, color = "dodgerblue", alpha = 0.5,
                                       gridLabelSize=20)))
  
  # save the plpt
  ggsave(paste0(out_dir, "/paired_distribution_and_correlation.png"), 
         numeric_cor,
         width = 25, 
         height = 25)
}

main(opt[["--train"]], opt[["--out_dir"]])