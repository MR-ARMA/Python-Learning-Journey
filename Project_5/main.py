def rangoli(size):
    import string
    
    # Create a list of all alphabet letters.
    alphabet = string.ascii_lowercase
    
    # Create the rangoli lines.
    lines = []
    for i in range(size):
        # Create a list of characters to include in the current line.
        chars = [alphabet[j] for j in range(size - 1, i, -1)]  # Right half of the line.
        chars.extend([alphabet[j] for j in range(i + 1, size)])  # Left half of the line.
        
        # Join the characters with hyphens and center-align the line.
        line = '-'.join(chars).center(size * 4 - 3, '-')
        lines.append(line)
    
    # Join all the lines with newline characters.
    return '\n'.join(lines + lines[:-1][::-1])  # Combine top and bottom halves of the rangoli.

# Input size
size = int(input())
# Print the rangoli
print(rangoli(size))

    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)