def file_read_write():
    # Ask user for input file name
    input_filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Create a new output filename
        output_filename = "modified_" + input_filename

        # Write modified content into a new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File processed successfully! Modified content saved as {output_filename}")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Run the function
file_read_write()
