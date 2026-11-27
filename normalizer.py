def normalize(lines):
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            result.append(stripped)
    return result
