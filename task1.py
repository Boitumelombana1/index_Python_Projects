with open("records.txt", "w") as file:
    print("Enter at least 5 records")

    for i in range(1, 6):
        record = input(f"Enter your record {i}: ")
        file.write(record + "\n")

print("\nRecords saved successfully!")

print("\nContents of records.txt")
print("_" * 20)

with open("records.txt", "r") as file:
    contents = file.read()
    print(contents)