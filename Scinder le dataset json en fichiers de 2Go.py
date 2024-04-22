import os

input_path = r'C:\Users\Kenzi\Documents\MIASHS\L3 MIAGE\Nanterre\Semestre 6\GRAPHES ET OPEN DATA\projet\Dataset\Dataset publication scientifique JSON.json'
base_output_path = r'C:\Users\Kenzi\Documents\MIASHS\L3 MIAGE\Nanterre\Semestre 6\GRAPHES ET OPEN DATA\projet\Dataset\Split_'

# Open the large file
with open(input_path, 'r', encoding='utf-8') as big_file:
    file_count = 1
    current_file = open(f'{base_output_path}{file_count}.json', 'w', encoding='utf-8')
    current_size = 0
    for line in big_file:
        current_file.write(line)
        current_size += len(line.encode('utf-8'))
        # Check if current file size is approximately 2GB (2 * 10^9 bytes)
        if current_size >= 2 * 10**9:
            current_file.close()
            file_count += 1
            current_file = open(f'{base_output_path}{file_count}.json', 'w', encoding='utf-8')
            current_size = 0

    current_file.close()

print("Splitting completed.")
