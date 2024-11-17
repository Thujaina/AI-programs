# Simple File Handling Program
def write_to_file():
    file_name = input("Enter the file name: ")
    content = input("Enter the content to write: ")
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"Content written to {file_name} successfully!")

def read_from_file():
    file_name = input("Enter the file name: ")
    try:
        with open(file_name, 'r') as file:
            print("\nFile Content:")
            print(file.read())
    except FileNotFoundError:
        print("File not found!")

if __name__ == "__main__":
    print("1. Write to File")
    print("2. Read from File")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        write_to_file()
    elif choice == '2':
        read_from_file()
    else:
        print("Invalid choice!")