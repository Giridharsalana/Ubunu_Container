'''#####################################################################'''
 #               Program        :- Image to Gds Converter                 #
 #               Langauge       :- Python -3.8.5                          #
 #               Author         :- Giridhar Salana                        #
 #               Mail           :- Giridharsalana@gmail.com               #
 #               Version        :- 1.0                                    #
'''#####################################################################'''

# Importing Modules 

import sys
import cv2
import numpy as np
import gdspy


def main(fileName, sizeOfTheCell, layerNum): 
    print(r"""
  ___                                      ____         ____      _       
 |_ _| _ __ ___    __ _   __ _   ___      |___ \       / ___|  __| | ___  
  | | | '_ ` _ \  / _` | / _` | / _ \       __) |     | |  _  / _` |/ __| 
  | | | | | | | || (_| || (_| ||  __/      / __/      | |_| || (_| |\__ \ 
 |___||_| |_| |_| \__,_| \__, | \___|     |_____|      \____| \__,_||___/ 
                         |___/                                            
""")
    
    # Read an image file
    img = cv2.imread(fileName)

    width = img.shape[1]
    height = img.shape[0]
    print("Image width:{0}".format(width))
    print("Image height:{0}".format(height))

    # Convert an image to grayscale one
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # cv2.imwrite("image_gray.bmp", gray)

    ret, binaryImage = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    # ret, binaryImage_1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    # cv2.imwrite("image_mid.bmp", binaryImage_1)

    # Fill orthological corner
    for x in range(width - 1):
        for y in range(height - 1):
            if binaryImage.item(y, x) == 0 and binaryImage.item(y + 1, x) == 255 \
                    and binaryImage.item(y, x + 1) == 255 and binaryImage.item(y + 1, x + 1) == 0:
                binaryImage.itemset((y + 1, x), 0)
            elif binaryImage.item(y, x) == 255 and binaryImage.item(y + 1, x) == 0 \
                    and binaryImage.item(y, x + 1) == 0 and binaryImage.item(y + 1, x + 1) == 255:
                binaryImage.itemset((y + 1, x + 1), 0)


    # Debugging binary threshold code
    """ 
        for x in range(int(width - width/2)):
            for y in range(height -250):
                binaryImage.itemset((y, x), 0)

        cv2.imwrite("image_exp.bmp", binaryImage)
    """

    # Image processing

    cv2.imwrite("image.bmp", binaryImage)

    gen_layer = {"layer": int(layerNum), "datatype": 250}

    print(gen_layer)

    # gds generation
    # library initialize
    lib = gdspy.GdsLibrary('My_Logo') 
    
    # unit cell view initialize 
    Unit_Cell = lib.new_cell('Unit_Cell')
    # shape generation
    square = gdspy.Rectangle((0.0, 0.0), (1.0, 1.0), **gen_layer)
    # shape adding into cellview
    Unit_Cell.add(square)

    # scaled grid for unit cell
    Grid_Cell = lib.new_cell('Grid_Cell')
    for x in range(width):
        for y in range(height):
            if binaryImage.item(y, x) == 255:      # inverted tweak
                # print("({0}, {1}) is black".format(x, y))
                instance = gdspy.CellReference(Unit_Cell, (x, height - y -1))
                Grid_Cell.add(instance)

    # Logo cell  gds creation

    Scaled_Grid_Cell = gdspy.CellReference(Grid_Cell, origin=(0, 0), magnification=(float)(sizeOfTheCell))

    Logo_Cell = lib.new_cell('Logo_Cell')

    Logo_Cell.add(Scaled_Grid_Cell)

    lib.write_gds('Logo.gds')

    #gdspy.LayoutViewer()


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 4:
        fileName = args[1]
        sizeOfTheCell = args[2]
        layerNum = args[3]
        main(fileName, sizeOfTheCell, layerNum)
    else:
        print(
            "usage: python picToGDS.py <fileName> <sizeOfTheCell[um]> <layerNum>")
        quit()