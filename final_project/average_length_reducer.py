#!/usr/bin/python
"""Reducer of Final Project: Post and Answer Length

Output the length of the post and the average answer length for each post
"""

import sys
import csv

def reducer():
    """Select Output from Input.

    Input (tab-delimited):
    - for question: "id" "node_type" "length_body"
    - for answer: "abs_parent_id" "node_type" "length_body"

    Output (tab-delimited):
    "id" "length_body of question" "average length_body of answer"
    """

    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)

    total_len = 0
    total_count = 0
    for line in reader:
        # question always follows answers
        if len(line) == 4:	# answer
            total_len += int(line[2])
            total_count += 1
        elif len(line) == 3:	# question
            if total_count != 0:
                writer.writerow([line[0], line[2],
                                 float(total_len) / total_count])
            else:
                writer.writerow([line[0], line[2], 0])

            total_len = 0
            total_count = 0

def main():
    reducer()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
