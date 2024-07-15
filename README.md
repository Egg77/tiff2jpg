# tiff2jpg
 Batch file converter - TIFF to JPEG

Requirements: 

- Python 3 or higher (only tested with Python 3.9.0 64-bit)
- Pillow (can be installed with pip install Pillow)

This is a simple, specialized tool designed to look through a directory (and any sub-directories), find every TIFF file, and convert it to a much smaller JPEG. 

This program can be run in the command line and takes up to two arguments:

1) The top-level directory in which to search
2) (Optional) "-overwrite". If this is included, original TIFF files will be deleted after conversion, leaving only the output JPEG behind.

## My use case 
As a former real estate photographer, part of my editing workflow required the generation of hundreds of large multi-gigabyte TIFF files for editing in Adobe Photoshop. Since these files were an intermediate format (not the original raw file, nor the final file delivered to the client), I did not want to waste precious HDD space storing them indefinitely. As such, every few weeks, I ran this program on my top-level directory to convert all tiff files to jpegs, saving hundreds of gigabytes in HDD space at a time. 
