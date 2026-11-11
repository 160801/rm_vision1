# chapt3 — ROS2 话题通信（发布 / 订阅）

第 3 章练习：用 Python 节点实现小说章节的发布与订阅。

## 目录结构

```text
chapt3/
├── novel1.txt                          # 示例数据，由本地 HTTP 服务提供下载
└── src/demo_python_topic/
    ├── demo_python_topic/
    │   ├── novel_pub_node.py           # 发布者：下载整篇小说，每 5 秒发一行
    │   └── novel_sub_node.py           # 订阅者：接收并打印
    ├── resource/demo_python_topic
    ├── test/
    ├── package.xml
    └── setup.py
```

## 运行方式

```bash
# 1. 把 chapt3/src 放进一个 colcon 工作空间的 src/ 下，然后编译
colcon build --packages-select demo_python_topic
source install/setup.bash

# 2. 起一个本地 HTTP 服务，让发布节点能下载 novel1.txt
cd chapt3 && python3 -m http.server 8000

# 3. 另开两个终端
ros2 run demo_python_topic novel_pub_node
ros2 run demo_python_topic novel_sub_node
```

## 要点

- 发布者先把整篇小说塞进 `queue.Queue`，再用 `create_timer(5, ...)` 定时取一行发布，避免一次性刷屏。
- 话题名 `novel`，消息类型 `example_interfaces/msg/String`。
- `entry_points` 是可执行名到「模块:函数」的映射，写错或漏写会出现
  `Package 'xxx' found at ... but libexec directory ... does not exist` 之类的报错。
