---
lab:
    title: 'Lab: Track and manage models with MLflow'
    module: 'Module 3: Use MLflow with Azure ML jobs submitted with the CLI (v2)'
---

# Track and manage models with MLflow

In this exercise, you will train a model with a Python script.

## Prerequisites

Before you continue, complete the [*Create an Azure Machine Learning Workspace and assets with the CLI (v2)*](Instructions/Labs/01-create-workspace.md) lab to set up your Azure Machine Learning environment.

To do this lab, you'll need the files from the Labs 02 folder on your computer: mslearn-aml-cli/Allfiles/Labs/02. Clone this repo to your local computer or download the repo `https://github.com/MicrosoftLearning/mslearn-aml-cli` as a ZIP and extract the files to a local path.

## Train a model

To train a model...

1. Initiate the job

```azurecli
az ml job create --file jobs/train/job.yml --web
```

1. Monitor in Studio
