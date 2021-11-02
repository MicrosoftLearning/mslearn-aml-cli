---
lab:
    title: 'Lab: Create an Azure Machine Learning Workspace and assets with the CLI (v2)'
    module: 'Module 1: Create Azure Machine Learning resources with the CLI (v2)'
---

# Create an Azure Machine Learning Workspace and assets with the CLI (v2)

In this exercise, you will create and explore an Azure Machine Learning workspace.

## Install the Azure CLI and Azure Machine Learning extension

Before you continue, make sure you have the Azure CLI and the Azure Machine Learning extension installed on your computer.

1. Use the instructions to [install the Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli) based on the platform you choose.
2. Open a shell prompt such as cmd.exe on Windows, or Bash on Linux or macOS. To run a command, copy and paste it in the shell prompt and hit **Enter**.
3. Install the Azure Machine Learning extension `ml`:

```azurecli
az extension add -n ml -y
```

4. Sign in to Azure:

```azurecli
az login
```

5. Set the default subscription. Replace **<YOUR_SUBSCRIPTION_ID>** with your **subscription ID**.

```azurecli
az account set -s "<YOUR_SUBSCRIPTION_ID>"
```

## Create an Azure resource group and set as default

To create a workspace with the CLI (v2), you need a resource group. You can create a new one with the CLI or use an existing resource group. Either way, make sure to set a resource group as the default to complete this exercise.

1. Create a resource group. Choose a location close to you.

> **Tip:** You can get a list of available locations with the `az account list-locations` command.

```azurecli
az group create --name "diabetes-dev-rg" --location "eastus"
```

2. Set the resource group as the default.

```azurecli
az configure --defaults group="diabetes-dev-rg"
```

## Create an Azure Machine Learning workspace and set as default

As its name suggests, a workspace is a centralized place to manage all of the Azure ML assets you need to work on a machine learning project.

1. Create a workspace:

```azurecli
az ml workspace create --workspace-name "aml-diabetes-dev"
```

2. Set the workspace as the default:

```azurecli
az configure --defaults workspace="aml-diabetes-dev"
```

You can check your work by signing in to the [Azure Machine Learning Studio](https://ml.azure.com). After you sign in, choose the *aml-diabetes-dev* workspace to open it.

## Create a Compute Instance

To run a notebook, you'll need a compute instance.

In this exercise, you'll create a compute instance with the following settings:
    - `--name`: *Name of compute instance. Has to be unique and fewer than 24 characters.*
    - `--size`: STANDARD_DS11_V2
    - `--type`: ComputeInstance
    - `--workspace-name`: *Will use the default workspace you've configured so you don't need to specify.*
    - `--resource-group`: *Will use the default resource group you've configured so you don't need to specify.*

1. Run the `az ml compute create` with the settings listed above. It should look something like this:

```azurecli
az ml compute create --name "testdev-vm" --size STANDARD_DS11_V2 --type ComputeInstance
```

## Create an environment

To execute a Python script, you'll need to install any necessary libaries and packages. To automate the installation of packages, you can use an environment.

To create an environment with the CLI (v2) you need two files:

1. The specification YAML file, including the environment name, version and base Docker image. Navigate to  **Allfiles/Labs/01/basic-env.yml** to explore the contents of this file.
2. The Conda environment file, including the libraries and packages you want installed. Navigate to **Allfiles/Labs/01/conda-envs/basic-env-cpu.yml** to explore the contents of this file.

Before you can run the command to create the environment, you need the two files stored on the computer you're running the CLI from.

3. Clone the repo `https://github.com/MicrosoftLearning/mslearn-aml-cli` or download and extract the ZIP to store the files locally.
4. From your shell prompt, navigate to the **Allfiles/Labs/01** folder.
5. Run the command:

```azurecli
az ml environment create --file basic-env.yml
```

Once the environment is created, a summary is shown in the prompt. You can also view the environment in the [Azure ML Studio](https://ml.azure.com) in the Environments tab.

## Create a dataset

To create a dataset in the workspace from a local CSV, you need two files:

1. The specification YAML file, including the dataset name, version and local path of the CSV file. Navigate to  **Allfiles/Labs/01/data-local-path.yml** to explore the contents of this file.
2. The CSV file containing data. In this exercise, you'll work with diabetes data. Navigate to **Allfiles/Labs/01/data/diabetes.csv** to explore the contents of this file.

Before you can run the command to create the dataset, you need the two files stored on the computer.

3. Clone this repo or download and extract the ZIP to store the files locally. 
4. From your shell prompt, navigate to the **Allfiles/Labs/01** folder.
5. Run the command:

```azurecli
az ml data create --file data-local-path.yml
```

When you create a dataset from a local path, the workspace will automatically upload the dataset to the default datastore. In this case, it will be uploaded to the storage account which was created when you created the workspace. 
Once the dataset is created, a summary is shown in the prompt. You can also view the environment in the [Azure ML Studio](https://ml.azure.com) in the Environments tab.

## Upload a notebook and train a model



## Clean up resources

When you're finished exploring Azure Machine Learning, shut down the compute instance to avoid unnecessary charges in your Azure subscription.

You can stop a compute instance with the following command. Change `"testdev-vm"` to the name of your compute instance if necessary.

```azurecli
az ml compute stop --name "testdev-vm" --no-wait
```

> **Note:** Stopping your compute ensures your subscription won't be charged for compute resources. You will however be charged a small amount for data storage as long as the Azure Machine Learning workspace exists in your subscription. If you have finished exploring Azure Machine Learning, you can delete the Azure Machine Learning workspace and associated resources. However, if you plan to complete any other labs in this series, you will need to repeat this lab to create the workspace and prepare the environment first.

To delete the Azure Machine Learning workspace, you can use the following command in the CLI:

```azurecli
az ml workspace delete
```
