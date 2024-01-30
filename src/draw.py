"""Module to provide function to draw text in certificate"""

from io import BytesIO
from PIL import ImageFont, Image

IMAGE_PATH = "./source_image/certificate_background.jpg"
PAGE_X_SIZE = 730
NAME_FONT_SIZE = 55
TITLE_FONT_SIZE = 65
NORMAL_FONT_SIZE = 18
BOLD_FONT_PATH = "./fonts/Weather-Sunday.otf"
REGULAR_FONT_PATH = "./fonts/DejaVuSans.ttf"
TITLE_FONT_PATH = "./fonts/vogue.ttf"
COLOR = 'black'
SEAL_PATH = './source_image/genuine_seal.png'

bold_font_file = open(BOLD_FONT_PATH, "rb")
reg_font_file = open(REGULAR_FONT_PATH, "rb")
title_font_file = open(TITLE_FONT_PATH, "rb")
bold_bytes_font = BytesIO(bold_font_file.read())
reg_bytes_font = BytesIO(reg_font_file.read())
title_bytes_font = BytesIO(title_font_file.read())
name_font = ImageFont.truetype(bold_bytes_font, NAME_FONT_SIZE)
title_font = ImageFont.truetype(title_bytes_font, TITLE_FONT_SIZE)
normal_font = ImageFont.truetype(reg_bytes_font, NORMAL_FONT_SIZE)


def get_center_point_x(text, font, drawer):
    """get the horizontal center of the screen"""
    _, _, w, _ = drawer.textbbox((0, 0), text, font)
    return (PAGE_X_SIZE - w)/2


def draw_name(drawer, name):
    """draw certificate name"""
    centralized_coordinates = (
        get_center_point_x(name, name_font, drawer), 130)
    drawer.text(centralized_coordinates, name, fill=COLOR, font=name_font)


def draw_cpf(drawer, cpf):
    """draw certificate document"""
    text = f'CPF: {cpf}'
    centralized_coordinates = (get_center_point_x(
        str(text), normal_font, drawer), 200)
    drawer.text(centralized_coordinates, str(
        text), fill=COLOR, font=normal_font)


def draw_curse_date(drawer, course_date):
    """draw certificate date"""
    drawer.text((320, 470), course_date.strftime(
        "%d/%m/%Y"), fill=COLOR, font=normal_font)


def draw_title(drawer):
    """draw certificate title"""
    certificate_title = "C E R T I F I C A D O"
    center_x = get_center_point_x(certificate_title, title_font, drawer)
    drawer.text(
        (center_x, 45),
        certificate_title,
        fill=COLOR,
        font=title_font
    )


def draw_first_line(drawer):
    """draw certificate first line"""
    text = "Este certificado atesta que"
    center_x = get_center_point_x(text, normal_font, drawer)
    drawer.text(
        (center_x, 120),
        text,
        fill=COLOR,
        font=normal_font
    )


def draw_text_block(drawer, parsed_data):
    """draw certificate text block"""
    phrase1 = f'concluiu com êxito o curso de {parsed_data["course_name"]} oferecido '
    phrase2 = 'pela instituição Kratos Cursos SA, com início na data de  '
    phrase3 = f'{parsed_data["course_date"].strftime("%d/%m/%Y")}. Durante sua participação no curso, demonstrou'
    phrase4 = 'um notável comprometimento e dedicação,destacando-se pelo'
    phrase5 = 'seu empenho notável em todas as atividades propostas.'
    get_center = lambda text:get_center_point_x(text, normal_font, drawer)

    drawer.text(
        (get_center(phrase1), 240),
        phrase1,
        fill=COLOR,
        font=normal_font
    )
    drawer.text(
        (get_center(phrase2), 260),
        phrase2,
        fill=COLOR,
        font=normal_font
    )
    drawer.text(
        (get_center(phrase3), 280),
        phrase3,
        fill=COLOR,
        font=normal_font
    )
    drawer.text(
        (get_center(phrase4), 300),
        phrase4,
        fill=COLOR,
        font=normal_font
    )
    drawer.text(
        (get_center(phrase5), 320),
        phrase5,
        fill=COLOR,
        font=normal_font
    )


def draw_signatures(drawer):
    """draw certificate signature spaces"""
    line = "________________________"
    left_text = "Diretor"
    right_text = 'Coordenador'

    get_center_left = lambda text: get_center_point_x(text, normal_font, drawer) / 2
    get_center_right = lambda text: get_center_point_x(text, normal_font, drawer) * 1.5

    drawer.text(
        (get_center_left(line), 380),
        line,
        fill=COLOR,
        font=normal_font
    )
    drawer.text(
        (get_center_left(left_text) + 30, 400),
        left_text,
        fill=COLOR,
        font=normal_font
    )
    drawer.text(
        (get_center_right(line), 380),
        line,
        fill=COLOR,
        font=normal_font
    )
    drawer.text(
        (get_center_right(right_text) - 25, 400),
        right_text,
        fill=COLOR,
        font=normal_font
    )


def draw_seal(image):
    """draw certificate seal"""
    seal_raw = Image.open(SEAL_PATH)
    seal = seal_raw.resize((130, 100))
    image.paste(seal, (600, 400), seal)


def draw_certificate(drawer, data, image):
    """draw certificate routine"""
    draw_seal(image)
    draw_title(drawer)
    draw_first_line(drawer)
    draw_name(drawer, data['name'])
    draw_cpf(drawer, data['cpf'])
    draw_text_block(drawer, data)
    draw_signatures(drawer)
