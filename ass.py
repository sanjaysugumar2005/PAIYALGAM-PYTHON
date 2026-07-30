def is_unique_chars(s):
    # ASCII has only 128 unique characters
    if len(s) > 128:
        return False

    char_set = [False] * 128

    for ch in s:
        val = ord(ch)  # Get ASCII value

        if char_set[val]:
            return False  # Character already exists

        char_set[val] = True

    return Truei


# Example
print(is_unique_chars("hello"))   # False
print(is_unique_chars("world"))   # True
print(is_unique_chars("Python"))  # True
print(is_unique_chars("apple"))   # False