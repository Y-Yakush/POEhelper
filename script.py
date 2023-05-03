import numpy
import cv2
from PIL import ImageGrab
from plyer import notification


def image_analyser(img):
    blr_img = cv2.GaussianBlur(img, (11, 11), 80)
    hsv_img = cv2.cvtColor(blr_img, cv2.COLOR_BGR2HSV)

    lower_red = numpy.array([0, 50, 50])
    upper_red = numpy.array([10, 255, 255])
    lower_red2 = numpy.array([170, 50, 50])
    upper_red2 = numpy.array([180, 255, 255])

    mask_find_red = cv2.inRange(hsv_img, lower_red, upper_red) + cv2.inRange(hsv_img, lower_red2, upper_red2)

    smoothing_kernel = numpy.ones((12, 12), numpy.uint8)
    mask_kernel = cv2.morphologyEx(mask_find_red, cv2.MORPH_OPEN, smoothing_kernel)

    contours, hierarchy = cv2.findContours(mask_kernel, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    active_blocks = len(contours)

    # Отрисовка найденных кругов на изображении
    img_copy = img.copy()
    cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2)
    cv2.imwrite('src/final.jpg', img_copy)

    return active_blocks


def active_elements_search():
    img = ImageGrab.grabclipboard()
    if img:
        img.save('src/image.jpg')
        img = cv2.imread('src/image.jpg')

        notification_message = image_analyser(img)

        notification.notify(
            title='Твоих херовин',
            message=str(notification_message),
            app_icon='src/poe.ico',
            timeout=1
        )

    else:
        notification.notify(
            title='Эй, лошара!',
            message='Буфер обмена пуст!',
            app_icon='src/poe.ico',
            timeout=1
        )
