import os


def compress(text):
    """
    Compress text using Run-Length Encoding (RLE).
    Example:
    AAAABBBCC -> A4B3C2
    """

    if not text:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed.append(text[i - 1] + str(count))
            count = 1

    compressed.append(text[-1] + str(count))

    return "".join(compressed)


def decompress(data):
    """
    Decompress RLE encoded text.
    Example:
    A4B3C2 -> AAAABBBCC
    """

    if not data:
        raise ValueError("Compressed file is empty.")

    output = []
    i = 0

    while i < len(data):

        char = data[i]
        i += 1

        count = ""

        while i < len(data) and data[i].isdigit():
            count += data[i]
            i += 1

        if count == "":
            raise ValueError("Invalid RLE data.")

        output.append(char * int(count))

    return "".join(output)


def file_exists(filename):
    """Check if file exists."""
    return os.path.isfile(filename)


def file_not_empty(filename):
    """Check if file is not empty."""
    return os.path.getsize(filename) > 0


def file_size(filename):
    """Return file size in bytes."""
    return os.path.getsize(filename)


def compression_statistics(original_file, compressed_file):
    """
    Returns:
    original_size,
    compressed_size,
    saved_bytes,
    compression_ratio,
    reduction_percentage
    """

    original_size = file_size(original_file)
    compressed_size = file_size(compressed_file)

    saved_bytes = original_size - compressed_size

    if original_size == 0:
        compression_ratio = 0
        reduction = 0
    else:
        compression_ratio = (compressed_size / original_size) * 100
        reduction = 100 - compression_ratio

    return (
        original_size,
        compressed_size,
        saved_bytes,
        compression_ratio,
        reduction,
    )


def compression_status(reduction):
    """
    Return a message based on compression efficiency.
    """

    if reduction >= 70:
        return "Excellent Compression"

    elif reduction >= 40:
        return "Good Compression"

    elif reduction >= 10:
        return "Average Compression"

    elif reduction >= 0:
        return "Poor Compression"

    else:
        return "Compressed file is larger than original"


def get_output_filename(filename):
    """
    sample.txt
    ->
    sample.txt.rle
    """

    return filename + ".rle"


def get_restored_filename(filename):
    """
    sample.txt.rle
    ->
    sample_restored.txt
    """

    if filename.endswith(".rle"):
        filename = filename[:-4]

    name, extension = os.path.splitext(filename)

    if extension == "":
        extension = ".txt"

    return f"{name}_restored{extension}"


def about():
    """
    Project information.
    """

    return """
==========================================
        CUSTOM FILE COMPRESSOR
==========================================

Algorithm : Run-Length Encoding (RLE)
--------------
Language : Python
--------------
Features :
--------------
✓ Compress Text Files
✓ Decompress RLE Files
✓ Compression Statistics
✓ Exception Handling
✓ Automatic Output File Generation
✓ File Validation
✓ Interactive Command-Line Interface(CLI)
--------------

Time Complexity
--------------
Compression   : O(n)
Decompression : O(n)
---------------

Space Complexity
---------------
Compression   : O(n)
Decompression : O(n)


==========================================
"""