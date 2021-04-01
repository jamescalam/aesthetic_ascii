from PIL import Image, ImageDraw, ImageFont
import random
from importlib import resources
import io

ASCII = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'.'
ASCII_DARK = '.\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

IMAGES = [
    'wallpaperuse.com-outrun-wallpaper-76590.png',
    'wallpaperuse.com-synthwave-wallpaper-1003075.jpg',
    'wallpaperuse.com-wallpapers-retro-803078.jpg',
    'wallpaperuse.com-retro-wallpaper-hd-999925.png',
    '31-synthwave-sun-waves-electronic-sky.jpg',
    'city-5848267_1920.jpg'
]

def get_image():
    # pick an image at random
    n = random.randint(0, len(IMAGES)-1)
    # open image
    with resources.open_binary('aesthetic_ascii', IMAGES[n]) as fp:
        img = fp.read()
    img = Image.open(io.BytesIO(img))
    # convert to grayscale and return
    return img.convert('L')

def resize(img, new_width=300, ascii_ratio=1.9):
    # pull image width and height
    width, height = img.size
    # calculate ratio from image width and height
    # (also divide by ascii_ratio because ascii width and height are not equal)
    ratio = height / width / ascii_ratio
    # get new height, using the new_width
    new_height = int(new_width * ratio)
    # resize image to new dimensions
    return img.resize((new_width, new_height)), new_width, new_height

def get_char(brightness, dark_mode=False):
    # get index value
    index = int((brightness/255)*(len(ASCII)-1))
    # check for dark mode vs light mode
    if dark_mode:
        # return character at index (dark)
        return ASCII_DARK[index]
    else:
        # return character at index (light)
        return ASCII[index]

def to_ascii(img, dark_mode=False):
    # get generator of pixel brightness in image
    pixels = img.getdata()
    # pixel values will be in range 0-255 - we use this to select ASCII
    # character based on the intensity value (0 = dark, 255 = light)
    return "".join([get_char(pixel, dark_mode) for pixel in pixels])

def resize_ascii(ascii_list, width):
    pass

class Drive:
    def __init__(self):
        # open font resource
        with resources.open_binary('aesthetic_ascii', 'RobotoMono-VariableFont_wght.ttf') as fp:
            font = fp.read()
        # initialize font
        self.font = ImageFont.truetype(io.BytesIO(font))

    def generate(self, width=300, ascii_ratio=2, dark_mode=False):
        """Method that generates the ASCII image. Creates ASCII text image
        and stores in internal img attribute.

        :param width: number of characters in each line (like ascii pixels),
            defaults to 300
        :param ascii_ratio: ratio of height-to-width of ascii characters,
            defaults to 1.8
        :param dark_mode: whether to use ascii dark mode (for dark backgrounds)
            or light mode, defaults to False
        """
        # assign values as attributes
        self.width = width
        self.ascii_ratio = ascii_ratio
        self.dark_mode = dark_mode
        # get a random image
        img = get_image()
        # resize
        img, self.ascii_width, self.ascii_height = resize(img, width, ascii_ratio)
        # convert to ascii
        self.img = to_ascii(img, dark_mode=dark_mode)
        # split based on width
        self.img = "\n".join(self.img[i:i+self.width] for i in range(
                0, len(self.img), self.width
        ))

    def print_out(self):
        # print the image to screen
        print(self.img)

    def to_txt(self, filepath):
        """Save ASCII image to text file.

        :param filepath: filepath to save to, including file extension (eg .txt)
        """
        # save to text file
        with open(filepath, 'w') as fp:
            fp.write(self.img)

    def to_png(self, filepath):
        # set font and background color
        font_color = '#FFFFFF' if self.dark_mode else '#000000'
        color = '#000000' if self.dark_mode else '#FFFFFF'
        # get required image width and height
        w = int(self.ascii_width * 6.1)
        h = int(self.ascii_height * 15.3)
        # initialize image background
        bg = Image.new('RGBA', (w, h), color)
        # draw text
        draw = ImageDraw.Draw(bg)
        draw.text((15, 15), self.img, font=self.font, fill=font_color)
        # save as image
        bg.save(filepath)
