#!/usr/bin/env python3

import sys
import os

books = """Genesis (Ge)
Exodus (Exo)
Leviticus (Lev)
Numbers (Num)
Deuteronomy (Deu)
Joshua (Josh)
Judges (Jdgs)
Ruth (Ruth)
1 Samuel (1Sm)
2 Samuel (2Sm)
1 Kings (1Ki)
2 Kings (2Ki)
1 Chronicles (1Chr)
2 Chronicles (2Chr)
Ezra (Ezra)
Nehemiah (Neh)
Esther (Est)
Job (Job)
Psalms (Psa)
Proverbs (Prv)
Ecclesiastes (Eccl)
Song of Solomon (SSol)
Isaiah (Isa)
Jeremiah (Jer)
Lamentations (Lam)
Ezekiel (Eze)
Daniel (Dan)
Hosea (Hos)
Joel (Joel)
Amos (Amos)
Obadiah (Obad)
Jonah (Jonah)
Micah (Mic)
Nahum (Nahum)
Habakkuk (Hab)
Zephaniah (Zep)
Haggai (Hag)
Zechariah (Zec)
Malachi (Mal)
Matthew (Mat)
Mark (Mark)
Luke (Luke)
John (John)
The Acts (Acts)
Romans (Rom)
1 Corinthians (1Cor)
2 Corinthians (2Cor)
Galatians (Gal)
Ephesians (Eph)
Philippians (Phi)
Colossians (Col)
1 Thessalonians (1Th)
2 Thessalonians (2Th)
1 Timothy (1Tim)
2 Timothy (2Tim)
Titus (Titus)
Philemon (Phmn)
Hebrews (Heb)
James (Jas)
1 Peter (1Pet)
2 Peter (2Pet)
1 John (1Jn)
2 John (2Jn)
3 John (3Jn)
Jude (Jude)
Revelation (Rev)"""

apocrypha = {
    "Tobit": ["Tob", 67],
    "Judit": ["Jdt", 68],
    "Weisheit": ["Wis", 70],
    "Sirach": ["Sir", 71],
    "Baruch": ["Bar", 72],
    "Brief Jeremias": ["1Jer", 74],
    "1. Makkabäer": ["1Mac", 76],
    "2. Makkabäer": ["2Mac", 77],
    "Zusätze Ester": ["AddEst", 78],
    "Gebet Manasses": ["Man", 79],
    "Zusätze Daniel": ["AddDan", 81]
}

book_abbrevs = []
for book in books.split("\n"):
    book_abbrevs.append(book.split("(")[1].split(")")[0].strip())


to_read = sys.argv[1]
file_name = os.path.basename(to_read)
book_number = file_name.split(" - ")[0].strip()

if len(sys.argv) == 3:
    book_number = sys.argv[2]

book_name = file_name.split(" - ")[1].strip().split(".txt")[0].strip()

book_abbrev = book_abbrevs[int(book_number) - 1]

print(book_name)
if book_name in apocrypha:
    book_abbrev = apocrypha[book_name][0]
    book_number = apocrypha[book_name][1]

print(book_abbrev)
print(book_number)

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
