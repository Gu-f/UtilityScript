import queue
import threading
import time


def read_file():
    with open(filePath,'r') as fp:
        file_data = fp.readlines()
    dataList = file_data
    dataLength = len(dataList)
    flag_xy = 0
    while flag_xy != dataLength:
        while (not workQueue.full()) and (flag_xy != dataLength):
            workQueue.put(dataList[flag_xy])
            flag_xy += 1
        continue
    # print("文件内容放入队列完成")


def multi_start_tmain():
    while not workQueue.empty():
        file_line_api = workQueue.get()
        custom_def(file_line_api)


def custom_def(file_line_api):
    fileDataLine = file_line_api.strip()  # fileDataLine变量为文件的每一行内容,可直接用
    # ================= #
    # 自定义功能从下方开始
    # ================= #
    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    print(fileDataLine)  # 测试代码：将文件中每一行的信息延时1s输出
    time.sleep(1)


if __name__ == '__main__':
    # 以下为相关配置信息
    # =========================================================
    multi = 7  # 线程数量
    queueSize = 10  # 申请队列空间大小,值一般略大于multi的值
    filePath = "testfile.txt"  # 文件路径，和脚本同一目录下可直接用文件名
    waitTime = 1  # 文件线程准备时间(s)，默认1s，若需要读取的文件大小大于10M可增加至5s以上，文件越大设置的时间理论上越长
    # =========================================================

    threads = []
    workQueue = queue.Queue(queueSize)
    fileThread = threading.Thread(target=read_file)
    fileThread.start()
    print("文件读取线程准备时间%ss" %waitTime)
    time.sleep(waitTime)
    for i in range(multi+1):
        thread = threading.Thread(target=multi_start_tmain)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()
    fileThread.join()
    print("主线程结束，任务完成")
