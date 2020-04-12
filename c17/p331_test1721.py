from PIL import Image

cat = Image.open('../resource/image/zophie.png')
print(cat.size)
print(cat.filename)
print(cat.format)
print(cat.format_description)
cat.close()

print()

im = Image.new('RGBA', (100, 200), 'purple')
im.save('../resource/image/output/purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('../resource/image/output/transparentImage.png')
print('Output Success')

"""
(816, 1088)
../resource/image/zophie.png
PNG
Portable network graphics

Output Success
"""
