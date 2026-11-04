from demo_python_pkg.person_node import PersonNode

class WriterNode(PersonNode):
    def __init__(self, name: str, age: int, book: str) -> None:
        print('WriterNode __init__方法被调用了')
        super().__init__(name, age)
        self.book = book

def main():
    node = WriterNode('法外狂徒张三', 18, '论快速入狱')
    node.eat('鱼香肉丝')
    print(f'{node.name} 正在写《{node.book}》')

if __name__ == '__main__':
    main()
