import os

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory)
    if directory is not in working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    for item in os.listdir(directory):
        return f'- {item}: file_size={os.path.getsize(item)} bytes, is_dir={os.path.isdir(item)}'
