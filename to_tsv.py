#!/usr/bin/env python3

import sys

book_name = sys.argv[1]
book_abbrev = sys.argv[2]
book_number = sys.argv[3]
to_read = sys.argv[4]

curr_chapter = -1
new_lines = [""]

with open(to_read, "r") as f:
    old_lines = f.readlines()

for line in old_lines:
    if line.startswith("Kapitel "):
        curr_chapter = line.split("Kapitel ")[1].strip()
    elif curr_chapter != -1 and line.split(" ")[0].isdigit():
        l = line.split(" ")
        verse_num = l[0]
        verse = " ".join(l[1:])
        new_lines.append(f"{book_name}\t{book_abbrev}\t{book_number}\t{curr_chapter}\t{verse_num}\t{verse}".replace("\n", "\r\n"))

with open("books/" + book_name + ".tsv", "w") as f:
    f.writelines(new_lines)
