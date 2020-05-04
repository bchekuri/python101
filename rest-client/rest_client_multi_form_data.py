import logging
import requests
from requests_toolbelt import MultipartEncoder
import argparse
import base64
import os
import json


logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] %(module)s.%(funcName)s:%(lineno)s: %(message)s')

URL = "http://localhost:8080/documents/v1/convert"

class ReadArgument:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Documents Converter Client')
        parser.add_argument('--inputfile', action='store', required=True,
            help='provide input file with complete path')
        self.args = parser.parse_args()

def main():
    read_argument = ReadArgument()
    logging.debug("Input file - %s" % read_argument.args.inputfile)
    file_name = "sample.pdf"
    with open(read_argument.args.inputfile, "rb") as pdf_file:
        encoded_content = base64.b64encode(pdf_file.read()).decode('utf-8')
    data = {
        'merge' : True,
        'converts' :[{
            'convertTo' : 'tiff',
            'file' : {
                'name' : file_name,
                'type' : 'pdf',
                'content' : encoded_content
            }
        }]
    }
    headers = {
        'Client-Correlation-Id': 'multi-test-base64',
        'Content-Type': 'application/json'
    }
    res = requests.post(URL, data=data, headers=headers)    
    print(res.json())



if __name__ == '__main__':
    main()
