#!/bin/bash

options=()

echo "$1"

if [ -z "${*:2}" ]
  then
    echo "Run full test cases"
  else
    options+=("-m" "${*:2}")
fi

options+=("--html=report.html")
options+=("--self-contained-html")

echo "About to launch pytest ${options[@]}"
pytest "${options[@]}"
