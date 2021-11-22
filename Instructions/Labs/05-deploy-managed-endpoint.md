# Deploy a model to a managed online endpoint

In this exercise, you will deploy a model to a managed online endpoint.

## Prerequisites



## Deploy a model

### MLflow endpoint

```azurecli
az ml online-endpoint create --name diabetes-mlflow -f ./mslearn-aml-cli/Allfiles/Labs/05/mlflow-endpoint/create-endpoint.yml
```

```azurecli
az ml online-deployment create --name mlflow-deployment --endpoint diabetes-mlflow -f ./mslearn-aml-cli/Allfiles/Labs/05/mlflow-endpoint/mlflow-deployment.yaml --all-traffic
```
