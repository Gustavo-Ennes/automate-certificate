"""Module to automate certificate creation based on a spreadsheet"""

import openpyxl
from PIL import Image, ImageDraw

from draw import draw_certificate

WORKBOOK_PATH = './table/certificate.xlsx'
SHEET_NAME = 'students'
IMAGE_PATH = "./source_image/certificate_background.jpg"

workbook = openpyxl.load_workbook(WORKBOOK_PATH)
data = workbook[SHEET_NAME]


def parse_data(certificate_data):
    """Method to parse data to certificate"""
    return {
        'name': certificate_data[0].value,
        'cpf': certificate_data[1].value,
        'course_name': certificate_data[2].value,
        'course_date': certificate_data[3].value
    }


for index, student in enumerate(data.iter_rows(min_row=2)):
    parsed_data = parse_data(student)
    image = Image.open(IMAGE_PATH)
    drawer = ImageDraw.Draw(image)

    draw_certificate(drawer, parsed_data, image)

    image.save(f'./certificates/{parsed_data["name"]}.png', 'PNG')
