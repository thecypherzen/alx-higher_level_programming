#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 14(advanced)

Title: Log Parsing:
    mimicks parsing  a log(string) into meanigful output

Function(s):
    sig_interrupt: handler for SIGINT(ctrl + C) interrupt
    print_log: prints log information to stdout
    log_update: updates log information

Notes:
    - Input format: ``<IP Address> - [<date>] \
        "GET /projects/260 HTTP/1.1" <status code> \
            <file size>``
    - Every 10 lines and after a keyboard interruption (CTRL + C),
        prints the stats since the beginning
        Format:
            Total size: <total size>, where total_size is sum of all
                sizes so far; followed by
            <status code> : <count of stat code>:
    - possible stat codes: 200, 301, 400, 401, 403, 404, 405 and 500
        if a status code doesn't appear, nothing should be printed
        for that code.
    - status codes should be printed in ascending order
"""


import sys
import time
import signal


# interrupt signal handler
def sig_interrupt(signum, frame):
    """SIGINT handler function"""
    global log_data, total_size
    print_log(log_data, total_size)


signal.signal(signal.SIGINT, sig_interrupt)


# print log information
def print_log(data, total):
    """prints log information to stdout

    Parameters:
        data(:obj:dict): dictionary of stat info
        total(:obj:int): total size of data read so far

    Return: None
    """
    print("File size: {}".format(total))
    for key, value in data.items():
        if value["count"]:
            print("{}: {}".format(key, value["count"]), flush=True)


# global variables definition
log_data = {
    '200': {"count": 0, "size": 0},
    '301': {"count": 0, "size": 0},
    '400': {"count": 0, "size": 0},
    '401': {"count": 0, "size": 0},
    '403': {"count": 0, "size": 0},
    '404': {"count": 0, "size": 0},
    '405': {"count": 0, "size": 0},
    '500': {"count": 0, "size": 0}
}

total_size = 0
itr = 0


def log_update(line):
    """Log Updating fuction

    Parses the line read from stdin, extracts relevant stats
        and updates the ``log_data`` dict

    Parameters:
        line: the current line read

    Returns: None
    """
    global log_data, total_size, itr
    line = line.rstrip('\n').split(" ")
    itr += 1
    log_size = int(line[8])
    key = line[7]
    if key in log_data:
        log_data[key]["count"] += 1
        log_data[key]["size"] += log_size
        total_size += log_size
        if not itr % 10:
            print_log(log_data, total_size)


if __name__ == "__main__":
    """Entry point

    Reads line from stdin and passes to log_update function
    """
    for line in sys.stdin:
        log_update(line)
