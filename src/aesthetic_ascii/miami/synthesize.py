import PIL.Image
import random

ASCII = '.\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

IMAGES = [
    'wallpaperuse.com-outrun-wallpaper-76590.png',
    'wallpaperuse.com-synthwave-wallpaper-1003075.jpg',
    'wallpaperuse.com-wallpapers-retro-803078.jpg',
    'wallpaperuse.com-retro-wallpaper-hd-999925.png',
    '31-synthwave-sun-waves-electronic-sky.jpg',
    'city-5848267_1920.jpg'
]

REPO = 'https//github.com/jamescalam/aesthetic_ascii/'
RAW_IMG = 'raw/main/assets/images/'

def get_image():
    # pick an image at random
    n = random.randint(0, len(IMAGES)-1)
    # open image
    img = PIL.Image.open(f'../assets/images/{IMAGES[n]}')
    # convert to grayscale and return
    return img.convert('L')

def resize(img, new_width=300, ascii_ratio=1.9):
    # pull image width and height
    width, height = img.size
    # calculate ratio from image width and height
    # (also divide by ascii_ratio because ascii width and height are not equal)
    ratio = height / width / asci_ratio
    # get new height, using the new_width
    new_height = int(new_width * ratio)
    # resize image to new dimensions
    return img.resize((new_width, new_height)), new_width

def get_char(brightness):
    # get index value
    index = int((brightness/255)*(len(ASCII)-1))
    # return character at index
    return ASCII[index]

def to_ascii(img):
    # get generator of pixel brightness in image
    pixels = img.getdata()
    # pixel values will be in range 0-255 - we use this to select ASCII
    # character based on the intensity value (0 = dark, 255 = light)
    return "".join([get_char(pixel) for pixel in pixels])

def resize_ascii(ascii_list, width):
    pass

def drive(definition=300, ascii_ratio=1.9):
    img = get_image()
    # resize
    img, width = resize(img, definition, ascii_ratio)
    # convert to ascii
    img = to_ascii(img)
    return img, width
