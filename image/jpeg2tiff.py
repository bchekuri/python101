# python jpeg2tiff.py --ij=C:\Users\BC\Desktop\jpegsystems-home.jpg --od=C:\Users\BC\Desktop

import logging
import argparse
import os
import sys
from PIL import Image


logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] %(module)s.%(funcName)s:%(lineno)s: %(message)s')




class ReadArgument:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Convert JPEG images into Tiff')
        parser.add_argument('--ij', action='store', required=True,
            help='provide input JPEG file with complete path')
        parser.add_argument('--od', action='store', required=True,
            help='Generated TIFF output directory')
        self.args = parser.parse_args()



def main():
    read_argument = ReadArgument()
    logging.debug("Input JPEG file - %s" % read_argument.args.ij)
    logging.debug("Output TIFF Dir - %s" % read_argument.args.od)

    jpeg_file_with_path = read_argument.args.ij
    jpeg_file_name = os.path.basename(jpeg_file_with_path).split(".")[0]
    logging.debug("JPEG File Name - %s" % jpeg_file_name)

    img = Image.open(read_argument.args.ij)
    img = img.convert('1')
    img.save(os.path.join(read_argument.args.od, jpeg_file_name + ".tiff"))

if __name__ == '__main__':
    main()