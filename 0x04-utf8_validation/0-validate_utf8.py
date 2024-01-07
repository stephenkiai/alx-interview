#!/usr/bin/python3
'''UTF-8 Validation'''


def validUTF8(data):
    '''Validate UTF-8 encoding'''

    remaining_bytes = 0

    for byte in data:
        if remaining_bytes == 0:
            """
            Determine number of remaining bytes based on starting byte
            """
            if byte < 128:
                remaining_bytes = 0
            elif byte < 224:
                remaining_bytes = 1
            elif byte < 240:
                remaining_bytes = 2
            elif byte < 248:
                remaining_bytes = 3
            else:
                # Invalid starting byte
                return False
        else:
            # Check if current byte is a valid continuation byte
            if not 128 <= byte < 192:
                return False
            remaining_bytes -= 1

    # All characters are valid if no remaining bytes are left
    return remaining_bytes == 0
