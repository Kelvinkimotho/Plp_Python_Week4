def read_and_write_file():
    try:
        # Asking the user for the input file name
        input_filename = input("Enter the filename to read from: ")
        
        # Opening then reading the file
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        # Modifying the content (Converting to uppercase)
        modified_content = [line.upper() for line in content]
        
        # Asking the user for the output file name
        output_filename = input("Enter the filename to write to: ")
        
        # Writing modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Successfully written to {output_filename}")
    
    except FileNotFoundError:
        print("Error: The file you are trying to read does not exist.")
    except IOError:
        print("Error: There was an issue reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# I the call my function
read_and_write_file()
