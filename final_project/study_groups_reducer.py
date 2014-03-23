#!/usr/bin/python
"""Reducer of Final Project: Study Groups

Output threads ID and their participants ID
"""

import sys
import csv

def reducer():
    """Select Output from Input.

    Input (tab-delimited):
    - for question: "id" "node_type" "autor_id"
    - for answer: "abs_parent_id" "node_type" "author_id" "id"
    - for comment: "abs_parent_id" "node_type" "author_id" "id"

    Output (tab-delimited):
    "id" "author_id"
    """

    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)

    authors = []
    for line in reader:
        # comments always follows answers
        # question always follows comments
        if len(line) == 4:	# answer of comment
            authors += [line[2]]
        elif len(line) == 3:	# question
            authors += [line[2]]
            authors.reverse()
            writer.writerow([line[0]] + authors)
            authors = []

def main():
    reducer()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
