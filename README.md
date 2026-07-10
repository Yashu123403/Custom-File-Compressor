CUSTOM FILE COMPRESSOR

## Overview

Custom File Compressor is a lightweight Python application that implements the Run-Length Encoding (RLE) algorithm from scratch. It allows users to compress and decompress text files through an interactive command-line interface while providing compression statistics and file validation.

## Features
- Custom Run-Length Encoding (RLE) implementation
- Compress text files
- Decompress RLE files
- Automatic output file generation
- Compression ratio calculation
- Space saved calculation
- Original and compressed file size comparison
- Execution time measurement
- File validation
- Error handling for invalid or corrupted files
- Interactive command-line interface
- Modular Python code structure

## Project Structure
Custom File Compressor/
│── main.py
│── compressor.py
│── examples
│── .gitignore

## Technologies Used
- Python 3
- Run-Length Encoding (RLE)
- File Handling
- os module
- time module

## Requirements
- Python 3x
- No external libraries are required.

## How to Run
1. Download or clone the repository.
2. Open the project folder in VS Code or any Python IDE.
3. Open the terminal.
4. Run the following command:
python main.py

## Menu
========================
 CUSTOM FILE COMPRESSOR
========================

1. Compress File
2. Decompress File
3. About
4. Exit

## Sample Input

AAAAAAAAAABBBBBCCCCDDDDDEEEEEFFFFGGGG
`
## Sample Compressed Output

A10B5C4D5E5F4G4

## Sample Program Output

========== COMPRESSION SUCCESSFUL ==========

Input File        : sample.txt
Output File       : sample.txt.rle

Original Size     : 30 bytes
Compressed Size   : 8 bytes

Space Saved       : 22 bytes

Compression Ratio : 26.67%

Reduction         : 73.33%

Status            : Excellent Compression

Execution Time    : 0.000214 seconds

## Algorithm

The project uses the Run-Length Encoding (RLE) compression algorithm.
Instead of storing repeated characters individually, RLE stores each character followed by the number of consecutive occurrences.

Example:

Original Data: AAAAABBBCC
Compressed Data: A5B3C2

During decompression, the original text is reconstructed using the stored counts.

## Time Complexity

| Operation | Complexity |
|----------|------------|
| Compression | O(n) |
| Decompression | O(n) |

## Space Complexity

| Operation | Complexity |
|----------|------------|
| Compression | O(n) |
| Decompression | O(n) |

## Limitations

- Supports text files only.
- Run-Length Encoding performs best on data containing repeated characters.
- Files with little repetition may not compress efficiently.

## Future Enhancements

- Graphical User Interface (Tkinter)
- Binary file support
- Folder compression
- Password protection
- Multiple compression algorithms
- Drag-and-drop support
- Compression history log

## Author
YASHU A.B.
