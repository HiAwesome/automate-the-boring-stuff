from PIL import Image

cat = Image.open('../resource/image/zophie.png')
catCopy = cat.copy()

faceIm = cat.crop((335, 345, 565, 560))
print(faceIm.size)
catCopy.paste(faceIm, (0, 0))
catCopy.paste(faceIm, (400, 500))
catCopy.save('../resource/image/output/pasted.png')
print('All done.')

"""
(230, 215)
All done.
"""
