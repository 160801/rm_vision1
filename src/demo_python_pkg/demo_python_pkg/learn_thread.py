import threading
import requests


class Download:
    def download(self, url, callback_world_count):
        print(f'线程:{threading.get_ident()}开始下载：{url}')
        """下载 url 的内容，完成后调用回调函数"""
        response = requests.get(url)
        response.encoding = 'utf-8'
        callback_world_count(url, response.text)  # 调用回调函数

    def start_download(self, url, callback_world_count):
        # self.download(url, callback world count)
        thread = threading.Thread(target=self.download, args=(url, callback_world_count))
        thread.start()


def world_count(url, result):
    """
    普通函数, 用于回调
    """
    print(f"{url}:{len(result)}->{result[:5]}")


def main():
    download = Download()
    download.start_download('http://localhost:8000/novel1.txt', world_count)
    download.start_download('http://localhost:8000/novel2.txt', world_count)
    download.start_download('http://localhost:8000/novel3.txt', world_count)
