#!/usr/bin/python3
import sys

""" Initialize variables to store total file size and status code counts """
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    # Read lines from stdin
    for i, line in enumerate(sys.stdin, start=1):
        try:
            # Split the line into parts and extract size and status code
            parts = line.split()
            size = int(parts[-1])
            status_code = int(parts[-2])
        except (ValueError, IndexError):
            # Skip lines with incorrect format
            continue

        # Update total file size and status code counts
        total_size += size
        status_counts[status_code] += 1

        # Print statistics every 10 lines
        if i % 10 == 0:
            print(f"File size: {total_size}")
            for code, count in sorted(status_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    # Handle keyboard interruption (Ctrl+C)
    pass

finally:
    # Print final statistics after all lines are processed or interrupted
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
