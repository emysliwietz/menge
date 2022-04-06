#!/usr/bin/env python3

import sys
import os

books = {
    "Genesis": ["Ge", 1],
    "Exodus": ["Exo", 2],
    "Levitikus": ["Lev", 3],
    "Numeri": ["Num", 4],
    "Deuteronomium": ["Deu", 5],
    "Josua": ["Josh", 6],
    "Richter": ["Jdgs", 7],
    "Rut": ["Ruth", 8],
    "1. Samuel": ["1Sm", 9],
    "2. Samuel": ["2Sm", 10],
    "1. Könige": ["1Ki", 11],
    "2. Könige": ["2Ki", 12],
    "1. Chronik": ["1Chr", 13],
    "2. Chronik": ["2Chr", 14],
    "Esra": ["Ezra", 15],
    "Nehemia": ["Neh", 16],
    "Ester": ["Est", 17],
    "Hiob": ["Job", 18],
    "Psalmen": ["Psa", 19],
    "Sprüche": ["Prv", 20],
    "Prediger": ["Eccl", 21],
    "Hoheslied": ["SSol", 22],
    "Jesaja": ["Isa", 23],
    "Jeremia": ["Jer", 24],
    "Klagelieder": ["Lam", 25],
    "Hesekiel": ["Eze", 26],
    "Daniel": ["Dan", 27],
    "Hosea": ["Hos", 28],
    "Joel": ["Joel", 29],
    "Amos": ["Amos", 30],
    "Obadja": ["Obad", 31],
    "Jona": ["Jonah", 32],
    "Micha": ["Mic", 33],
    "Nahum": ["Nahum", 34],
    "Habakuk": ["Hab", 35],
    "Zefanja": ["Zep", 36],
    "Haggai": ["Hag", 37],
    "Sacharja": ["Zec", 38],
    "Maleachi": ["Mal", 39],
    "Matthew": ["Mat", 40],
    "Mark": ["Mark", 41],
    "Luke": ["Luke", 42],
    "John": ["John", 43],
    "The Acts": ["Acts", 44],
    "Romans": ["Rom", 45],
    "1 Corinthians": ["1Cor", 46],
    "2 Corinthians": ["2Cor", 47],
    "Galatians": ["Gal", 48],
    "Ephesians": ["Eph", 49],
    "Philippians": ["Phi", 50],
    "Colossians": ["Col", 51],
    "1 Thessalonians": ["1Th", 52],
    "2 Thessalonians": ["2Th", 53],
    "1 Timothy": ["1Tim", 54],
    "2 Timothy": ["2Tim", 55],
    "Titus": ["Titus", 56],
    "Philemon": ["Phmn", 57],
    "Hebrews": ["Heb", 58],
    "James": ["Jas", 59],
    "1 Peter": ["1Pet", 60],
    "2 Peter": ["2Pet", 61],
    "1 John": ["1Jn", 62],
    "2 John": ["2Jn", 63],
    "3 John": ["3Jn", 64],
    "Jude": ["Jude", 65],
    "Revelation": ["Rev", 66],
}

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
    "Zusätze Daniel": ["AddDan", 81],
}


def parse_book(to_read):
    file_name = os.path.basename(to_read)
    book_name = file_name.split(" - ")[1].strip().split(".txt")[0].strip()

    if book_name in books:
        book_abbrev = books[book_name][0]
        book_number = books[book_name][1]
    elif book_name in apocrypha:
        book_abbrev = apocrypha[book_name][0]
        book_number = apocrypha[book_name][1]
    else:
        print(f"Unable to find name of: {file_name}")
        return

    print(f"{book_number} {book_name} {book_abbrev}")

    curr_chapter = -1
    new_lines = [""]
    is_text = False

    with open(file_name, "r") as f:
        old_lines = f.readlines()

        for line in old_lines:
            if line.startswith("Kapitel "):
                curr_chapter = line.split("Kapitel ")[1].strip()
            elif curr_chapter != -1 and line.split(" ")[0].isdigit():
                l = line.split(" ")
                verse_num = l[0]
                verse = " ".join(l[1:])
                new_lines.append(
                    f"{book_name}\t{book_abbrev}\t{book_number}\t{curr_chapter}\t{verse_num}\t{verse}".replace(
                        "\n", "\r\n"
                    )
                )
                is_text = True
            elif line.isspace():
                is_text = False
            elif curr_chapter != -1 and is_text:
                last_line = new_lines.pop().replace("\r\n", " ")
                last_line += line.replace("\n", "\r\n")
                new_lines.append(last_line)
                print(last_line)
            else:
                pass

    with open("books/" + book_name + ".tsv", "w") as f:
        f.writelines(new_lines)


if len(sys.argv) == 1:
    print(f"Usage: {sys.argv[0]} {{source_dir}}")
    exit()

for f in os.listdir(sys.argv[1]):
    f = os.path.join(sys.argv[1], f)
    if os.path.isfile(f):
        parse_book(f)
