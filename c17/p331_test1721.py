from PIL import Image

cat = Image.open('../resource/image/zophie.png')
print(cat.size)
print(cat.filename)
print(cat.format)
print(cat.format_description)
cat.close()

"""
(816, 1088)
../resource/image/zophie.png
PNG
Portable network graphics
"""
