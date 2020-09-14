# 2020.09.14 add a random mask for each pic in dataset

import cv2 as cv
import os
import sys
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
import pylab
import numpy as np
import random

data_root = "/Users/firmiana/data"
save_path = "/Users/firmiana/data_mask"

class pic_Mask(object):

    def __init__(self, original_path, new_path):
        # super(pic_Mask, self).__init__()
        self.count_pic = 0
        self.ls_file = []
        self.old_path = original_path
        self.new_path = new_path

    def search(self):       
        for filename in os.listdir(self.old_path):
            self.count_pic += 1
            # print("file ", self.count_pic, ":", filename)
            self.ls_file.append(filename)

        # test
        '''
        for i in range(self.count_pic):
            print(self.ls_file[i])
        '''

    def add_mask(self):

        for i in range(self.count_pic):
            img1_path = os.path.join(self.old_path, self.ls_file[i])
            img2_path = os.path.join(self.new_path, self.ls_file[i])
            img1 = cv.imread(img1_path)
            img2 = Image.open(img1_path)
            (x, y, channel) = img1.shape

            # 256 * 256 into 6 parts
            range_width = x / 6
            range_width = int(range_width)
            for i in range(6):
                boundary = (range_width * i)
                width1 = random.randint(boundary, boundary + 42)
                width_ran = random.randint(5, 15)
                draw = ImageDraw.Draw(img2)
                if(width1 < boundary + 42 - 5):
                    start = width1
                else:
                    start = width1 - 5
                draw.rectangle((start, 0, start + width_ran, 255), fill = (0, 0, 0))
            img2 = np.asarray(img2)
            cv.imwrite(img2_path, img2)
            print("file ", img2_path, "write success! ")
        '''
        cv.namedWindow("add_pic")
        cv.imshow("add_pic", img2)
        cv.waitKey(0)
        cv.destroyWindow()
        '''

if __name__ == "__main__":
    Mask_edit = pic_Mask(data_root, save_path)
    Mask_edit.search()
    Mask_edit.add_mask()