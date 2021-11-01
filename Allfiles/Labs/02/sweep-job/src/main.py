# Import libraries
import mlflow
import argparse
import glob

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

# define functions
def main(args):
    # enable auto logging
    mlflow.autolog()
    
    params = {
        "learning_rate": args.learning_rate,
        "n_estimators": args.n_estimators,
    }

    # read data
    data_path = args.diabetes_csv
    all_files = glob.glob(data_path + "/*.csv")
    df = pd.concat((pd.read_csv(f) for f in all_files), sort=False)
    
    # process data
    X_train, X_test, y_train, y_test = process_data(df)

    # train model
    model = train_model(params, X_train, X_test, y_train, y_test)
    
def process_data(df):
    # split dataframe into X and y
    X, y = df[['Pregnancies','PlasmaGlucose','DiastolicBloodPressure','TricepsThickness','SerumInsulin','BMI','DiabetesPedigree','Age']].values, df['Diabetic'].values

    # train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

    # return splits and encoder
    return X_train, X_test, y_train, y_test

def train_model(params, X_train, X_test, y_train, y_test):
    # train model
    model = GradientBoostingClassifier(**params)
    model = model.fit(X_train, y_train)

    # return model
    return model

def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--diabetes-csv", type=str)
    parser.add_argument("--learning-rate", dest='learning_rate', type=float, default=0.1)
    parser.add_argument("--n-estimators", dest='n_estimators', type=int, default=100)

    # parse args
    args = parser.parse_args()

    # return args
    return args

# run script
if __name__ == "__main__":
    # add space in logs
    print("\n\n")
    print("*" * 60)

    # parse args
    args = parse_args()

    # run main function
    main(args)

    # add space in logs
    print("*" * 60)
    print("\n\n")