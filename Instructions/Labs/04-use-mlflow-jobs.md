---
lab:
    title: 'Lab: Track Azure ML jobs with MLflow'
    module: 'Module: Use MLflow with Azure ML jobs submitted with CLI (v2)'
---

# Track Azure ML jobs with MLflow

In this exercise, you will train a model with a Python script. The Python script uses **MLflow** to track parameters, metrics, and artifacts.

## Prerequisites

Before you continue, complete the [Create an Azure Machine Learning Workspace and assets with the CLI (v2)](01-create-workspace.md) lab to set up your Azure Machine Learning environment.

You'll run all commands in this lab from the Azure Cloud Shell. If this is your first time using the cloud shell, complete the [Create an Azure Machine Learning Workspace and assets with the CLI (v2)](Instructions/Labs/01-create-workspace.md) lab to set up the cloud shell environment.

1. Open the Cloud Shell by navigating to [http://shell.azure.com](https://shell.azure.com/?azure-portal=true) and signing in with your Microsoft account.
1. The repo [https://github.com/MicrosoftLearning/mslearn-aml-cli](https://github.com/MicrosoftLearning/mslearn-aml-cli) should be cloned. You can explore the repo and its contents by using the `code .` command in the Cloud Shell.
1. If your compute instance is stopped. Start the instance again by using the following command. Change `<your-compute-instance-name>` to your compute instance name before running the code:

    ```azurecli
    az ml compute start --name "<your-compute-instance-name>"
    ```

1. To confirm that the instance is now in a **Running** state, open another tab in your browser and navigate to the [Azure Machine Learning Studio](https://ml.azure.com). Open the **Compute** tab and select **Compute instances**.

## Track a model

You'll train a Logistic Regression model to classify whether someone has diabetes. You can track things like input parameter such as the value of the regularization rate used to train the model. As a result, you want to know the accuracy of the model and store a confusion matrix to explain the accuracy.

To track the input and output of a model, we can:

- Enable autologging using `mlflow.autolog()`
- Use logging functions to track custom metrics using `mlflow.log_*`

Note that to do either, we have to include the `mlflow` and `azureml-mlflow` packages in the environment used during training. The registered environment **basic-env-scikit** includes these two packages.

### Enable autologging

You'll submit a job from the Azure Cloud Shell with the CLI (v2), using a Python script.

1. Run the following command in the Cloud Shell to open the files of the cloned repo:

    ```azurecli
    code .
    ```

1. Navigate to **mslearn-aml-cli/Allfiles/Labs/03/mlflow-job** and open **mlflow-job.yml** by selecting the file.
1. Change the **compute** value by replacing `<your-compute-instance-name>` with the name of your compute instance.
1. Save the file by selecting the top right corner of the text editor and then selecting **Save**.
1. Note that you'll run the **mlflow-autolog.py** script that is located in the **src** folder. Navigate to that folder and open the file to explore it. Find the `mlflow.autolog()` method.
1. Run the job by using the following command:

    ```azurecli
    az ml job create --file ./mslearn-aml-cli/Allfiles/Labs/03/mlflow-job/mlflow-job.yml
    ```

1. Switch to your Azure Machine Learning Studio browser tab. Go to the **Jobs** page, in the **All experiments** tab and select the **diabetes-mlflow-example** experiment.
1. Monitor the job and refresh the view if necessary. Once completed, you can explore the details of the job which are stored in the experiment run.

### Use logging functions to track custom metrics

Instead of using the autologging feature of Mlflow, you can also create and track your own parameters, metrics, and artifacts. For this, we'll use another training script.

1. Navigate to **mslearn-aml-cli/Allfiles/Labs/03/mlflow-job** and open **mlflow-job.yml** by selecting the file.
1. Now, you want to run the **custom-mlflow.py** script that is located in the **src** folder. In the **mlflow-job.yml** file, remove the **mlflow-autolog.py** file, and replace with **custom-mlflow.py**. Don't forget to save the YAML file!
1. To explore the training script, navigate to the **src** folder and open the file to explore it. Find the `mlflow.log_param()`, `mlflow.metric()`, and `mlflow.artifact()` methods.
1. Run the job by using the following command:

    ```azurecli
    az ml job create --file ./mslearn-aml-cli/Allfiles/Labs/03/mlflow-job/mlflow-job.yml
    ```

1. Go to the Azure Machine Learning Studio and again, locate the **diabetes-mlflow-example** experiment. Open the newest run to monitor the job. Once completed, you'll find the regularization rate in the **Overview** tab under **Parameters**. The accuracy score is listed under **Metrics** and the confusion matrix can be found under **Images**.

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
