#!/bin/bash

options=("--html=report.html")
options+=("--self-contained-html")

if [ -z "$1" ]
  then
    echo "Run full test cases"
  else
    options+=("-m" "$1")
fi

echo "about to launch pytest ${options[@]}"
pytest "${options[@]}"

