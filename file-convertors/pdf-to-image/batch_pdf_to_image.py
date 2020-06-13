'''
Batch PDF to Image Converter
Author: Fraser Love, me@fraser.love
Created: 2020-06-13
Latest Release: v1.0.0, 2020-06-13

Converts multiple pdf's to images and stores them in a logical folder structure under the desired image directory.

Usage:  Update the pdf_dir and img_dir paths to point to the directory that holds the pdf files and the directory 
        that the generated images should be placed under.
'''

from pdf2image import convert_from_path
import os

pdf_dir = 'static/files/'
img_dir = 'static/images/'

pdf_names = [pdf_name.split('.')[0] for pdf_name in os.listdir(pdf_dir) if os.path.isfile(os.path.join(pdf_dir, pdf_name))]

for pdf_name in pdf_names:
    pages = convert_from_path('{}{}.pdf'.format(pdf_dir, pdf_name))

    directory = '{}{}'.format(img_dir, pdf_name)
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, page in enumerate(pages):
        page.save('{}{}/{}-{}.jpg'.format(img_dir, pdf_name, pdf_name, i), 'JPEG')