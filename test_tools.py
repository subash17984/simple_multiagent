from tools.file_tools import create_file, list_files

result = create_file(
    "hello.txt",
    "Hello from my first AutoGen tool!"
)

print(result)
print(list_files())