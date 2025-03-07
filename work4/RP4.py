def caesarCipher(s: str, k: int) -> str:
    result = []
    k = k % 26  # ลด k ให้อยู่ในช่วง 0-25
    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            new_char = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))
        else:
            new_char = char  # ไม่เปลี่ยนอักขระที่ไม่ใช่ตัวอักษร
        result.append(new_char)
    return "".join(result)