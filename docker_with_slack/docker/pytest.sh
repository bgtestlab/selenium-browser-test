#!/bin/bash

options=("--html=report.html")
options+=("--self-contained-html")
options+=("-m" "not sanity")
echo "about to launch pytest ${options[@]}"
pytest "${options[@]}"
