def counting_sort(numbers: list[int]) -> list[int]:
    if not numbers:
        return []

    # Logic: Calculate range to handle offsets (e.g., negative numbers)
    min_val, max_val = min(numbers), max(numbers)
    range_width = max_val - min_val + 1
    
    # Frequency Map (The 'Distribution' storage)
    counts = [0] * range_width
    
    for x in numbers:
        counts[x - min_val] += 1
        
    # Reconstruct: Professional 'In-place' overwrite
    write_idx = 0
    for val_offset, freq in enumerate(counts):
        actual_val = val_offset + min_val
        for _ in range(freq):
            numbers[write_idx] = actual_val
            write_idx += 1
    
    return numbers

x = counting_sort([1, 2,,5, 3, 4])
print(x)
