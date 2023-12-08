#!/usr/bin/python3
import re
def str_match(search_str):
    pattern = re.compile(r"(([0-2][0-5]{2}|[0-2][0-4][0-9]|[0-1]" +
                         r"[0-9]{1,2}|[0-9]{1,2}).){3}([0-2][0-5]" +
                         r"{2}|[0-2][0-4][0-9]|[0-1][0-9]{1,2}|" +
                         r"[0-9]{1,2})\s?\-\s?\[.*\] \"GET " +
                         r"/projects/260 HTTP/1\.1\" \d+ \d+$")
    match = pattern.match(search_str)
    return match


with open("test_file2.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        print(str_match(line.rstrip('\n')))
