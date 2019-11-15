import os.path
import sys
import queue
from threading import Thread
import time
from youtube_upload import main
from modal import ComUser
from jsonutils import getData

sys.path.insert(0, os.path.join(os.path.dirname(
    os.path.realpath(__file__)), os.pardir))
os.environ["https_proxy"] = "https://127.0.0.1:1080"  # 增加代理

class UploadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            read = self.queue.get()
            main.run2("test", "this is desc", "xx, bb, oo", "C:/1.mp4")
            self.queue.task_done()


if __name__ == "__main__":
    content = []
    data = getData()
    user_id_list = []
    for item in data:
        user_id_list.append(item["user_id"])

    query = ComUser.select().where(ComUser.user_id << ("109638574452t", "109638574452"))
    for x in query:
        print(x)
 
    # queue = queue.Queue()
    # for num in range(1, 100):
    #     content.append({"num": num})
    #     queue.put(num)

    # print(queue.qsize)

    # for i in range(1, 11):
    #     w = UploadWorker(queue)
    #     w.daemon = True
    #     w.start()

    # queue.join()
    # print("finish all task")
