import espeakng
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from queue import Queue
import threading
import time


class NovelSubNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info(f'{node_name}, 启动！')
        self.novels_queue = Queue()
        self.novel_subscriber = self.create_subscription(String, 'novel', self.novel_callback, 10)
        self.speech_thread = threading.Thread(target=self.speake_thread)
        self.speech_thread.start()

    def novel_callback(self, msg):
        self.novels_queue.put(msg.data)

    def speake_thread(self):
        speaker = espeakng.Speaker()
        speaker.voice = 'zh'
        while rclpy.ok():  # 检测当前ROS上下文是否ok
            if self.novels_queue.qsize() > 0:
                text = self.novels_queue.get()
                self.get_logger().info(f'朗读: {text}')
                speaker.say(text)  # 说
                speaker.wait()     # 等他说完
            else:
                # 让当前的线程休眠1s
                time.sleep(1)


def main():
    rclpy.init()
    node = NovelSubNode('novel_sub')
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()