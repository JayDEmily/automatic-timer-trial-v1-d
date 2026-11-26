def normalize(lines):
    return [stripped for line in lines if (stripped := line.strip())]
