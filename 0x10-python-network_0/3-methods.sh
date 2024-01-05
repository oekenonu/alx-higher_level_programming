#!bin/bash
# Script to display HTTP methods allowed on server
curl -sI "$1" | grep "Allow" | cut -d" " -f2-
