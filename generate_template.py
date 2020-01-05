import cv2 as cv
import os
from ArknightsStatusChecker import ArknightsStatusChecker

flags = True
start_x = 0
start_y = 0
end_x = 0
end_y = 0


# 用于生成模板，读取目标图片并弹出窗口以供剪切模板，剪切后输出至当前目录
def cut_template(filepath, target_status):
    image = cv.imread(filepath, cv.IMREAD_GRAYSCALE)

    # cv.IMREAD_UNCHANGED

    def cut(event, x, y, flag, param):
        global flags, start_x, start_y, end_x, end_y
        if event == cv.EVENT_LBUTTONDOWN:
            if flags:
                start_x = x
                start_y = y
                flags = False
            else:
                end_x = x
                end_y = y

    cv.namedWindow('image_original', cv.WINDOW_NORMAL)
    cv.setMouseCallback('image_original', cut)
    cv.imshow('image_original', image)
    cv.waitKey(0)
    print(start_x)
    print(start_y)
    print(end_x)
    print(end_y)
    newimg = image[start_y:end_y, start_x:end_x]
    cv.imshow('image', newimg)
    cv.waitKey(0)
    cv.imwrite(os.path.join(os.getcwd(), f"{target_status}-{start_x}-{start_y}-{end_x}-{end_y}.png"), newimg)
    cv.destroyAllWindows()


if __name__ == '__main__':
    cut_template(
        os.path.join(os.getcwd(), 'test_case', 'restore_mind_medicine_MuMu20200105015933.png'),
        ArknightsStatusChecker.ASC_STATUS_RESTORE_MIND_MEDICINE)