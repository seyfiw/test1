from itertools import combinations

def alternate(s: str) -> int:
    unique_chars = set(s)
    max_length = 0
    
    for char1, char2 in combinations(unique_chars, 2):
        filtered = [char for char in s if char == char1 or char == char2]
        
        # ตรวจสอบว่าตัวอักษรสลับกันจริง ๆ
        if all(filtered[i] != filtered[i + 1] for i in range(len(filtered) - 1)) and len(filtered) > 1:
            max_length = max(max_length, len(filtered))
    
    return max_length