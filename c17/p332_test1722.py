from PIL import Image

cat = Image.open('../resource/image/zophie.png')
croppedIm = cat.crop((335, 345, 565, 560))
croppedIm.save('../resource/image/output/cropped.png')
print('All done')

"""
All done
"""
