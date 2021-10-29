---
lab:
    title: 'Lab: Run a basic Python training job'
    module: 'Module 1: Run jobs in Azure Machine Learning with CLI (v2)'
---

# Run a basic Python training job

In this exercise, you will train a model with a Python script.

## Prerequisites

Before you continue, complete the [*Create an Azure Machine Learning Workspace and assets with the CLI (v2)*](Instructions/Labs/01-create-workspace.md) lab to set up your Azure Machine Learning environment.

To do this lab, you'll need the files from the Labs 02 folder on your computer: mslearn-aml-cli/Allfiles/Labs/02. Clone this repo to your local computer or download the repo as a ZIP and extract the files to a local path.

## Train a model

To train a model...

1. Initiate the job

```azurecli
az ml job create --file jobs/train/job.yml --web
```

1. Monitor in Studio
