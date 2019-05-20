#!/usr/bin/env python3

import sys
import csv

# Warning: this script works for *_three experiments. You must specify
# the total number of runs manually here:
MAX_RUNS=4
NUMBER_OF_FIELDS=8

class NotEnoughFields(Exception):
    """NotEnoughFields."""

def get_and_write(filename_in: str, delimiter: str = ','):
    run_number=dict()
    for i in range(1, MAX_RUNS+1):
        run_number[str(i)]=dict()
        run_number[str(i)]['samples'] = list()
        run_number[str(i)]['mh_time'] = list()
        run_number[str(i)]['mh_prob'] = list()
        run_number[str(i)]['gibbs_time'] = list()
        run_number[str(i)]['gibbs_prob'] = list()
        run_number[str(i)]['rejection_time'] = list()
        run_number[str(i)]['rejection_prob'] = list()

    with open(filename_in, 'r') as f:
        data = csv.reader(f, delimiter=delimiter)
        for row in data:
            if len(row) < NUMBER_OF_FIELDS:
                raise NotEnoughFields
            run_number[row[0]]['samples'].append(row[1])
            run_number[row[0]]['mh_time'].append(row[2])
            run_number[row[0]]['mh_prob'].append(row[3])
            run_number[row[0]]['gibbs_time'].append(row[4])
            run_number[row[0]]['gibbs_prob'].append(row[5])
            run_number[row[0]]['rejection_time'].append(row[6])
            run_number[row[0]]['rejection_prob'].append(row[7])

    prefix_finename_out = ['mh_samples_time', 'mh_samples_prob', 'gibbs_samples_time', 'gibbs_samples_prob', 'rejection_samples_time', 'rejection_samples_prob']
    id = ['mh_time', 'mh_prob', 'gibbs_time', 'gibbs_prob', 'rejection_time', 'rejection_prob']
    for i in range(1, MAX_RUNS+1):
        w = 0
        for filename in prefix_finename_out:
            filename_with_run_number = filename + '_' + str(i) + '.txt'
            with open(filename_with_run_number, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=delimiter)
                for x in range(0, len(run_number[str(i)]['samples'])):
                    csvwriter.writerow([run_number[str(i)]['samples'][x], run_number[str(i)][id[w]][x]])
        w += 1

if __name__ == '__main__':
    filename_in=sys.argv[1]
    get_and_write(filename_in)

