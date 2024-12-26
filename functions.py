import os

def generate_css_file():
    # Define paths
    source_file_path = os.path.join('data', 'style.css')
    directory = os.path.join('products', 'css')
    file_path = os.path.join(directory, 'style.css')

    try:
        # Ensure the source file exists
        if not os.path.exists(source_file_path):
            print(f"Source file does not exist: {source_file_path}")
            return

        # Create destination directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Read the source file
        with open(source_file_path, 'r') as r_file:
            contents = r_file.read()

        # Write to the destination file
        with open(file_path, 'w') as file:
            file.write(contents)

        print(f"CSS file created at: {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
