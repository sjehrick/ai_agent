import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_path_full_path = os.path.abspath(full_path)
    abs_path_working = os.path.abspath(working_directory)
    try:
        if not abs_path_full_path.startswith(abs_path_working):
            return f'   Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'   Error: "{directory}" is not a directory'
        #if directory == ".":
        output = ""
        #else:
        #    output = f"Result for '{directory}' directory:"
        
        for item in os.listdir(full_path):
            output += f'\n- {item}: file_size={os.path.getsize(os.path.join(full_path, item))} bytes, is_dir={os.path.isdir(os.path.join(full_path, item))}'
        return output
    
    except Exception as e:
        return f'Error: An unexpected error occurred, {e} \nNeed you to try again!'
