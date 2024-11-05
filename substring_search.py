def find_pattern_occurrences(text, pattern):
    positions = []
    pos = text.find(pattern)
    while pos != -1:
        positions.append(pos)
        pos = text.find(pattern, pos + 1)
    return positions

text = "abracadabra"
pattern = "abra"
positions = find_pattern_occurrences(text, pattern)
print("Pattern found at positions:", positions)
