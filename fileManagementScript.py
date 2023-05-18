import os
import shutil

def create_directory(path):
    """Create a new directory."""
    try:
        os.mkdir(path)
        print(f"Directory created: {path}")
    except FileExistsError:
        print(f"Directory already exists: {path}")

def delete_directory(path):
    """Delete an existing directory."""
    try:
        shutil.rmtree(path)
        print(f"Directory deleted: {path}")
    except FileNotFoundError:
        print(f"Directory not found: {path}")

def copy_file(source, destination):
    """Copy a file from the source path to the destination path."""
    try:
        shutil.copy2(source, destination)
        print(f"File copied: {source} -> {destination}")
    except FileNotFoundError:
        print(f"File not found: {source}")

def move_file(source, destination):
    """Move a file from the source path to the destination path."""
    try:
        shutil.move(source, destination)
        print(f"File moved: {source} -> {destination}")
    except FileNotFoundError:
        print(f"File not found: {source}")

def list_files(directory):
    """List all files and directories within a given directory."""
    try:
        contents = os.listdir(directory)
        print(f"Contents of directory: {directory}")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Directory not found: {directory}")

# Example usage
create_directory("example_dir")
delete_directory("example_dir")
copy_file("source.txt", "destination.txt")
move_file("source.txt", "destination.txt")
list_files(".")
