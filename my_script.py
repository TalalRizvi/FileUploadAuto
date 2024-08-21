import os

def main():
    output_path = os.path.join(os.getcwd(), "output.txt")
    with open(output_path, "w") as file:
        file.write("Hello from my_script.py!\n")
        file.write("This is a sample output file.")
    print(f"Output written to {output_path}")

if __name__ == "__main__":
    main()
