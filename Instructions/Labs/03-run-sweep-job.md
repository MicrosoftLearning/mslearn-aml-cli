---
lab:
    title: 'Lab: Perform hyperparameter tuning with the CLI (v2)'
    module: 'Module: Run jobs in Azure Machine Learning with CLI (v2)'
---

# Run a sweep job to tune hyperparameters

In this exercise, you will perform hyperparameter tuning when training a model with a Python script.The model training will be submitted with the CLI (v2). 

## Prerequisites

Before you continue, complete the [Create an Azure Machine Learning Workspace and assets with the CLI (v2)](Instructions/Labs/01-create-workspace.md) lab to set up your Azure Machine Learning environment.

You'll run all commands in this lab from the Azure Cloud Shell. If this is your first time using the cloud shell, complete the [Create an Azure Machine Learning Workspace and assets with the CLI (v2)](Instructions/Labs/01-create-workspace.md) lab to set up the cloud shell environment.

1. Open the Cloud Shell by navigating to [http://shell.azure.com](https://shell.azure.com/?azure-portal=true) and signing in with your Microsoft account.
1. The repo [https://github.com/MicrosoftLearning/mslearn-aml-cli](https://github.com/MicrosoftLearning/mslearn-aml-cli) should be cloned. You can explore the repo and its contents by using the `code .` command in the Cloud Shell.
1. To train multiple models in parallel, you'll use a compute cluster to train the models. To create a compute cluster, use the following command:
    ```azurecli
    az ml compute create --name "aml-cluster" --size STANDARD_DS11_V2 --max-instances 2 --type AmlCompute
    ```

> **Note:** Creating a compute cluster with two maximum instances means you can train two models in parallel. If you want to train more models in parallel, increase the number for --max-instances. You can also change this after the cluster is created.

## Run a sweep job

To train multiple models with varying hyperparameters, you can run the training script using a **sweep job**. Just like with a command job, the configuration of the sweep job can be described in a YAML file.

In this exercise, you'll train a Gradient Boosting Classifier model. Explore the training script **main.py** by navigating to **mslearn-aml-cli/Allfiles/Labs/03/src/main.py**. The dataset used is the registered dataset **diabetes-data**.

There are two hyperparameter values:
- Learning rate: [0.01, 0.1, 1.0]
- N estimators: [10, 100]

You'll use 

1. Run the following command in the Cloud Shell to open the files of the cloned repo:
    ```azurecli
    code .
    ```
1. Navigate to **mslearn-aml-cli/Allfiles/Labs/02/basic-job** and open **basic-job.yml** by selecting the file.
1. Change the **compute** value: replace <your-compute-instance-name> with the name of your compute instance.
1. Run the job by using the following command:
    ```azurecli
    az ml job create --file ./mslearn-aml-cli/Allfiles/Labs/02/basic-job/basic-job.yml --web
    ```
1. When using the `--web` parameter, the experiment run will automatically open in the Azure Machine Learning Studio. You can monitor the job there. Refresh the view if necessary. Once completed, you can explore the details of the job which are stored in the experiment run.