import os

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    abs_file = os.path.join(working_dir_abs, file_path);
    
    if os.path.commonpath([abs_file, working_dir_abs]) != working_dir_abs:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:    
        with open(abs_file, "w") as file:
            file.write(content)        
    except Exception as e:
        return f"Error: {str(e)}"
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
if __name__ == "__main__":
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))