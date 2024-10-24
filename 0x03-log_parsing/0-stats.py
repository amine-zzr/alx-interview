#!/usr/bin/python3

import sys
import re
import signal

# Dictionary to hold the count of each status code
status_code_count = {200: 0,
                     301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Total file size
total_size = 0

# Line counter for printing stats every 10 lines
line_count = 0


def print_stats():
    global total_size, status_code_count
    print(f"File size: {total_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


# Register signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line_count += 1
    # Regular expression to match the input format
    match = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))
        if status_code in status_code_count:
            status_code_count[status_code] += 1
            total_size += file_size
    # Print stats every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print final stats if not interrupted
print_stats()