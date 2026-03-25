from PIL import Image

# monochrome
def show_monochrome_image(width, height, pixels):
  img = Image.new('1', (width, height))
  if pixels is not None:
      if isinstance(pixels[0], list):
          pixels = list(zip(*pixels))
          pixels = [item for sublist in pixels for item in sublist]
      img.putdata(pixels)
  
  newsize = (img.width, img.height)
  while newsize[0]<10000:
    newsize =(newsize[0]*2, newsize[1]*2)
  im_new = img.resize(newsize)
  im_new.save(r"./cx_out/output_image.png")

def new_monochrome_pixels(w,h):
    return [0 for y in range(w*h)]
    
def new_monochrome_pixels_2d(w,h):
    return [[0 for y in range(h)] for x in range(w)]

# grayscale
def show_grayscale_image(width, height, pixels):
    img = Image.new('L', (width,height))
    if pixels is not None:
        if isinstance(pixels[0], list):
            pixels = list(zip(*pixels))
            pixels = [item for sublist in pixels for item in sublist]
        img.putdata(pixels)
        
    newsize = (img.width, img.height)
    while newsize[0]<10000:
      newsize =(newsize[0]*2, newsize[1]*2)
    im_new = img.resize(newsize, Image.Resampling.NEAREST)
    im_new.save(r"./cx_out/output_image.png")

def new_grayscale_pixels(w,h):
    return [0 for y in range(w*h)]
    
def new_grayscale_pixels_2d(w,h):
    return [[0 for y in range(h)] for x in range(w)]
    
def load_grayscale_pixels(filename):
  if type(filename) == type('foo'):
    im = im = Image.open(filename).convert('L')
  else:
    im = filename
  w,h = im.size
  return w,h,list(im.getdata())

def load_grayscale_pixels_2d(filename):
  if type(filename) == type('foo'):
    im = im = Image.open(filename).convert('L')
  else:
    im = filename
  w,h = im.size
  data = im.getdata()
  return w,h,[[data[y*w + x] for y in range(h)] for x in range(w)]
    
# rgb
def show_rgb_image(width, height, pixels):
  img = Image.new('RGB', (width, height))
  if pixels is not None:
      if isinstance(pixels[0], list):
          pixels = list(zip(*pixels))
          pixels = [item for sublist in pixels for item in sublist]
      img.putdata(pixels)
  
  newsize = (img.width, img.height)
  while newsize[0]<200:
    newsize =(newsize[0]*2, newsize[1]*2)
  im_new = img.resize(newsize)
  im_new.save(r"./cx_out/output_image.png")
  
def new_rgb_pixels_2d(w,h):
    return [[(0,0,0) for y in range(h)] for x in range(w)]


def load_rgb_pixels_2d(filename):
    if type(filename) == type('foo'):
        im = Image.open(filename).convert("RGB")
    else:
        im = filename
    w, h = im.size
    data = im.getdata();
    return w,h,[[data[y*w + x] for y in range(h)] for x in range(w)]