#!/bin/bash

options=("--html=report.html")
options+=("--self-contained-html")

echo "about to launch pytest ${options[@]}"
pytest "${options[@]}"