'''
PDF to Image Converter
Author: Fraser Love, me@fraser.love
Created: 2020-06-13
Latest Release: v1.0.1, 2020-06-21
Python: v3.6.9
Dependancies: pdf2image

Converts multiple pdf's to images (JPEG format) and stores them in a logical folder structure under the desired image directory.

Usage:  Update the pdf_dir and img_dir paths to point to the directory that holds the pdf files and the directory that the 
        generated images should be placed under.
'''

from pdf2image import convert_from_path
import os

pdf_dir = 'pdfs/' # Include trailing forward slash
img_dir = 'images/'
first_page_only = False # Only convert the first page of the pdf to an image

pdf_names = [pdf_name.split('.')[0] for pdf_name in os.listdir(pdf_dir) if os.path.isfile(os.path.join(pdf_dir, pdf_name))]

for pdf_name in pdf_names:
    pages = convert_from_path('{}{}.pdf'.format(pdf_dir, pdf_name))

    if first_page_only:
        directory = '{}{}'.format(img_dir)
        if not os.path.exists(directory):
            os.makedirs(directory)
        pages[0].save('{}/{}.jpg'.format(img_dir, pdf_name), 'JPEG')

    else:
        directory = '{}{}'.format(img_dir, pdf_name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        for i, page in enumerate(pages):
            page.save('{}{}/{}-{}.jpg'.format(img_dir, pdf_name, pdf_name, i), 'JPEG')