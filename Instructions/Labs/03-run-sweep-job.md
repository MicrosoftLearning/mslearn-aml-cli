---
lab:
    title: 'Lab: Perform hyperparameter tuning with a sweep job'
    module: 'Module: Run jobs in Azure Machine Learning with CLI (v2)'
---

# Run a sweep job to tune hyperparameters

In this exercise, you will perform hyperparameter tuning when training a model with a Python script.The model training will be submitted with the CLI (v2).

## Prerequisites

Before you continue, complete the [Create an Azure Machine Learning Workspace and assets with the CLI (v2)](01-create-workspace.md) lab to set up your Azure Machine Learning environment.

You'll run all commands in this lab from the Azure Cloud Shell. If this is your first time using the cloud shell, complete the [Create an Azure Machine Learning Workspace and assets with the CLI (v2)](Instructions/Labs/01-create-workspace.md) lab to set up the cloud shell environment.

1. Open the Cloud Shell by navigating to [http://shell.azure.com](https://shell.azure.com/?azure-portal=true) and signing in with your Microsoft account.
1. The repo [https://github.com/MicrosoftLearning/mslearn-aml-cli](https://github.com/MicrosoftLearning/mslearn-aml-cli) should be cloned. You can explore the repo and its contents by using the `code .` command in the Cloud Shell.
1. To train multiple models in parallel, you'll use a compute cluster to train the models. To create a compute cluster, use the following command:

    ```azurecli
    az ml compute create --name "aml-cluster" --size STANDARD_DS11_V2 --max-instances 2 --type AmlCompute
    ```

1. To confirm that the cluster has been created, open another tab in your browser and navigate to the [Azure Machine Learning Studio](https://ml.azure.com). Open the **Compute** tab and select **Compute clusters**, you should see there a cluster named **aml-cluster**.
    > **Note:** Creating a compute cluster with two maximum instances means you can train two models in parallel. If you want to train more models in parallel, increase the number for --max-instances. You can also change this after the cluster is created.

## Run a sweep job

To train multiple models with varying hyperparameters, you can run the training script using a **sweep job**. Just like with a command job, the configuration of the sweep job can be described in a YAML file.

In this exercise, you'll train a Gradient Boosting Classifier model. Explore the training script **main.py** by navigating to **mslearn-aml-cli/Allfiles/Labs/02/sweep-job/src/main.py**. The dataset used is the registered dataset **diabetes-data**.

There are two hyperparameter values:

- Learning rate: with search space [0.01, 0.1, 1.0]
- N estimators: with search space [10, 100]

You'll use the grid sampling method on these hyperparameters, which means you'll try out all possible combinations of values. As a result, you'll train six models as part of the sweep job. Recall that each individual model will be listed as a child run, and the details of the overview of the sweep job will be stored with the main experiment run.

To run the sweep job:

1. Run the following command in the Cloud Shell to open the files of the cloned repo, if they are not opened yet:

    ```azurecli
    code .
    ```

1. Navigate to **mslearn-aml-cli/Allfiles/Labs/02/sweep-job** and open **sweep-job.yml** by selecting the file.

1. Run the job by using the following command:

    ```azurecli
    az ml job create --file ./mslearn-aml-cli/Allfiles/Labs/02/sweep-job/sweep-job.yml
    ```

1. Switch to the browser tab with Azure Machine Learning Studio. Go to the **Jobs** page and select the **diabetes-sweep-example** experiment.
1. Monitor the job and refresh the view if necessary. Once completed, you can explore the details of the job which are stored in the experiment run.

## Clean up resources

The compute cluster will automatically scale down to 0 nodes, so there is no need to stop the cluster.

> **Note:** Stopping your compute ensures your subscription won't be charged for compute resources. You will however be charged a small amount for data storage as long as the Azure Machine Learning workspace exists in your subscription. If you have finished exploring Azure Machine Learning, you can delete the Azure Machine Learning workspace and associated resources. However, if you plan to complete any other labs in this series, you will need to repeat the set-up to create the workspace and prepare the environment first.

To delete the Azure Machine Learning workspace, you can use the following command in the CLI:

```azurecli
az ml workspace delete
```
