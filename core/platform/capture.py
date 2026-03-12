# core/platform/capture.py
import win32gui
import win32con
import win32ui
import win32api
import numpy as np 
import matplotlib.pyplot as plt
import time
from ctypes import windll
from PIL import Image
import pyuac
import sys

# 检查是否有管理员权限
def run_as_admin():
    # 如果当前脚本没有管理员权限，则调用 pyuac.runAsAdmin() 请求权限
    if not pyuac.isUserAdmin():
        try:
            pyuac.runAsAdmin(False)
            sys.exit(0)
        except Exception:
            sys.exit(1)



class Capture:
    def capture(self):
        raise NotImplementedError("Capture method must be implemented")

class PCCapture(Capture):
    def __init__(self, window_name, dpi_scale):
        # 在初始化时只调用一次 `initialize`，确保窗口初始化
        self.hwnd, self.width, self.height = self.initialize(window_name, dpi_scale)

    # 初始化窗口捕获，返回窗口设备上下文和内存设备上下文
    def initialize(self, window_name, dpi_scale):
        # 获取窗口句柄
        hwnd = win32gui.FindWindow(None, window_name)
        if hwnd == 0:
            print(f"Window '{window_name}' not found!")
            return None, None, None
        
        print(f"Window found with hwnd: {hwnd}")  # 打印窗口句柄

        if win32gui.IsIconic(hwnd):  # 如果窗口是最小化的
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 恢复窗口
            time.sleep(10) 
        # 获取窗口位置
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)

        # 获取窗口的宽高
        width = int((right - left) * dpi_scale)
        height = int((bottom - top) * dpi_scale)

        print(f"Window size: Width={width}, Height={height}")  # 打印窗口的宽高
        # 返回初始化结果
        return hwnd, width, height

    # 截取窗口图像并保存为文件
    def sceenshot(self):
        # 恢复窗口（如果窗口最小化了）
        if win32gui.IsIconic(self.hwnd):  # 如果窗口是最小化的
            print(f"Restoring window {self.hwnd}...")  # 打印恢复窗口的过程
            win32gui.ShowWindow(self.hwnd, win32con.SW_RESTORE)  # 恢复窗口
        
        # 获取窗口设备上下文
        srcdc = win32ui.CreateDCFromHandle(win32gui.GetWindowDC(self.hwnd))
        
        # 创建内存设备上下文
        memdc = srcdc.CreateCompatibleDC()


        # 创建位图对象
        bitmap = win32ui.CreateBitmap()
        bitmap.CreateCompatibleBitmap(srcdc, self.width, self.height)
        

        # 将窗口内容复制到内存位图
        memdc.SelectObject(bitmap)
        windll.user32.PrintWindow(self.hwnd, memdc.GetSafeHdc(), 3)

        # 获取位图信息和像素数据
        bmpinfo = bitmap.GetInfo()
        bmpstr = bitmap.GetBitmapBits(True)

        img = Image.frombuffer(
            "RGB",
            (bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
            bmpstr,
            "raw",
            "BGRX",
            0,
            1,
        )

        # 清理资源，确保每次截图都释放相关资源
        win32gui.DeleteObject(bitmap.GetHandle())
        memdc.DeleteDC()  # 删除内存设备上下文
        srcdc.DeleteDC()  # 删除源设备上下文
        win32gui.ReleaseDC(self.hwnd, win32gui.GetWindowDC(self.hwnd))

        return img

class EmulatorCapture(Capture):
    def capture(self):
        # 使用 adb 命令进行截图
        pass

if __name__ == "__main__":
    dpi_scale = 1.5
    window_name = "LimbusCompany"  # 窗口名称
    capture_instance = PCCapture(window_name, dpi_scale)  # 创建捕获实例，传入窗口名称
    if capture_instance.hwnd is None:
        print("Failed to initialize window capture.")
    else:
        for i in range (5):
            img = capture_instance.sceenshot()  # 调用 screenshot方法进行截图
            if img is not None:
                plt.imshow(img)
                plt.show()
            else:
                print("Failed to capture image.")