# python pdf2tiff.py --ip=C:\Users\BC\Desktop\loan-agreement-template.pdf --od=C:\Users\BC\Desktop\test

import logging
import argparse
import os
import sys
import uuid
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes


logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] %(module)s.%(funcName)s:%(lineno)s: %(message)s')




class ReadArgument:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Convert JPEG images into Tiff')
        parser.add_argument('--ip', action='store', required=True,
            help='provide input PDF file with complete path')
        parser.add_argument('--od', action='store', required=True,
            help='Generated TIFF output directory')
        self.args = parser.parse_args()



def main():
    read_argument = ReadArgument()
    logging.debug("Input PDF file - %s" % read_argument.args.ip)
    logging.debug("Output TIFF Dir - %s" % read_argument.args.od)

    pdf_file_with_path = read_argument.args.ip
    pdf_file_name = os.path.basename(pdf_file_with_path).split(".")[0]
    logging.debug("PDF File Name - %s" % pdf_file_name)

    logging.debug("Start")
    images = convert_from_path(pdf_file_with_path, dpi=200, output_folder=None, first_page=None, last_page=None, fmt='ppm', jpegopt=None, thread_count=1, userpw=None, use_cropbox=False, strict=False, transparent=False, single_file=False, output_file=str(uuid.uuid4()), poppler_path=None, grayscale=False, size=None, paths_only=False)
    logging.debug("middle")
    count = 0
    for image in images:
        image.convert('1')
        image.save(os.path.join(read_argument.args.od, pdf_file_name + str(count) + ".tiff"), dpi=(300, 0))
        count = count + 1
    logging.debug("Finish")

    
if __name__ == '__main__':
    main()