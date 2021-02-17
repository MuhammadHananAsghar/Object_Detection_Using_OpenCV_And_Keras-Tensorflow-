import imutils


def sliding_windows(image, step, window_size):
	"""
	Params: 
			image: Input Image Array
			step: sliding windows gaps
			window_size: Size of sliding windows 
	"""
	for y in range(0, image.shape[0] - window_size[1], step):
		for x in range(0, image.shape[1] - window_size[0], step):
			yield (x, y, image[y: y+window_size[1], x: x+window_size[0]])


def image_pyramid(image, scale = 1.5, minSize = (224, 224)):
	# Yield Original Image
	yield image

	while True:
		width = int(image.shape[0] / scale)
		image = imutils.resize(image, width=width)

		if (image.shape[0] < minSize[0]) or (image.shape[1] < minSize[1]):
			break

		yield image