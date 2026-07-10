import time

from compressor import (
    compress,
    decompress,
    file_exists,
    file_not_empty,
    compression_statistics,
    compression_status,
    get_output_filename,
    get_restored_filename,
    about,
)


def compress_file():
    filename = input("\nEnter text file (.txt): ").strip()

    if not file_exists(filename):
        print("\n❌ Error: File does not exist.")
        return

    if not filename.endswith(".txt"):
        print("\n❌ Error: Only .txt files are supported.")
        return

    if not file_not_empty(filename):
        print("\n❌ Error: File is empty.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        start = time.perf_counter()

        compressed = compress(text)

        output_file = get_output_filename(filename)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(compressed)

        end = time.perf_counter()

        (
            original_size,
            compressed_size,
            saved_bytes,
            ratio,
            reduction,
        ) = compression_statistics(filename, output_file)

        print("\n========== COMPRESSION SUCCESSFUL ==========")
        print(f"Input File        : {filename}")
        print(f"Output File       : {output_file}")
        print(f"Original Size     : {original_size} bytes")
        print(f"Compressed Size   : {compressed_size} bytes")
        print(f"Space Saved       : {saved_bytes} bytes")
        print(f"Compression Ratio : {ratio:.2f}%")
        print(f"Reduction         : {reduction:.2f}%")
        print(f"Status            : {compression_status(reduction)}")
        print(f"Execution Time    : {(end-start):.6f} seconds")

    except Exception as e:
        print("\n❌ Error:", e)


def decompress_file():
    filename = input("\nEnter compressed file (.rle): ").strip()

    if not file_exists(filename):
        print("\n❌ Error: File does not exist.")
        return

    if not filename.endswith(".rle"):
        print("\n❌ Error: Only .rle files are supported.")
        return

    if not file_not_empty(filename):
        print("\n❌ Error: File is empty.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()

        start = time.perf_counter()

        original = decompress(data)

        output_file = get_restored_filename(filename)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(original)

        end = time.perf_counter()

        print("\n========= DECOMPRESSION SUCCESSFUL =========")
        print(f"Input File     : {filename}")
        print(f"Output File    : {output_file}")
        print(f"Execution Time : {(end-start):.6f} seconds")

    except Exception as e:
        print("\n❌ Error:", e)


def menu():

    while True:

        print("\n===================================")
        print("     CUSTOM FILE COMPRESSOR")
        print("===================================")
        print("1. Compress File")
        print("2. Decompress File")
        print("3. About")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            compress_file()

        elif choice == "2":
            decompress_file()

        elif choice == "3":
            print(about())

        elif choice == "4":
            print("\nThank you for using Custom File Compressor!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()