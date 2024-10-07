def find_substring_in_file(file_path, substring):
    matches = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            start_pos = 0
            while True:
                start_pos = line.find(substring, start_pos)
                if start_pos == -1:
                    break 
                matches.append((line_number, start_pos + 1)) 
                start_pos += 1  
    return matches

file_path = 'lab2_4.txt'
substring = 'xam'
results = find_substring_in_file(file_path, substring)

for line_number, position in results:
    print(f"Найдено совпадение в строке {line_number}, позиция {position}")