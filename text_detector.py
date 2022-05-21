import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/opt/local/bin/tesseract'

def text_from_image(file):
	img = cv2.imread(file)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

	rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
	dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
	contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

	im2 = img.copy()

	content = ""

	for cnt in contours:
		x, y, w, h = cv2.boundingRect(cnt)
		rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cropped = im2[y:y + h, x:x + w]
		text = pytesseract.image_to_string(cropped)
		content += text

	return content

print(text_from_image("./test/IMG_3968.jpeg"))