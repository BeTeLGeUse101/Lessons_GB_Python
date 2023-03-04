""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
Входные и выходные данные хранятся в отдельных текстовых файлах. """

def compress(data: str) -> str:
    compressed_data = ""
    count = 1
    prev_char = data[0]
    
    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed_data += str(count) + prev_char
            count = 1
            prev_char = char
    
    compressed_data += str(count) + prev_char
    return compressed_data


def decompress(data: str) -> str:
    decompressed_data = ""
    count = ""
    
    for char in data:
        if char.isdigit():
            count += char
        else:
            decompressed_data += char * int(count)
            count = ""
    
    return decompressed_data

original_data = "AAABBBCCCCDDDEEE"
compressed_data = compress(original_data)
decompressed_data = decompress(compressed_data)

print("Оригинальные данные:", original_data)
print("Сжатые данные:", compressed_data)
print("Восстановленные данные:", decompressed_data)