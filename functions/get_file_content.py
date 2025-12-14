import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_abs = os.path.join(working_dir_abs, file_path)
        
        if os.path.commonpath([working_dir_abs, file_abs]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(file_abs, "r") as file:
            file_content_str = file.read()
            if len(file_content_str) > MAX_CHARS:
                file_content_str = file_content_str[:MAX_CHARS+1]
                file_content_str += f'File "{file_path}" truncated at 10000 characters'
        return file_content_str
        
    except Exception as e:
        return f"Error: {str(e)}"