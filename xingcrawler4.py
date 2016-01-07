import glob
from PIL import Image

fname_list = glob.glob('*.jpg')
for fname in fname_list:
    try:
	    raw_image = Image.open(fname)
	    factor = 500/raw_image.width
	    resized_image = raw_image.resize((500,int(raw_image.height*factor)),Image.ANTIALIAS)
	    resized_image.save("resized_images/resized_"+fname, "JPEG", quality=100)
    except:
        print(fname+'에러발생')
