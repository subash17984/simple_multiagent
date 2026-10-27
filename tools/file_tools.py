from pathlib import Path

OUTPUT_DIR=Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def create_file(filename:str,content:str)-> str:
    """
    Create a file inside the output folder."""
    
    filepath=OUTPUT_DIR/filename
    
    with open(filepath,"w", encoding="utf-8") as f:
        f.write(content)
        
    # return f"Created {filepath}"
    return f"{filename} created successfully."



def list_files():
    files = []

    for file in OUTPUT_DIR.iterdir():
        files.append(file.name)

    return files

