from PIL import Image
import os


def make_pdf(dir_path, blackwhite_color_mode):
    if blackwhite_color_mode:
        images = [Image.open(dir_path + '/' + f) for f in os.listdir(dir_path)]
    else:
        images = [Image.open(dir_path + '/' + f).convert('L') for f in os.listdir(dir_path)]

    pdf_path = dir_path + "/pdf_file.pdf"
    if len(images) > 1:
        images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
    else:
        images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True)
