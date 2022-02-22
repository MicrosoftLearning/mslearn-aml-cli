# Import libraries
import mlflow
import argparse
import glob
import joblib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# define functions
def main(args):
    # read data
    data_path = args.diabetes_csv
    all_files = glob.glob(data_path + "/*.csv")
    df = pd.concat((pd.read_csv(f) for f in all_files), sort=False)

    # process data
    X_train, X_test, y_train, y_test = process_data(df)

    # train model
    reg_rate = args.reg_rate
    mlflow.log_param("Regularization rate", reg_rate)
    model = train_model(reg_rate, X_train, X_test, y_train, y_test)
  
def process_data(df):
    # split dataframe into X and y
    X, y = df[['Pregnancies','PlasmaGlucose','DiastolicBloodPressure','TricepsThickness','SerumInsulin','BMI','DiabetesPedigree','Age']].values, df['Diabetic'].values

    # train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

    # return splits and encoder
    return X_train, X_test, y_train, y_test

def train_model(reg_rate, X_train, X_test, y_train, y_test):
    # train model
    model = LogisticRegression(C=1/reg_rate, solver="liblinear").fit(X_train, y_train)

    # calculate accuracy
    y_pred = model.predict(X_test)
    acc = np.average(y_pred == y_test)
    mlflow.log_metric("Accuracy", np.float(acc))

    # create confusion matrix
    conf_matrix = confusion_matrix(y_true=y_test, y_pred=y_pred)
    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    ax.matshow(conf_matrix, cmap=plt.cm.Blues, alpha=0.3)
    for i in range(conf_matrix.shape[0]):
        for j in range(conf_matrix.shape[1]):
            ax.text(x=j, y=i,s=conf_matrix[i, j], va='center', ha='center', size='xx-large')
    
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.savefig("ConfusionMatrix.png")
    mlflow.log_artifact("ConfusionMatrix.png")

    # return model
    return model

def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--diabetes-csv", dest='diabetes_csv', type=str)
    parser.add_argument("--reg-rate", dest='reg_rate', type=float, default=0.01)

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