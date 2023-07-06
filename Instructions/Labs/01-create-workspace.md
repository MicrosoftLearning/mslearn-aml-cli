---
lab:
    title: 'Lab: Create an Azure Machine Learning workspace and assets with the CLI (v2)'
    module: 'Module: Create Azure Machine Learning resources with the CLI (v2)'
---

# Create an Azure Machine Learning workspace and assets with the CLI (v2)

In this exercise, you will create and explore an Azure Machine Learning workspace using the Azure Cloud Shell.

## Set up the Azure Cloud Shell and install the Azure Machine Learning extension

To start, open the Azure Cloud Shell, install the Azure Machine Learning extension and clone the Git repo.

1. In a browser, open the Azure portal at [http://portal.azure.com](https://portal.azure.com/?azure-portal=true), signing in with your Microsoft account.
1. Select the [>_] (*Cloud Shell*) button at the top of the page to the right of the search box. This opens a Cloud Shell pane at the bottom of the portal.
1. The first time you open the cloud shell, you will be asked to choose the type of shell you want to use (*Bash* or *PowerShell*). Select **Bash**.
1. If you are asked to create storage for your cloud shell, check that the correct subscription is specified and select **Create storage**. Wait for the storage to be created.
1. Check to see if the Azure Machine Learning extension is installed with the following command:

    ```azurecli
    az extension list
    ```

    > **Tip:** Adding **-o table** at the end of the command will format the output in a table, making it easier to read for some people. The command would then be: `az extension list -o table`

1. If it is not intalled, use the following command to install the Azure Machine Learning extension:

    ```azurecli
    az extension add -n ml -y
    ```

1. In the command shell, clone this Github repository to download all necessary files which are stored in the *Allfiles* folder.

    ```azurecli
    git clone https://github.com/MicrosoftLearning/mslearn-aml-cli.git mslearn-aml-cli
    ```

1. The files are downloaded to a folder named **mslearn-aml-cli**. To see the files in your Cloud Shell storage and work with them, type the following command in the shell:

    ```azurecli
    code .
    ```

## Create an Azure resource group and set as default

To create a workspace with the CLI (v2), you need a resource group. You can create a new one with the CLI or use an existing resource group. Either way, make sure to set a resource group as the default to complete this exercise.

> **Tip:** You can get a list of available locations with the `az account list-locations -o table` command. Use the **name** column for the location name

1. Run the following command to create a resource group and use a location close to you:

    ```azurecli
    az group create --name "diabetes-dev-rg" --location "eastus"
    ```

1. Set the resource group as the default to avoid having to specify it on every command going forward:

    ```azurecli
    az configure --defaults group="diabetes-dev-rg"
    ```

## Create an Azure Machine Learning workspace and set as default

As its name suggests, a workspace is a centralized place to manage all of the Azure ML assets you need to work on a machine learning project.

1. Create a workspace:

    ```azurecli
    az ml workspace create --name "aml-diabetes-dev"
    ```

1. Set the workspace as the default:

    ```azurecli
    az configure --defaults workspace="aml-diabetes-dev"
    ```

1. Check your work by signing in to the [Azure Machine Learning Studio](https://ml.azure.com). After you sign in, choose the *aml-diabetes-dev* workspace to open it.

## Create a Compute Instance

To run a notebook, you'll need a compute instance.

In this exercise, you'll create a compute instance with the following settings:

- `--name`: *Name of compute instance. Has to be unique and fewer than 24 characters.*
- `--size`: STANDARD_DS11_V2
- `--type`: ComputeInstance
- `--workspace-name`: *Will use the default workspace you've configured so you don't need to specify.*
- `--resource-group`: *Will use the default resource group you've configured so you don't need to specify.*

1. Run the `az ml compute create` with the settings listed above. Change the name to make it unique in your region. It should look something like this:

    ```azurecli
    az ml compute create --name "testdev-vm" --size STANDARD_DS11_V2 --type ComputeInstance
    ```

    > **Note:** If a compute instance with the name "testdev-vm" already exists, change the name to make it unique within your Azure region, with a maximum of 24 characters. If you get an error because the name is not unique, delete the partially created compute instance with `az ml compute delete --name "compute-instance-name"`.

1. The command will take 2 to 5 minutes to complete. After that, switch to [Azure Machine Learning Studio](https://ml.azure.com), open the **Compute** tab and confirm that the instance has been created and is running.

## Create an environment

To execute a Python script, you'll need to install any necessary libraries and packages. To automate the installation of packages, you can use an environment.

To create an environment from a Docker image plus a Conda environment with the CLI (v2) you need two files:

- The specification YAML file, including the environment name, version and base Docker image.
- The Conda environment file, including the libraries and packages you want installed.

The necessary YAML files have already been created for you and are part of the **mslearn-aml-cli** repo you cloned in the Azure Cloud Shell.

1. To navigate to the YAML files, run the following command in the Cloud Shell:

    ```azurecli
    code .
    ```

1. Navigate to the **mslearn-aml-cli/Allfiles/Labs/01** folder.
1. Select the **basic-env.yml** file to open it. Explore its contents which describes how the environment should be created within the Azure ML workspace.
1. Select the **conda-envs/basic-env-cpu.yml** file to open it. Explore its contents which list the libraries that need to be installed on the compute.
1. Run the following command to create the environment :

    ```azurecli
    az ml environment create --file ./mslearn-aml-cli/Allfiles/Labs/01/basic-env.yml
    ```

1. Once the environment is created, a summary is shown in the prompt. You can also view the environment in the **Azure Machine Learning Studio** in the **Environments** tab, under *Custom environments*.

## Create a dataset

To create a dataset in the workspace from a local CSV, you need two files:

- The specification YAML file, including the dataset name, version and local path of the CSV file. Navigate to  **Allfiles/Labs/01/data-local-path.yml** to explore the contents of this file.
- The CSV file containing data. In this exercise, you'll work with diabetes data. Navigate to **Allfiles/Labs/01/data/diabetes.csv** to explore the contents of this file.

Before you create a dataset, you can explore the files by using the `code .` command in the Cloud Shell.

1. Run the following command to create a dataset from the configuration described in `data-local-path.yml`:

    ```azurecli
    az ml data create --file ./mslearn-aml-cli/Allfiles/Labs/01/data-local-path.yml
    ```

    >**Note:** When you create a dataset from a local path, the workspace will automatically upload the dataset to the default datastore. In this case, it will be uploaded to the storage account which was created when you created the workspace.

2. Once the dataset is created, a summary is shown in the prompt. You can also view the environment in the **Azure Machine Learning Studio** in the **Data** tab, under *Data assets*.

## Clean up resources

Once you've finished exploring Azure Machine Learning, shut down the compute instance to avoid unnecessary charges in your Azure subscription.

You can stop a compute instance with the following command. Change `"testdev-vm"` to the name of your compute instance if necessary.

```azurecli
az ml compute stop --name "testdev-vm" --no-wait
```

> **Note:** Stopping your compute ensures your subscription won't be charged for compute resources. You will however be charged a small amount for data storage as long as the Azure Machine Learning workspace exists in your subscription. If you have finished exploring Azure Machine Learning, you can delete the Azure Machine Learning workspace and associated resources. However, if you plan to complete any other labs in this series, you will need to repeat this lab to create the workspace and prepare the environment first.

To delete the complete Azure Machine Learning workspace and all assets you created, you can use the following command in the CLI:

```azurecli
az ml workspace delete
```
