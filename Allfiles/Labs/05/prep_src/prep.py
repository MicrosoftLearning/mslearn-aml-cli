# import libraries

import argparse
import glob
from pathlib import Path
import pandas as pd
import mlflow
from sklearn.preprocessing import MinMaxScaler

# get parameters
parser = argparse.ArgumentParser()
parser.add_argument("--raw_data", type=str, help='Path to raw dataset')
parser.add_argument('--prep_data', type=str, help='Path of prepped data')
args = parser.parse_args()

# load the data (passed as an input dataset)
print("Loading Data...")
# read data
data_path = args.raw_data
all_files = glob.glob(data_path + "/*.csv")
df = pd.concat((pd.read_csv(f) for f in all_files), sort=False)
    
# log raw row count
row_count_raw = (len(df))
mlflow.log_metric('raw_rows', row_count_raw)

# get summary statistics
stats = df.describe()
stats.to_csv('raw_data_statistics.csv')
mlflow.log_artifact('raw_data_statistics.csv')

# remove nulls
df = df.dropna()

# normalize the numeric columns
scaler = MinMaxScaler()
num_cols = ['Pregnancies','PlasmaGlucose','DiastolicBloodPressure','TricepsThickness','SerumInsulin','BMI','DiabetesPedigree']
df[num_cols] = scaler.fit_transform(df[num_cols])

# log processed rows
row_count_processed = (len(df))
mlflow.log_metric('processed_rows', row_count_processed)

# get summary statistics
stats_processed = df.describe()
stats_processed.to_csv('prep_data_statistics.csv')
mlflow.log_artifact('prep_data_statistics.csv')

# set the prepped data as output
output_df = df.to_csv((Path(args.prep_data) / "prep_data.csv"))