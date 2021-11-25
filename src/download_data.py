# author : Group 27 
# date : 2021-11-18

""""Downloads data csv data from a url and save it to a local filepath as csv format"

Usage: download_data.py --url=<url> --out_file=<out_file>

Options:
--url=<url>             URL from where to download the data (must be in standard csv format)
--out_file=<out_file>   Path (including filename) of where to locally write the file
"""

import pandas as pd
import os
from docopt import docopt

opt = docopt(__doc__)

def main(url, out_file):
  
  # test if the url exist
  try: 
    request = requests.get(url)
    request.status_code == 200
  except Exception as req:
    print("Website at the provided url does not exist.")
    print(req)
    
  # read in data
  data = pd.read_csv(url)
  
  # write the file
  try:
    data.to_csv(out_file, index = False)
  except:
     os.makedirs(os.path.dirname(out_file))
     data.to_csv(out_file, index = False)

if __name__ == "__main__":
  main(opt["--url"], opt["--out_file"])
