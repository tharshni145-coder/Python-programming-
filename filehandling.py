def main():
    filename = "student_records.txt"

    # --- 1. WRITE CONCEPT: Collect user input and write to file ---
    print("=== Enter Student Details ===")
    name = input("Enter Student Name: ").strip()

    # Collect marks for 3 subjects
    marks = []
    for i in range(1, 4):
        mark = input(f"Enter mark for Subject {i}: ").strip()
        marks.append(mark)

    email = input("Enter Email ID: ").strip()
    phone = input("Enter Phone Number: ").strip()

    # Write data into the file using 'with' statement
    with open(filename, "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Marks (Sub1, Sub2, Sub3): {', '.join(marks)}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Phone: {phone}\n")

    print(f"\n[Success] Information saved to '{filename}'.\n")

    # --- 2. READ CONCEPT: Read file content and display output ---
    print("=== Reading Student Record from File ===")
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


if __name__ == "__main__":
    main()