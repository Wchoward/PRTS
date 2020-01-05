import cv2 as cv
import os
import numpy as np


def test_level_selection(target_image):
    #
    # 关卡选择模板
    #
    template_image = cv.imread(
        os.path.join(os.getcwd(), 'template', 'level_selection-1705-877-1853-917.png'), cv.IMREAD_GRAYSCALE)

    cut_image = target_image[877:917, 1705:1853]

    # 全局阈值
    difference = cv.absdiff(cut_image, template_image)
    result = not np.any(difference)
    # print(result)
    # cv.imshow('cut_image', cut_image)
    # cv.imshow('template_image', template_image)
    # cv.imshow('difference', difference)
    # cv.waitKey(0)
    return result


def test_team_up(target_image):
    #
    # 队伍选择模板
    #
    template_image = cv.imread(os.path.join(os.getcwd(), 'template', 'team_up-1523-640-1661-778.png'),
                               cv.IMREAD_GRAYSCALE)

    cut_image = target_image[640:778, 1523:1661]

    # 全局阈值
    difference = cv.absdiff(cut_image, template_image)
    result = not np.any(difference)
    # print(result)
    # cv.imshow('cut_image', cut_image)
    # cv.imshow('template_image', template_image)
    # cv.imshow('difference', difference)
    # cv.waitKey(0)
    return result


def test_battle_settlement(target_image):
    #
    # 游戏结算模板
    #
    # 模板图片
    template_image = cv.imread(
        os.path.join(os.getcwd(), 'template', 'battle_settlement-53-794-538-913.png'), cv.IMREAD_GRAYSCALE)

    # 正向目标图片
    cut_image = target_image[794:913, 53:538]

    # Otsu 阈值
    _, cut_image_battle_settlement_new = cv.threshold(cut_image, 170, 255,
                                                      cv.THRESH_BINARY + cv.THRESH_OTSU)
    _, template_image_battle_settlement_new = cv.threshold(template_image, 170, 255,
                                                           cv.THRESH_BINARY + cv.THRESH_OTSU)

    difference = cv.absdiff(cut_image_battle_settlement_new, template_image_battle_settlement_new)
    mean, std_dev = cv.meanStdDev(difference)
    # print(mean)
    # print(std_dev)
    result = mean[0][0] < 1
    # print(result)
    # cv.imshow('cut_image', cut_image)
    # cv.imshow('template_image', template_image)
    # cv.imshow('difference', difference)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    return result


def test_restore_mind_medicine(target_image):
    #
    # 理智恢复-药剂模板
    #
    template_image = cv.imread(
        os.path.join(os.getcwd(), 'template', 'restore_mind_medicine-1033-115-1273-171.png'), cv.IMREAD_GRAYSCALE)

    cut_image = target_image[115:171, 1033:1273]

    # 全局阈值
    difference = cv.absdiff(cut_image, template_image)
    result = not np.any(difference)
    # print(result)
    # cv.imshow('cut_image', cut_image)
    # cv.imshow('template_image', template_image)
    # cv.imshow('difference', difference)
    # cv.waitKey(0)
    return result


def test_restore_mind_stone(target_image):
    #
    # 理智恢复-药剂模板
    #
    template_image = cv.imread(
        os.path.join(os.getcwd(), 'template', 'restore_mind_stone-1464-115-1748-168.png'), cv.IMREAD_GRAYSCALE)

    cut_image = target_image[115:168, 1464:1748]

    # 全局阈值
    difference = cv.absdiff(cut_image, template_image)
    result = not np.any(difference)
    # print(result)
    # cv.imshow('cut_image', cut_image)
    # cv.imshow('template_image', template_image)
    # cv.imshow('difference', difference)
    # cv.waitKey(0)
    return result


if __name__ == '__main__':

    # 把test_case下的所有图片读出来，丢给目标函数检查，输出每一次的检查结果和被检查的文件名

    target_images = {}

    for test_file in os.listdir(os.path.join(os.getcwd(), 'test_case')):
        image = cv.imread(
            os.path.join(os.getcwd(), 'test_case', test_file), cv.IMREAD_GRAYSCALE
        )
        target_images[test_file] = image
    print(f"read {len(target_images)} test cases")

    success_count = 0
    fail_count = 0

    test_target = 'restore_mind_stone'
    test_active_only = False
    test_method = {
        "level_selection": test_level_selection,
        "team_up": test_team_up,
        "battle_settlement": test_battle_settlement,
        "restore_mind_medicine": test_restore_mind_medicine,
        "restore_mind_stone": test_restore_mind_stone,
    }
    test_string = {
        "level_selection": "enter_team_up",
        "team_up": "enter_game",
        "battle_settlement": "leave_settlement",
        "fighting": "fighting",
        "restore_mind_medicine": "restore_mind_medicine",
        "restore_mind_stone": "restore_mind_stone",
    }

    for case_name, image in target_images.items():
        actual = test_string[test_target] in case_name
        # 当test_active_onely 为真时只测试正向case，为负时测全部
        if test_active_only and not actual:
            continue
        test_result = test_method[test_target](image)
        if test_result == actual:
            success_count += 1
        else:
            fail_count += 1
            print(f"failed test case: {case_name}, wanted result is {actual}, but get {test_result}")
    print(f"test finished, success: {success_count}, fail: {fail_count}")
