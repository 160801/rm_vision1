class PersonNode:
    def __init__(self, name_value: str, age_value: int) -> None:
        print('PersonNode __init__ 方法被调用了，添加了两个属性')
        self.name = name_value
        self.age = age_value

    def eat(self, food_name: str):
        """
        方法: 吃东西
        :food_name 食物名字
        """
        print(f"{self.name}, {self.age}岁, 爱吃{food_name}")

def main():
    node = PersonNode('法外狂徒张三', 18)
    node.eat('鱼香肉丝')


if __name__ == '__main__':
    main()
