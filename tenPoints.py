import cv2
import csv

def merge_channels(input_dir, output_dir):
    image_counter = open(input_dir + '\image_counter.txt', "r")
    imageCounter = int(image_counter.read())

    with open(input_dir + '\description.csv') as inputFile:
        readList = list(csv.reader(inputFile))
        counter = 0
        for i in range(1, imageCounter*3, 3):
            imageFirst = cv2.imread(input_dir + '\data/' + readList[i][2])
            b = cv2.split(imageFirst)[0]
            imageSecond = cv2.imread(input_dir + '\data/' + readList[i+1][2])
            g = cv2.split(imageSecond)[1]
            ImageThird = cv2.imread(input_dir + '\data/' + readList[i+2][2])
            r = cv2.split(ImageThird)[2]
            outputImage = cv2.merge([b, g, r])
            cv2.imwrite(output_dir + "/" + str(counter + 1) + ".jpg", outputImage)
            counter+=1

merge_channels("C:\VEZDECOD\Vision", "C:\VEZDECOD\Vision\out")