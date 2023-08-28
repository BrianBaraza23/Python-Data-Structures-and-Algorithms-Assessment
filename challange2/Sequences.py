def remove_duplicates(sequence):
    result = []
    
    for item in sequence:
        if item not in result:
            result.append(item)
    
    return result

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result) 