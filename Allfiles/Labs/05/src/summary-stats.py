# import libraries
import argparse
import glob
from pathlib import Path
import pandas as pd
import mlflow

# get parameters
parser = argparse.ArgumentParser()
parser.add_argument("--input_data", type=str, help='Path to input data')
args = parser.parse_args()

# read data
data_path = args.input_data
all_files = glob.glob(data_path + "/*.csv")
df = pd.concat((pd.read_csv(f) for f in all_files), sort=False)
    
# log row count
row_count = (len(df))
mlflow.log_metric('row count', row_count)

# get summary statistics
stats = df.describe()
stats.to_csv('summary_statistics.csv')
mlflow.log_artifact('summary_statistics.csv')
