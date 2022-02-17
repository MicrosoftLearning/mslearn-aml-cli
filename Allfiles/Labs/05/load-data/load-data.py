# import libraries
import argparse
import os
import glob
from pathlib import Path
import pandas as pd
import mlflow

# get parameters
parser = argparse.ArgumentParser()
parser.add_argument("--input_data", type=str, help='Path to input dataset')
parser.add_argument('--raw_data', type=str, help='Path of raw data')
args = parser.parse_args()

# load the data (passed as an input dataset)
print("Loading Data...")

# read data
data_path = os.listdir(args.input_data)
print(data_path)
all_files = glob.glob(data_path + "/*.csv")
df = pd.concat((pd.read_csv(f) for f in all_files), sort=False)

# log raw row count
row_count_raw = (len(df))
mlflow.log_metric('raw_rows', row_count_raw)

# get summary statistics
stats = df.describe()
stats.to_csv('raw_data_statistics.csv')
mlflow.log_artifact('raw_data_statistics.csv')

# set the prepped data as output
output_df = df.to_csv((Path(args.raw_data) / "raw_data.csv"))