---
lab:
    title: 'Lab: Deploy an MLflow model to a managed online endpoint'
    module: 'Module: Deploy an Azure Machine Learning model to a managed endpoint with CLI (v2)'
---

# Deploy a model to a managed online endpoint

In this exercise, you will deploy an MLflow model to a managed online endpoint.

## Prerequisites

Before you continue, complete the [Create an Azure Machine Learning Workspace and assets with the CLI (v2)](01-create-workspace.md) lab to set up your Azure Machine Learning environment.

## Deploy a model

A model has been trained to predict whether someone has diabetes. To consume the model, you want to deploy it to a managed online endpoint. The endpoint can be called from an application where a patient's information can be entered, after which the model can decide whether the patient is probable to have diabetes.

To deploy the model using the CLI (v2), you first create an endpoint.

1. Run the following command in the Cloud Shell to open the files of the cloned repo:

    ```azurecli
    code .
    ```

1. Navigate to **mslearn-aml-cli/Allfiles/Labs/04/mlflow-endpoint** and open **create-endpoint.yml** by selecting the file.
1. Explore the contents of the file. Note that your endpoint will use key-based authentication.
1. Use the following command to create the new endpoint.Before you run the command, replace `<endpoint_name>` with a name that is unique in the Azure region:

    ```azurecli
    az ml online-endpoint create --name <endpoint_name> -f ./mslearn-aml-cli/Allfiles/Labs/04/mlflow-endpoint/create-endpoint.yml
    ```

1. Next, you'll create the deployment. In the same folder **mslearn-aml-cli/Allfiles/Labs/04/mlflow-endpoint**, find and open the YAML configuration file **mlflow-deployment.yml** for the deployment.
1. The deployment configuration refers to the endpoint configuration. In addition, it specifies how the model should be registered, what kind of compute should be used for the inference configuration, and where it can find the model assets. The MLflow model assets are stored in the **model** folder.
1. To deploy the model, run the following command. Before you run the command, replace the `<endpoint_name>` with the name you previously created and create a new `<deployment_name>`:

    ```azurecli
    az ml online-deployment create --name <deployment_name> --endpoint <endpoint_name> -f ./mslearn-aml-cli/Allfiles/Labs/04/mlflow-endpoint/mlflow-deployment.yml --all-traffic
    ```

1. Deployment may take some time, and progress will be visible in the Azure Cloud Shell. You can also view the endpoint in the Azure Machine Learning Studio, in the **Endpoints** tab, under **Real-time endpoints**.

## Test the endpoint

Once deployment is completed, you can test and consume the endpoint. Let's try testing it with two data points.

1. In the **mslearn-aml-cli/Allfiles/Labs/04/mlflow-endpoint** folder, you can find the **sample-data.json** that contains two data points.
1. Run the following command to invoke the endpoint to predict for these two patients whether they have diabetes. Replace the `<endpoint_name>` with the name you previously created before you run the command:

    ```azurecli
    az ml online-endpoint invoke --name <endpoint_name> --request-file ./mslearn-aml-cli/Allfiles/Labs/04/mlflow-endpoint/sample-data.json
    ```

1. As a result, you will see either a 1 or a 0 for each data point. A 1 means the patient is likely to have diabetes, a 0 means the patient is likely not to have diabetes.
1. Feel free to play around with the sample data and run the command again to see different results!

## Clean up resources

When you're finished exploring Azure Machine Learning, delete your endpoint to avoid unnecessary charges in your Azure subscription.

You can delete an endpoint and all underlying deployments by using the following command. Rememeber to replace the `<endpoint_name>` with the name you previously created before you run the command:

```azurecli
az ml online-endpoint delete --name <endpoint_name> --yes --no-wait
```

To delete the Azure Machine Learning workspace, you can use the following command in the CLI:

```azurecli
az ml workspace delete
```
