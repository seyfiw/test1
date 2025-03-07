def is_funny_string(s: str) -> str:
    n = len(s)
    for i in range(1, n):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[n-i]) - ord(s[n-i-1])):
            return "Not Funny"
    return "Funny"
