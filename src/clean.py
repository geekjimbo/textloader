# load data sets
import pandas as pd
import yaml

_config = yaml.load( open('./config/config.yml')) 

df1 = pd.read_fwf(_config['file_path_1'])
df2 = pd.read_fwf(_config['file_path_2'])

frames = [df1, df2]

df = pd.concat( frames )


# integrate data sets 
# clean data set
