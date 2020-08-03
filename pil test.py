from PIL import Image
img = Image.open('out.png', 'r')
img=img.resize((144, 144))
img_w, img_h = img.size
background = Image.open('test.png', 'r')
bg_w, bg_h = background.size
offset = (19,22)
print((bg_w - img_w) // 2)
background.paste(img, offset)
background.save('get.png')