import cv2
from os.path import join, dirname, realpath


UPLOAD_FOLDER = join(dirname(realpath(__file__)),'templates/images/')
UPLOAD_FOLDERC = join(dirname(realpath(__file__)),'templates/mulsegimages/')

def apply_threshold(filename):
    img = cv2.imread(UPLOAD_FOLDER+filename,0)

    cv2.imwrite(UPLOAD_FOLDERC + 'original.png', img)


    img = cv2.medianBlur(img,5)

    ret,th1 = cv2.threshold(img,80,255,cv2.THRESH_BINARY)

    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,115,14)

    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,115,14)

    cv2.imwrite(UPLOAD_FOLDERC + 'global_thresh.png', th1)
    cv2.imwrite(UPLOAD_FOLDERC + 'adaptive_mean_thresh.png', th2)
    cv2.imwrite(UPLOAD_FOLDERC + 'adaptive_thresh_gaussian.png', th3)

    # titles = ['Original Image', 'Global Thresholding (v = 127)',
    #             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

    # images = [img, th1, th2]



    cv2.imwrite(str(UPLOAD_FOLDER)+'inverted_final.png',th2)
    blurred = cv2.medianBlur(th2,9)



    # cv2.imwrite(str(UPLOAD_FOLDER)+'thresholded.png',th2)
    # blurred = cv2.medianBlur(th2,9)
    cv2.imwrite(UPLOAD_FOLDERC+'median_blurred.png',blurred)

    # gray = cv2.cvtColor(th2, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(UPLOAD_FOLDERC+'gray.png',gray)

    # new=cv2.imread('out.bmp',0)
    # grayd = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)



    inverted = 255 - blurred
    cv2.imwrite(UPLOAD_FOLDERC+'inverted.png',inverted)




