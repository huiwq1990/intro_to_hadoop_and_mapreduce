#!/usr/bin/python
"""Reducer of Final Project: Top Tags

Output Top 10 tags, ordered by the number of questions they appear in
"""

import sys
import csv

def update_top10(top10, eleventh, ignore_val, count, pre_tag):
    if len(eleventh) > 0: #####
        print pre_tag, count
    if len(top10) < 10:
        if (len(eleventh) > 0) and (count
                                    == eleventh.values()[0]):
            eleventh[pre_tag] = count
        elif count > ignore_val:
            top10[pre_tag] = count

    else:
        min_key = min(top10.items(), key=lambda x:x[1])[0]
        min_value = top10[min_key]
        if count == min_value:
            top10[pre_tag] = count
        elif (len(eleventh) > 0) and (count
                                      == eleventh.values()[0]):
            eleventh[pre_tag] = count
        elif min_value < count:
            if len(eleventh) > 0:
                ignore_val = eleventh.values()[0]
                eleventh.clear()
            for k, v in top10.items():
                if v == min_value:
                    eleventh[k] = v
                    del(top10[k])
            top10[pre_tag] = count

    print top10, len(top10)
    print eleventh, len(eleventh)
    print ignore_val
    print "\n"

    return ignore_val

def reducer():
    """Select Output from Input.

    Input
    tag

    Output
    Top 10 tags
    """

    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)

    count = 0
    pre_tag = ""
    top10 = {}
    eleventh = {}
    ignore_val = -1
    for line in reader:
        if len(line) != 1: # ignore outlier
            continue
        else:
            tag = line[0]
            if tag != pre_tag and pre_tag != "":
                ignore_val = update_top10(top10, eleventh, 
                                          ignore_val, count, pre_tag)
                count = 1
                pre_tag = tag

            else:
                count += 1
                pre_tag = tag

    ignore_val = update_top10(top10, eleventh, ignore_val, count, pre_tag)

def main():
    reducer()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
