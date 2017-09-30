#!/bin/sh

for file in */*.txt; do
    echo ${file}
    nkf -d "${file}" | ./extract_text.py >> input.txt
done
