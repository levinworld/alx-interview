def validUTF8(data):
    # Helper function to check if a byte is a valid continuation byte
    def is_continuation(byte):
        return 128 <= byte <= 191

    # Iterate through each byte in the data
    i = 0
    while i < len(data):
        # Determine the number of bytes for the current character
        num_bytes = 0
        mask = 128  # 0b10000000
        while data[i] & mask:
            num_bytes += 1
            mask >>= 1

        # Check if the number of bytes is within the valid range (1 to 4)
        if num_bytes < 1 or num_bytes > 4:
            return False

        # Check if the following bytes are valid continuation bytes
        for j in range(1, num_bytes):
            i += 1
            if i >= len(data) or not is_continuation(data[i]):
                return False

        # Move to the next character
        i += 1

    return True

# Example usage
data_set1 = [197, 130, 1]  # Valid UTF-8 encoding (11000101: 10xxxxxx, 10000010: 10xxxxxx, 00000001: 0xxxxxxx)
data_set2 = [235, 140, 4]  # Invalid UTF-8 encoding (11101011: 10xxxxxx, 10001100: 10xxxxxx, 00000100: 0xxxxxxx)

print(validUTF8(data_set1))  # Output: True
print(validUTF8(data_set2))  # Output: False

