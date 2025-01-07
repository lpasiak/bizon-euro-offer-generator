import shutil
from pathlib import Path

def zip_all_folders(source_dir: Path, output_dir: Path):
    """
    Zips all folders inside the source directory, keeping the folder structure intact,
    and saves them in the output directory.

    :param source_dir: Path to the directory containing the folders to zip.
    :param output_dir: Path to the directory where the ZIP files will be saved.
    """
    try:

        output_dir.mkdir(exist_ok=True)

        # Iterate through all folders in the source directory
        for folder in source_dir.iterdir():
            if folder.is_dir():
                zip_file_path = output_dir / folder.name  # Path for the ZIP file
                shutil.make_archive(zip_file_path, 'zip', root_dir=source_dir, base_dir=folder.name)
                print(f"Zipped: {folder} -> {zip_file_path}.zip")
    except Exception as e:
        print(f"Error zipping folders: {e}")
