import random


class ScreenResolution:
    def __init__(self, length_x, width_y):
        self.length = int(length_x)
        self.width = int(width_y)
        if self.length < self.width:
            self.length, self.width = self.width, self.length

    def create_click_zone(self, left_up_x, left_up_y, right_down_x, right_down_y):
        return ClickZone(self, left_up_x, left_up_y, right_down_x, right_down_y)


class ClickZone:
    """保存可点击的区域，以及所属的屏幕尺寸"""

    def __init__(self, resolution: ScreenResolution, left_up_x: int, left_up_y: int, right_down_x: int,
                 right_down_y: int):
        self.resolution = resolution
        self.left_up_x = int(left_up_x)
        self.left_up_y = int(left_up_y)
        self.right_down_x = int(right_down_x)
        self.right_down_y = int(right_down_y)


class ClickHelper:
    def __init__(self, current_screen_resolution: ScreenResolution):
        """记录当前的屏幕分辨率"""
        self.current_screen_resolution = current_screen_resolution

    def generate_target_click(self, click_zone: ClickZone) -> (int, int):
        """根据目标屏幕分辨率，计算并生成点击位置"""
        # 从原始区域里选取点
        point_x = random.uniform(click_zone.left_up_x, click_zone.right_down_x)
        point_y = random.uniform(click_zone.left_up_y, click_zone.right_down_y)

        # 将点转化为目标分辨率的点
        new_x = point_x / click_zone.resolution.length * self.current_screen_resolution.length
        new_y = point_y / click_zone.resolution.width * self.current_screen_resolution.width
        return new_x, new_y