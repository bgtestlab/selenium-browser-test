#!/bin/bash

options=("--html=report.html")
options+=("--self-contained-html")

if [ -z "$@" ]
  then
    echo "Run full test cases"
  else
    options+=("-m" "\"$@\"")
fi

echo "about to launch pytest ${options[@]}"
pytest "${options[@]}"

