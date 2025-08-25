import csv
def analyze_csv_file(file_path):
    """
    Read a CSV file and return statistics about the data.
    Args:
        file_path (str): Path to the CSV file to analyze
    Returns:
        dict: Dictionary containing total_rows, empty_rows, and total_words
        or None if file cannot be read
    """
    try:
        total_rows = 0
        empty_rows = 0
        total_words = 0
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                total_rows += 1
                # Check if row is empty (all cells are empty or whitespace)
                if not row or all(cell.strip() == '' for cell in row):
                    empty_rows += 1                
                # Count words in each cell
                for cell in row:
                    if cell.strip():  # Only count non-empty cells
                        words = cell.strip().split()
                        total_words += len(words)
        return {
            'total_rows': total_rows,
            'empty_rows': empty_rows,
            'total_words': total_words
        }
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read file '{file_path}'.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
# Test the function
if __name__ == "__main__":
    # Example usage
    file_path = input("Enter the path to your CSV file: ")
    result = analyze_csv_file(file_path)
    if result:
        print("\nCSV File Analysis Results:")
        print("=" * 30)
        print(f"Total rows: {result['total_rows']}")
        print(f"Empty rows: {result['empty_rows']}")
        print(f"Total words: {result['total_words']}")
    else:
        print("Could not analyze the file.")
