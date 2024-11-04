#!/usr/bin/python3
'''
UTF-8 Validation
'''


def validUTF8(data):
    # Number of bytes left to check in the current character
    num_bytes = 0

    # Masks to identify the leading byte pattern
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        # Only keep the last 8 bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            if (byte & mask1) == 0:
                # 1-byte character
                continue
            elif (byte & (mask1 >> 1)) == (mask1 >> 1):
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 >> 2):
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 >> 3):
                num_bytes = 3
            else:
                return False
        else:
            # Check that each byte starts with "10"
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
