import cv2
import numpy as np
from PIL import ImageFilter, Image


def threshold(file):
    # pil_image=Image.open(file)
    # ImageFilter.

    # numpy_image=numpy.array(pil_img)
    img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.CV_8UC1)
    img = cv2.GaussianBlur(img,(5, 5), 0)
    # img = cv2.blur(img,(20, 20))
    # img = cv2.fastNlMeansDenoising(img, None, 9, 13)

    # imgArr = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    # pil_im = Image.fromarray(imgArr)
    # pil_im = pil_im.filter(ImageFilter.BLUR).filter(ImageFilter.MaxFilter(1))
    # numpy_image=np.array(pil_im)
    # img = cv2.cvtColor(numpy_image,cv2.COLOR_BGR2GRAY)

    ret3,th3 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return th3
    # return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)
