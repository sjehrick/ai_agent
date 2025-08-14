from google.genai import types


def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    print(f" - Calling function: {function_call_part.name}")

    function_dict = {
        "get_files_info": get_files_info(
            **{"working_directory": "./calculator", "directory": "."}
        ),
        "get_file_content": get_file_content(
            **{"working_directory": "./calculator", "file_path": "x"}
        ),
        "run_python": run_python_file(
            **{"working_directory": "./calculator", "file_path": "x", "args": []}
        ),
        "write_file": write_file(
            **{"working_directory": "./calculator", "file_path": "x", "content": "x"}
        ),
    }
