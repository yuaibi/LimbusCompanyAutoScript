# core/platform/factory.py

from .capture import PCCapture, EmulatorCapture
from .controller import PCController, EmulatorController

class PlatformFactory:
    def create_capture(self, platform, window_name):
        """
        创建平台相关的截图实例
        """
        if platform == "PC":
            return PCCapture("MuMu安卓设备")
        elif platform == "Emulator":
            return EmulatorCapture()
        else:
            raise ValueError(f"Unsupported platform: {platform}")

    def create_controller(self, platform):
        """
        创建平台相关的控制实例
        """
        if platform == "PC":
            return PCController()
        elif platform == "Emulator":
            return EmulatorController()
        else:
            raise ValueError(f"Unsupported platform: {platform}")