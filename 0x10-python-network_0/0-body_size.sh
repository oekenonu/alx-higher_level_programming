#!/bin/bash
# Script takes in a URL and displays the size of the body of the response

curl -Is "$1" | wc -c
