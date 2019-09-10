#!/bin/sh

curl -v -X POST -F file=@"datasets/file.csv" http://localhost:5000/datasets & \
curl -v -X POST -F file=@"datasets/file.csv" http://localhost:5001/datasets & \
curl -v -X POST -F file=@"datasets/file.csv" http://localhost:5002/datasets & \
curl -v -X POST -F file=@"datasets/file.csv" http://localhost:5003/datasets & \
curl -v -X POST -F file=@"datasets/file.csv" http://localhost:5004/datasets 
