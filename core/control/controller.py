# platform/controller.py
class Controller:
    def click(self, x, y):
        raise NotImplementedError("click method must be implemented")

    def type(self, text):
        raise NotImplementedError("type method must be implemented")
    
    def swipe(self, x_list, y_list):
        raise NotImplementedError("swipe method must be implemented")

class PCController(Controller):
    def click(self, x, y):
        # 使用 pyautogui 进行点击
        pass

    def type(self, text):
        # 使用 pynput 进行输入
        pass

    def swipe(self, x_list, y_list):
        # 使用 pyautogui 进行输入
        pass

class EmulatorController(Controller):
    def click(self, x, y):
        # 使用 adb shell input tap 命令
        pass

    def type(self, text):
        # 使用 adb shell input text 命令
        pass

    def swipe(self, x_list, y_list):
        # 使用 adb shell input text 命令
        pass