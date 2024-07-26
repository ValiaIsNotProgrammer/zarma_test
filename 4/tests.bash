#!/bin/bash

for ((i=1; i<=8; i++)); do
    python 4.py get_squares_v$i
done
