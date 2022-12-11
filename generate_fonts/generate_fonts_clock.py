from PIL import Image, ImageDraw, ImageFont


W=48
H=60
font = ImageFont.truetype("JetBrainsMono-ExtraBold.ttf", 80, encoding='utf-8')

names = list(range(10)) + ['colon']
values = list(range(10)) + [':']

for n, v in zip(names, values):
    image = Image.new('1', (W, H), "black")
    draw = ImageDraw.Draw(image)
    offset_w, offset_h = font.getoffset(str(v))
    w, h = draw.textsize(str(v), font=font)
    pos = ((W-w-offset_w)/2, (H-h-offset_h)/2)
    # Draw
    draw.text(pos, str(v), "white", font=font)
    # Save png file
    image.convert('RGB').save(f"clock_{n}.png")


import subprocess
subprocess.call('echo "# Generated automatically by generate_fonts.py" > ../wasp/fonts/clock.py',shell=True)
subprocess.call('python ../tools/rle_encode.py clock_*.png >> ../wasp/fonts/clock.py',shell=True)
