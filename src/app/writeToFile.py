from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
 
# in_file, out_file, text = sys.argv[1:]

# in_file = "C:/personal-git/aresta-barcode/src/app/isle-labels.png"
in_file = "C:/personal-git/aresta-barcode/src/app/pil_color.png"
text ="001"
out_file = "isle-out.png"
 
img = Image.open(in_file)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('Roboto-Bold.ttf',20)
draw.text((0, 0), text, (1, 1, 1), font=font)
img.save(out_file)
