#!/usr/bin/env bash

set -euo pipefail

EXPERIMENTS='26 27 28 29 30 31 34 36 39'

for e in ${EXPERIMENTS}; do
    ./extract_and_write_raw_data_by_type.py data/experiment-00${e}/job-*.csv
    mkdir -p data/experiment-00${e}/extracted
    mv *.txt data/experiment-00${e}/extracted
done
