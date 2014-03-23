#!/usr/bin/python
"""Mapper of Final Project: Top Tags

Output Top 10 tags, ordered by the number of questions they appear in
"""

import sys
import csv
import re

def mapper():
    """Select Output from Input.

    Input (tab-delimited):
    "id" "title" "tagnames" "author_id" "body" "node_type"
    "parent_id" "abs_parent_id" "added_at" "score" "state_string"
    "last_edited_id" "last_activity_by_id" "last_activity_at"
    "active_revision_id" "extra" "extra_ref_id" "extra_count" "marked"

    Output
    "tag"
    """

    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)

    r = '[0-9]'
    for line in reader:
        if len(line) != 19: # ignore outlier
            continue
        elif not re.match(r, line[0].strip()): # skip header
            continue
        else:
            tagnames = line[2].strip().split(" ")
            for tag in tagnames:
                if tag:
                    writer.writerow([tag])

def main():
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
