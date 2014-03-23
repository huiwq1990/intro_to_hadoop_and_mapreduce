#!/usr/bin/python
"""Mapper of Final Project: Study Groups

Output threads ID and their participants ID
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

    Output (tab-delimited):
    - for question: "id" "node_type" "autor_id"
    - for answer: "abs_parent_id" "node_type" "author_id" "id"
    - fof comment: "abs_parent_id" "node_type" "author_id" "id"
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
            node_id = line[0].strip()
            author_id = line[3].strip()
            node_type = line[5].strip()
            abs_parent_id = line[7].strip()

            if node_type == "question":
                writer.writerow([node_id, node_type, author_id])
            elif (node_type == "answer") | (node_type == "comment"):
                writer.writerow([abs_parent_id, node_type, author_id, node_id])

def main():
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
