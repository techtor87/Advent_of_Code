from functools import reduce

"""Monkey 0:
  Starting items: 75, 63
  Operation: new = old * 3
  Test: divisible by 11
    If true: throw to monkey 7
    If false: throw to monkey 2

Monkey 1:
  Starting items: 65, 79, 98, 77, 56, 54, 83, 94
  Operation: new = old + 3
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 66
  Operation: new = old + 5
  Test: divisible by 5
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 3:
  Starting items: 51, 89, 90
  Operation: new = old * 19
  Test: divisible by 7
    If true: throw to monkey 6
    If false: throw to monkey 4

Monkey 4:
  Starting items: 75, 94, 66, 90, 77, 82, 61
  Operation: new = old + 1
  Test: divisible by 17
    If true: throw to monkey 6
    If false: throw to monkey 1

Monkey 5:
  Starting items: 53, 76, 59, 92, 95
  Operation: new = old + 2
  Test: divisible by 19
    If true: throw to monkey 4
    If false: throw to monkey 3

Monkey 6:
  Starting items: 81, 61, 75, 89, 70, 92
  Operation: new = old * old
  Test: divisible by 3
    If true: throw to monkey 0
    If false: throw to monkey 1

Monkey 7:
  Starting items: 81, 86, 62, 87
  Operation: new = old + 8
  Test: divisible by 13
    If true: throw to monkey 3
    If false: throw to monkey 5
"""


class Monkey(object):
    def __init__(self, test_val, pass1, pass2, op, *args, **kwargs):
        self.items = [i for i in args]
        self.test_val = test_val
        self.monkey_1 = pass1
        self.monkey_2 = pass2
        self.op = op
        self.inspect_count = 0

    def Test(self, worry):
        self.inspect_count += 1
        if (worry % self.test_val) == 0:
            return self.monkey_1
        else:
            return self.monkey_2

    def operation(self, worry):
        old = worry
        return eval(self.op)

    def receive_item(self, item):
        self.items.append(item)


monkeys = [
    Monkey(11, 7, 2, "old * 3", 75, 63),
    Monkey(2, 2, 0, "old + 3", 65, 79, 98, 77, 56, 54, 83, 94),
    Monkey(5, 7, 5, "old + 5", 66),
    Monkey(7, 6, 4, "old * 19", 51, 89, 90),
    Monkey(17, 6, 1, "old + 1", 75, 94, 66, 90, 77, 82, 61),
    Monkey(19, 4, 3, "old + 2", 53, 76, 59, 92, 95),
    Monkey(3, 0, 1, "old * old", 81, 61, 75, 89, 70, 92),
    Monkey(13, 3, 5, "old + 8", 81, 86, 62, 87),
]


# monkeys = [
#     Monkey(23, 2, 3, "old * 19", 79, 98),
#     Monkey(19, 2, 0, "old + 6", 54, 65, 75, 74),
#     Monkey(13, 1, 3, "old * old", 79, 60, 97),
#     Monkey(17, 0, 1, "old + 3", 74)
# ]

part2 = True

var = reduce(lambda accu, m: accu * m.test_val, monkeys, 1) if part2 else None
for i in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            new_worry = monkey.operation(item)
            newest_worry = new_worry % var if part2 else new_worry // 3
            new_monkey = monkey.Test(newest_worry)
            monkeys[new_monkey].receive_item(newest_worry)
        monkey.items = []

    if i in [1, 20, 1000, 2000, 3000]:
        print(f"\nRound {i}")
        for monkey in monkeys:
            print(f"{monkey.inspect_count=} - {monkey.items}")

for i, monkey in enumerate(monkeys):
    print(f"Monkey {i} - {monkey.inspect_count}")
count_list = [m.inspect_count for m in monkeys]
count_list.sort()

print(f"{count_list[-1]*count_list[-2]}")
