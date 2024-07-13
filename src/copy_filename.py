import os
import csv

def create_sym_file():
    
    
    folder_path = '..\\eod2-main\\src\\eod2_data\\daily\\'

    # Get a list of all files in the folder
    all_files = os.listdir(folder_path)

    # Filter out the .csv files and remove the .csv extension
    csv_files = [os.path.splitext(file)[0] for file in all_files if file.endswith('.csv')]

    # Path to the sym_list.csv file
    output_file = 'sym_list.csv'

    # Write the file names to sym_list.csv
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for file in csv_files:
            writer.writerow([file])

    print(f"Successfully written {len(csv_files)} file names to {output_file}")

def rename_file():
    old_filename = 'nifty 500.csv'
    new_filename = 'nifty_500.csv'
    directory = "..\\eod2-main\\src\\eod2_data\\daily"
    # Create the full path for the old and new file names
    old_file = os.path.join(directory, old_filename)
    new_file = os.path.join(directory, new_filename)

    # Rename the file
    os.rename(old_file, new_file)
if __name__ == '__main__':
    create_sym_file()