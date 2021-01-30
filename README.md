# airflow-kubernetes-fbprophet

## build - 
```bash
docker build --tag='<image_name:v1>' .
```
## test - 
set path to service account json key file


```bash
docker run -e GOOGLE_APPLICATION_CREDENTIALS=<path/to/service/key/key.json> -v $GOOGLE_APPLICATION_CREDENTIALS:<path/to/service/key/key.json>:ro <image_name:v1>
```
https://cloud.google.com/run/docs/testing/local

## tag -
```bash 
docker tag <image_name:v1> gcr.io/<project_id>/<image_name:v1>
```

## deploy - 
```bash
docker push gcr.io/<project_id>/<image_name:v1>/<image_name:v1>
```
