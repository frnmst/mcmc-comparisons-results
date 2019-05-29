#!/usr/bin/env bash

set -euo pipefail

EXPERIMENTS='26 27 28 29 30 31 34 36 39 40 42 44 45 46 47 48 49 50 97 98 99'

set -x
for e in ${EXPERIMENTS}; do
    ./extract_and_write_raw_data_by_type.py data/experiment-00${e}/job-*.csv
    mkdir -p data/experiment-00${e}/extracted
    mv *.txt data/experiment-00${e}/extracted
done
set +x
