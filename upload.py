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

BASE_PATH = "C:/workspace/py/amemv-crawler/download"
PREFIX = "【抖音】【转载】"
category = "Pets & Animals"  # 娱乐

v_count = 0


class UploadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            user = self.queue.get()
            uploadVideo(user)
            self.queue.task_done()


def uploadVideo(user):
    v_path = "%s\\%s\\%s\\%s.mp4" % (
        BASE_PATH, user.tags, user.user_id, user.v_uri)
    main.run2(user.desc, user.desc, user.tags, v_path, category)
    q = ComUser.update(isupload=True).where(
        (ComUser.user_id == user.user_id) & (ComUser.v_uri == user.v_uri))
    q.execute()
    global v_count
    v_count += 1
    print(v_count)


if __name__ == "__main__":
    content = []
    data = getData()
    queue = queue.Queue()

    user_url_list = []
    for item in data:
        user_url_list.append(item["url"])

    query = ComUser.select().where((ComUser.user_url << user_url_list) &
                                   (ComUser.isupload == False) & (ComUser.v_size != 0))
    # sql = query.sql()
    # print(sql)
    for user in query:
        name = user.user_name
        user.desc = PREFIX + "【" + name + "】" + user.desc
        # print(user)
        # queue.put(user)
        try:
            uploadVideo(user)
        except e:
            print(e)
            break

    # if(queue.empty()):
    #     print('no need upload')

    # else:
    #     # 10 Thread
    #     for i in range(1, 11):
    #         w = UploadWorker(queue)
    #         w.daemon = True
    #         w.start()

    #     queue.join()

    #     print("Upload All Video Done")
