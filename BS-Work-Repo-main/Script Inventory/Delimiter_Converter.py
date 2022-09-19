'''
Convert TXT (Tab-delimited-values file) to CSV or CSV to TXT, etc.
'''

import os, csv, sys

OUTPUT_DIR = r"Delimiter Converted"

__THIS_SCRIPT = os.path.basename(sys.argv[0])

def print_usage():
    print(f"""Usage:
py {__THIS_SCRIPT} <Input files paths>

This script converts the delimiters of input files (character delimited) and outputs them to the "{OUTPUT_DIR}" directory (generated if doesn't exist).
""")


def convert_delimiters(input_file, output_path, to_delim):
    from_delim = None
    input_file_dialect = None

    print(f"\n[{input_file}]")
    
    try:
        input_file_dialect = get_dialect(input_file) # Gets delimiter as well
        print("Value separator detected:", repr(input_file_dialect.delimiter))
    except csv.Error as err:
        print(f"Error: {err}")
       
        if "Could not determine delimiter" in repr(err):
            from_delim = input("Please enter the input file's delimiter: ")
    
    with open(input_file) as infh:
        with open(output_path, 'w', newline='') as outfh:
            
            if from_delim != None:
                csvr = csv.DictReader(infh, delimiter=from_delim)
            else:
                csvr = csv.DictReader(infh, dialect=input_file_dialect)
                
            csvw = csv.DictWriter(outfh, fieldnames=csvr.fieldnames, delimiter=to_delim)
            
            csvw.writeheader()
            for row in csvr:
                csvw.writerow(row)


def get_dialect(csvpath):
    dialect = None
    with open(csvpath, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(2048))
    return dialect


def main():
    print(__THIS_SCRIPT.upper())
    print("-" * len(__THIS_SCRIPT))

    
    if len(sys.argv) == 1:
        print_usage()
        sys.exit(0)
    
    # Retrieve input files from commandline
    input_files = sys.argv[1:]
    
    to_delim = None
        
    if to_delim == None:
        to_delim = input("Enter the new delimiter: ")
   
    output_ext = None
    
    if to_delim == '\t':
        output_ext = '.txt'
    elif to_delim == ',':
        output_ext = '.csv'
    else:
        print('\nOutput file delimiter is not a comma or tab character.')
        output_ext = '.' + input("Please enter the output file\'s new file extension (excluding '.'): ")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"\nConverting to {output_ext}...")
    
    for input_file in input_files:
       
        output_file = os.path.splitext(os.path.basename(input_file))[0] + output_ext
        output_path = os.path.join(OUTPUT_DIR, output_file)
        
        convert_delimiters(input_file, output_path, to_delim)
        print(f"Converted \"{input_file}\" to \"{output_path}\"")

    print("\nDone")


if __name__ == '__main__':
    main()
