# author: UBC MDS Block 3 Group 27
# date: 2021-11-18

"""This script output the EDA report of the data.
Usage: eda_profile.py <data> <output>

Options:
<data>            Takes any data, remember the path ;)
<output>          output data, should be *.html
""" 

import pandas as pd
from docopt import docopt
from pandas_profiling import ProfileReport
from sklearn.model_selection import train_test_split



opt = docopt(__doc__)

def main(data, output):
  df = pd.read_csv(data, encoding="utf-8")
  df_train, df_test = train_test_split(df, test_size=0.2, random_state=123)
  profile = ProfileReport(df_train, title="Pandas Profiling Report")  #, minimal=True)
  profile.to_file(output)
  

if __name__ == "__main__":
  main(opt["<data>"], opt["<output>"])
