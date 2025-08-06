import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_dir):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            ["python", target_dir, args],
            timeout=30,
            capture_output=True,
            check=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        return (
            f"Error: executing Python file: {e} \nCommand failed with exit code {e.returncode}, \nStderr: {e.stderr}"
        )
    
    output = f"STDOUT: {result.stdout} \nSTDERR: {result.stderr}"

    if not result:
        return (
            "No output produced"
        )

    if result.returncode != 0:
        return (
            output + f"\nProcess exited with code {result.returncode}"
        )

    return output
