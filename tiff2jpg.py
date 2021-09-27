import os
import sys
from PIL import Image

overwrite: bool = False

if len(sys.argv) < 2:
    
    print("\n\n~~~~~~~tiff2jpg.py~~~~~~~\nLooks like you're trying to convert some huge tif files into less huge jpegs!\n\nRequired argument: Root Directory for Conversion\nOptional Argument: -overwrite (Warning! This deletes the original tif file after conversion!)\n\n")
    sys.exit(1)

else:
    
    inputPath = sys.argv[1]
    
    if len(sys.argv) > 2:
        
        if sys.argv[2] == "-overwrite":
            
            overwrite = True
            print("Note: Overwrite is enabled! All original tif files will be deleted after conversion!\n\n")
        
        else:
            
            print("Error! Invalid optional argument!")
            sys.exit(1)

    print("Checking all directories and subdirectories in: " + inputPath + "\n")

    if os.path.exists(inputPath) == False:
        
        print("Input Directory Does Not Exist!")
        sys.exit(2)

    else:
        # Initial search to determine how many files will be converted
        fileCount: int = 0
        
        for root, dirs, files in os.walk(inputPath, topdown = False):
            
            for name in files:
                
                if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
                    
                    fileCount += 1
        
        print("%i tif files found for conversion.\n" %fileCount)

        countCompleted: int = 0

        for root, dirs, files in os.walk(inputPath, topdown = False):
            
            for name in files:
                
                # print(os.path.join(root, name)) # Prints all files checked
                if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
                    
                    print(os.path.join(root, name))
                    
                    if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                        
                        print("A jpeg file already exists for %s\nSkipping..." %name)
                    
                    else:
                        
                        outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
                        tempPath: str = os.path.join(root, name)
                        
                        with Image.open(tempPath) as im:
                            
                            print("Generating jpeg file for %s" %tempPath)
                            
                            try:
                                im.thumbnail(im.size)
                                im.save(outfile, format = "JPEG", quality = 100, icc_profile = im.info.get('icc_profile',''))
                                
                                if overwrite == True:
                                    
                                    try:
                                        os.remove(os.path.join(root, name))
                                    except OSError as e:
                                        print("\nError occurred deleting original file: %s \n" %tempPath)
                            
                            except OSError as e:
                                print("\nError occurred opening the target file: %s\nIt may be corrupt.\nSkipping file...\n" %tempPath)
                    
                    countCompleted += 1
                    print("\n%i of %i completed" %(countCompleted, fileCount))