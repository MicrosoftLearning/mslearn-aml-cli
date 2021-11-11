# ---
# lab:
#    title: 'Lab: Deploy a model to a managed online endpoint'
#    module: 'Module 4: Deploy an Azure Machine Learning model to a managed endpoint with CLI (v2)'
# ---

# Deploy a model to a managed online endpoint

In this exercise, you will deploy a model to a managed online endpoint.

## Prerequisites

Before you continue, complete the [*Create an Azure Machine Learning Workspace and assets with the CLI (v2)*](Instructions/Labs/01-create-workspace.md) lab to set up your Azure Machine Learning environment.

To do this lab, you'll need the files from the Labs 04 folder on your computer: mslearn-aml-cli/Allfiles/Labs/04. Clone this repo to your local computer or download the repo `https://github.com/MicrosoftLearning/mslearn-aml-cli` as a ZIP and extract the files to a local path.

## Train a model

To train a model...

1. Initiate the job

```azurecli
az ml job create --file jobs/train/job.yml --web
```

1. Monitor in Studio
