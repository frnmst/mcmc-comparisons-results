#!/usr/bin/env bash

set -euo pipefail

EXPERIMENTS='26 27 28 29 30 31 34'

for e in ${EXPERIMENTS}; do
    ./extract_and_write_raw_data_by_type.py data/experiment-00${e}/job-*.csv
    mv *.txt data/experiment-00${e}/extracted
done
