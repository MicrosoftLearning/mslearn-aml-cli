---
lab:
    title: 'Lab: Run a basic Python training job'
    module: 'Module: Run jobs in Azure Machine Learning with CLI (v2)'
---

# Run a basic Python training job

In this exercise, you will train a model with a Python script. The model training will be submitted with the CLI (v2). First, you'll train a model based on a local CSV dataset. Next, you'll train a model using a dataset registered in the Azure Machine Learning workspace.

## Prerequisites

Before you continue, complete the [Create an Azure Machine Learning Workspace and assets with the CLI (v2)](01-create-workspace.md) lab to set up your cloud shell environment and your Azure Machine Learning environment.

1. Open the Cloud Shell by navigating to [http://shell.azure.com](https://shell.azure.com/?azure-portal=true) and signing in with your Microsoft account.
1. The repo [https://github.com/MicrosoftLearning/mslearn-aml-cli](https://github.com/MicrosoftLearning/mslearn-aml-cli) should be cloned. You can explore the repo and its contents by using the `code .` command in the Cloud Shell.
1. If your compute instance is stopped. Start the instance again by using the following command. Change `<your-compute-instance-name>` to your compute instance name before running the code:

    ```azurecli
    az ml compute start --name "<your-compute-instance-name>"
    ```

1. To confirm that the instance is now in a **Running** state, open another tab in your browser and navigate to the [Azure Machine Learning Studio](https://ml.azure.com). Open the **Compute** tab and select **Compute instances**.

## Train a model

To track a machine learning workflow, you can run the training script using a **job**. The configuration of the job can be described in a YAML file.

In this exercise, you'll train a Logistic Regression model. Explore the training script **main.py** by navigating to **mslearn-aml-cli/Allfiles/Labs/02/basic-job/src/main.py**. The dataset used is in the same folder and stored as **diabetes.csv**.

1. Run the following command in the Cloud Shell to open the files of the cloned repo:

    ```azurecli
    code .
    ```

1. Navigate to **mslearn-aml-cli/Allfiles/Labs/02/basic-job** and open **basic-job.yml** by selecting the file.
1. Change the **compute** value by replacing `<your-compute-instance-name> ` with the name of your compute instance.
1. Save the file by selecting the top right corner of the text editor and then selecting **Save**
1. Run the job by using the following command:

    ```azurecli
    az ml job create --file ./mslearn-aml-cli/Allfiles/Labs/02/basic-job/basic-job.yml
    ```

1. Return to your Azure Machine Learning Studio browser tab, go to the **Jobs** page and locate the **diabetes-example** experiment in the **All experiments** tab.
1. Open the run to monitor the job and refresh the view if necessary. Once completed, you can explore the details of the job which are stored in the experiment run.

## Train a model with dataset from datastore

In the [Create an Azure Machine Learning Workspace and assets with the CLI (v2)](Instructions/Labs/01-create-workspace.md) lab, you created a dataset named **diabetes-data**. To check that the dataset exists within your workspace, you can navigate to the Azure Machine Learning Studio and select the **Data** item from the left menu and then the **Data assets** tab.

Instead of storing a CSV file in the same folder as the training script, you can also train a model using a registered dataset as input.

1. Navigate to **mslearn-aml-cli/Allfiles/Labs/02/input-data-job** and open **data-job.yml** by selecting the file.
1. Change the **compute** value <your-compute-instance-name> with the name of your compute instance and save the file.

    > **Note** that the command now runs the **main.py** script with the parameter **--diabetes-csv**. The input of that parameter is defined in the **inputs.diabetes** value. It takes version 1 of the **diabetes-data** dataset from the Azure ML workspace.

1. Use the following command to run the job:

    ```azurecli
    az ml job create --file ./mslearn-aml-cli/Allfiles/Labs/02/input-data-job/data-job.yml
    ```

1. Go to the Azure Machine Learning Studio and locate the **diabetes-data-example** experiment. Open the run to monitor the job. Refresh the view if necessary. 
1. Once completed, you can explore the details of the job which are stored in the experiment run. Note that now, it lists the input dataset **diabetes-data**.

## Clean up resources

When you're finished exploring Azure Machine Learning, shut down the compute instance to avoid unnecessary charges in your Azure subscription.

You can stop a compute instance with the following command. Change `"testdev-vm"` to the name of your compute instance if necessary.

```azurecli
az ml compute stop --name "testdev-vm" --no-wait
```

> **Note:** Stopping your compute ensures your subscription won't be charged for compute resources. You will however be charged a small amount for data storage as long as the Azure Machine Learning workspace exists in your subscription. If you have finished exploring Azure Machine Learning, you can delete the Azure Machine Learning workspace and associated resources. However, if you plan to complete any other labs in this series, you will need to repeat the set-up to create the workspace and prepare the environment first.

To delete the Azure Machine Learning workspace, you can use the following command in the CLI:

```azurecli
az ml workspace delete
```
