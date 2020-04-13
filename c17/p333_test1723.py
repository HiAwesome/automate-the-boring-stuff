from PIL import Image

cat = Image.open('../resource/image/zophie.png')
catCopy = cat.copy()

faceIm = cat.crop((335, 345, 565, 560))
print(faceIm.size)
catCopy.paste(faceIm, (0, 0))
catCopy.paste(faceIm, (400, 500))
catCopy.save('../resource/image/output/pasted.png')

catWidth, catHeight = cat.size
faceWidth, faceHeight = faceIm.size
catCopyTwo = cat.copy()

for left in range(0, catWidth, faceWidth):
    for top in range(0, catHeight, faceHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))

catCopyTwo.save('../resource/image/output/tiled.png')
print('All done.')


"""
(230, 215)
0 0
0 215
0 430
0 645
0 860
0 1075
230 0
230 215
230 430
230 645
230 860
230 1075
460 0
460 215
460 430
460 645
460 860
460 1075
690 0
690 215
690 430
690 645
690 860
690 1075
All done.
"""
