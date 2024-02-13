import imageio.v3 as iio 
filenames = ['snowman1.png', 'snowman2.png']
images = [ ]
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('snowman.gif', images, duration = 500, loop = 0)
