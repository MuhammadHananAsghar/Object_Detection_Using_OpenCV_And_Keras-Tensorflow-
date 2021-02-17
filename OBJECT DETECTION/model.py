from img_utils import sliding_windows
from img_utils import image_pyramid
import cv2
import imutils
from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array


WIDTH = 600
PYR_SCALE = 1.5
WIN_STEP = 16
ROI_SIZE = (200, 200)
INPUT_SIZE = (224, 224)

orig = cv2.imread("humming_bird.jpg")
orig = imutils.resize(orig, width=WIDTH)
sample_image = orig
(H, W) = orig.shape[:2]

pyramid = image_pyramid(orig, scale=PYR_SCALE, minSize=ROI_SIZE)

rois = []
locs = []

for image in pyramid:
	scale = W / float(image.shape[1])

	for (x, y, roiOrig) in sliding_windows(image, WIN_STEP, ROI_SIZE):
		x = int(x * scale)
		y = int(y * scale)
		w = int(ROI_SIZE[0] * scale)
		h = int(ROI_SIZE[1] * scale)
		# cv2.rectangle(sample_image, (x, y), (w+x, y+h), (0, 255, 0), 2, 1)
		# cv2.imshow("OUTPUT", sample_image)
		# cv2.waitKey(0)

		roi = cv2.resize(roiOrig, INPUT_SIZE)
		roi = img_to_array(roi)
		roi = preprocess_input(img)

		rois.append(roi)
		locs.append((x, y, x + w, y + h))