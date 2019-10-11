#!/bin/sh

model_id=$1

curl -v -X PUT  http://localhost:5000/trainings/$model_id/accept & \
curl -v -X PUT  http://localhost:5001/trainings/$model_id/accept & \
curl -v -X PUT  http://localhost:5002/trainings/$model_id/accept & \
curl -v -X PUT  http://localhost:5003/trainings/$model_id/accept & \
curl -v -X PUT  http://localhost:5004/trainings/$model_id/accept
