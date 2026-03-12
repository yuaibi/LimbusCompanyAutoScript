import win32gui

# 用于回调的函数，每次找到一个窗口时被调用
def enum_windows_callback(hwnd, windows):
    window_title = win32gui.GetWindowText(hwnd)  # 获取窗口标题
    if window_title:  # 只打印有标题的窗口
        windows.append(window_title)

# 获取所有窗口的标题
def get_all_window_titles():
    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    return windows

# 获取并打印所有窗口标题
if __name__ == "__main__":
    window_titles = get_all_window_titles()
    for title in window_titles:
        print(title)