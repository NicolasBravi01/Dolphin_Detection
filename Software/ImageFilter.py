import os
import cv2


#Filtro Scharr applicato verticalmente
def scharrFilter(inputFileName, outputFileName):
    image = cv2.imread(inputFileName, cv2.IMREAD_GRAYSCALE)
    scharr_vertical = cv2.Scharr(image, cv2.CV_64F, 0, 1)
    scharr_vertical = cv2.normalize(scharr_vertical, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imwrite(outputFileName, scharr_vertical)


def scharrFilterDirectory(inputDirectory, outputDirectory):
    file_list_os = os.listdir(inputDirectory)
    nFile = len(file_list_os)
    print(nFile)

    for i in range(nFile):
        nameFile = file_list_os[i]
        imagePath = os.path.join(inputDirectory, nameFile)
        outputPath = os.path.join(outputDirectory, nameFile)

        print('scharr', nameFile)
        scharrFilter(imagePath, outputPath)






#Filtro Sobel applicato verticalmente, con kernel size settato a 5
def sobelFilter(inputFileName, outputFileName):
    image = cv2.imread(inputFileName, cv2.IMREAD_GRAYSCALE)
    sobel_vertical = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    sobel_vertical = cv2.normalize(sobel_vertical, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imwrite(outputFileName, sobel_vertical)


def sobelFilterDirectory(inputDirectory, outputDirectory):
    file_list_os = os.listdir(inputDirectory)
    nFile = len(file_list_os)
    print(nFile)

    for i in range(nFile):
        nameFile = file_list_os[i]
        imagePath = os.path.join(inputDirectory, nameFile)
        outputPath = os.path.join(outputDirectory, nameFile)

        print('sobel', nameFile)
        sobelFilter(imagePath, outputPath)
