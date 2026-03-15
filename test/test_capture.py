import time
import psutil
from datetime import datetime
from PIL import Image

import sys
import os
sys.path.append(r'c:\Users\yuaib\LimbusCompanyAutoScript')
# 确认路径设置无误
print(os.getcwd())

from core.capture import PCCapture, EmulatorCapture
from core.controller import PCController, EmulatorController


# 测试截图函数的时间消耗、长时间稳定性和资源消耗
def test_capture_window(window_name, num_tests, dpi_scale):

    # 记录开始时间
    start_time = time.time()
    capture_times = []  # 存储每次截图的时间消耗

    # 获取进程ID和进程对象（用于监控资源）
    process = psutil.Process()

    print("测试开始时间:", datetime.now())

    #初始化capture_window
    capture_instance = PCCapture(window_name, dpi_scale)  # 创建捕获实例，传入窗口名称
    if capture_instance.hwnd == 0:
        print(f"Window '{window_name}' not found!")
        print(f'初始化失败')
        return 

    # 循环多次执行截图
    for i in range(num_tests):
        print(f"开始第 {i+1} 次截图...")
        # 测量每次截图的时间消耗
        capture_start_time = time.time()

        # 调用 capture_window 函数进行截图
        image = capture_instance.sceenshot()
        print(image)
        image.save("debug.png")

        # 记录结束时间并计算消耗的时间
        capture_end_time = time.time()
        capture_duration = capture_end_time - capture_start_time
        capture_times.append(capture_duration)
        
        # 打印每次截图的时间消耗
        print(f"第 {i+1} 次截图耗时: {capture_duration:.4f} 秒")

    # 记录结束时间
    end_time = time.time()

    # 计算总的测试时间
    total_time = end_time - start_time
    print(f"\n总测试时间: {total_time:.4f} 秒")
    
    # 输出平均截图时间
    avg_capture_time = sum(capture_times) / len(capture_times)
    print(f"平均截图时间: {avg_capture_time:.4f} 秒")

    # 监控 CPU 和内存消耗
    print("\n资源消耗分析:")
    cpu_percent = process.cpu_percent(interval=1)  # 获取 CPU 使用率
    memory_info = process.memory_info()  # 获取内存信息
    print(f"CPU 使用率: {cpu_percent}%")
    print(f"内存使用情况: {memory_info.rss / (1024 * 1024):.2f} MB")

    print("\n测试完成！")


# 使用多线程来模拟长时间运行中的稳定性
def run_test_in_thread(window_name, num_tests):
    test_thread = threading.Thread(target=test_capture_window, args=(window_name, num_tests))
    test_thread.start()
    test_thread.join()

    print("\n所有测试完成！")


if __name__ == "__main__":
    dpi_scale = 1.5
    window_name = "LimbusCompany"  # 窗口名称
    num_tests = 200
    test_capture_window(window_name, num_tests, dpi_scale) 