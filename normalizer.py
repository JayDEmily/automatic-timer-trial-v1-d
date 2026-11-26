def normalize(lines):
    return [trimmed for line in lines if (trimmed := line.strip())]
