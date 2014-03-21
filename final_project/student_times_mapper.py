#!/usr/bin/python
"""Mapper of Final Project: Students and Posting Time on Forums

Find for each student what is the hour during which
the student has posted the most posts.
"""

import sys
import csv
import re
from datetime import datetime


def mapper():
    """Select Output from Input.

    Input (tab-delimited):
    "id" "title" "tagnames" "author_id" "body" "node_type"
    "parent_id" "abs_parent_id" "added_at" "score" "state_string"
    "last_edited_id" "last_activity_by_id" "last_activity_at"
    "active_revision_id" "extra" "extra_ref_id" "extra_count" "marked"

    Output (tab-delimited):
    "author_id" "hour"
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
            author_id = line[3].strip()
            added_at = line[8].strip()
            hour = added_at.split(" ")[1].split(":")[0]
            writer.writerow([author_id, hour])

def main():
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
