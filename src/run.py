import sys

def run():

    args = sys.argv[1:] 
    
    # Here you can parse args to extract -c and -p values
    custom_json = None
    process_all = False
    
    if '-c' in args:
        index = args.index('-c')
        custom_json = args[index + 1] if index + 1 < len(args) else None
    
    if '-p' in args:
        index = args.index('-p')
        process_all = True
    
    # Now you can use custom_json and process_all as needed in your script
    print(f"Custom JSON file: {custom_json}")
    print(f"Process all: {process_all}")

if __name__ == "__main__":
    run()