#!/usr/bin/python
"""Reducer of Final Project: Students and Posting Time on Forums

Find for each student what is the hour during which
the student has posted the most posts.
"""

import sys
import csv
from operator import itemgetter

def reducer():
    """Select Output from Input.

    Input (tab-delimited):
    "author_id" "hour"

    Output (tab-delimited):
    "author_id" "the hour"
    """

    reader = csv.reader(sys.stdin, delimiter='\t')

    pre_author_id = -1
    hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
             13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    counts = [0] * 24;
    for line in reader:
        if len(line) != 2: # ignore outlier
            continue
        else:
            author_id, hour = line
            # Same author_id will appear in succession cuz input is sorted.
            if (author_id != pre_author_id) and (pre_author_id >= 0):
                write_hot_hour(hours, counts, pre_author_id)

                for i in range(len(counts)):
                    counts[i] = 0

                counts[int(hour)] += 1
                pre_author_id = author_id

            else:
                counts[int(hour)] += 1
                pre_author_id = author_id

    write_hot_hour(hours, counts, pre_author_id)

def write_hot_hour(hours, counts, author_id):
    '''Write result
    @param hours list that has 24 elements
    @param counts list that has 24 elements
    @param author_id
    '''
    writer = csv.writer(sys.stdout, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)

    d = dict((x, y) for x, y in zip(hours, counts))
    for k, v in sorted(d.items(), 
                       key=itemgetter(1,0), reverse=True):
        if v != max(counts):
            break
        else:
            writer.writerow([author_id, k])

def main():
    reducer()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
