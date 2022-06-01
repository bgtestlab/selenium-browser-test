#!/bin/bash

options=()

if [ -z "$@" ]
  then
    echo "Run full test cases"
  else
    options+=("-m" "$@")
fi

options+=("--html=report.html")
options+=("--self-contained-html")

echo "About to launch pytest ${options[@]}"
pytest "${options[@]}"

