text = input()
result = ''

cyrillic_chars = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
    'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
    'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'ю', 'я',
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й',
    'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
    'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'ь', 'Ю', 'Я',
]

corresponding_english_chars = [
    'a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y',
    'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
    'f', 'h', 'ts', 'ch', 'sh', 'sht', 'a', 'a', 'yu', 'ya',
    'A', 'B', 'V', 'G', 'D', 'E', 'Zh', 'Z', 'I', 'Y',
    'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U',
    'F', 'H', 'Ts', 'Ch', 'Sh', 'Sht', 'A', 'a', 'Yu', 'Ya',
]

for char in text:
    if char in cyrillic_chars:
        idx = cyrillic_chars.index(char)
        result += corresponding_english_chars[idx]
    else:
        result += char

print(result)





