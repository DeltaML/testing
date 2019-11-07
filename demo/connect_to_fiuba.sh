#!/bin/sh

ssh -L 7070:localhost:7070 -L 9090:localhost:9090 -L 4000:localhost:4000 -L 4001:localhost:4001 -L 4002:localhost:4002 -L 4003:localhost:4003 -L 4004:localhost:4004 -L 5001:localhost:5001 -L 5002:localhost:5002 -L 5003:localhost:5003 -L 5004:localhost:5004 -L 8545:localhost:8545 -L 8080:localhost:8080 deltaml@antiguos.fi.uba.ar
