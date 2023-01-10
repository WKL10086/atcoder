# part 2 dont know why wrong but test case correct
from __future__ import annotations

working_stage = 3
test_part_1_answer = 152
test_part_2_answer = 301

if working_stage == 1:
    is_testing = True
    is_part_1 = True
elif working_stage == 2:
    is_testing = False
    is_part_1 = True
elif working_stage == 3:
    is_testing = True
    is_part_1 = False
else:
    is_testing = False
    is_part_1 = False


class Node:
    def __init__(self, name: str):
        self.name = name
        self.children: list[Node] = []
        self.operation: str | None = None
        self.value: int | None = None

    def __repr__(self):
        return f"{self.name}, {self.value}"

    def get_value_part_1(self) -> int:
        if self.value is not None:
            return self.value
        else:
            left_value = self.children[0].get_value_part_1()
            right_value = self.children[1].get_value_part_1()

            if self.operation == "+":
                self.value = left_value + right_value
                return left_value + right_value
            elif self.operation == "-":
                self.value = left_value - right_value
                return left_value - right_value
            elif self.operation == "*":
                return left_value * right_value
            else:
                self.value = left_value // right_value
                return left_value // right_value

    def check_node_exist_in_children(self, node: Node) -> bool:
        if node in self.children:
            return True
        else:
            for child in self.children:
                if child.check_node_exist_in_children(node):
                    return True
            return False

    def get_value_part_2(self, humn_node: Node) -> int | None:
        if self.value is not None:
            return self.value
        else:
            if self.check_node_exist_in_children(humn_node) or self.name == "humn":
                return None

            if self.children.__len__() == 0:
                print("name", self.name, "value", self.value)
                return print("error")

            left_value = self.children[0].get_value_part_2(humn_node)
            right_value = self.children[1].get_value_part_2(humn_node)
            if left_value is None or right_value is None:
                return None

            if self.operation == "+":
                self.value = left_value + right_value
                return left_value + right_value
            elif self.operation == "-":
                self.value = left_value - right_value
                return left_value - right_value
            elif self.operation == "*":
                self.value = left_value * right_value
                return left_value * right_value
            else:
                self.value = left_value // right_value
                return left_value // right_value


def create_nodes_part_1(data: list[str]) -> list[Node]:
    nodes: list[Node] = []
    for line in data:
        temp = line.replace(":", "")
        name, *_ = temp.split(" ")
        nodes.append(Node(name))

    for line in data:
        temp = line.replace(":", "")
        name, *rest = temp.split(" ")

        current_node = next(x for x in nodes if x.name == name)
        if len(rest) == 1:
            current_node.value = int(rest[0])
        else:
            current_node.operation = rest[1]
            left_child_node = next(x for x in nodes if x.name == rest[0])
            current_node.children.append(left_child_node)
            right_child_node = next(x for x in nodes if x.name == rest[2])
            current_node.children.append(right_child_node)

    return nodes


def part_1(data: list[str]) -> int:
    nodes = create_nodes_part_1(data)
    root = next(x for x in nodes if x.name == "root")
    ans = root.get_value_part_1()
    print("ans:", ans)
    return ans


def create_nodes_part_2(data: list[str]) -> list[Node]:
    nodes: list[Node] = []
    for line in data:
        temp = line.replace(":", "")
        name, *_ = temp.split(" ")
        nodes.append(Node(name))

    for line in data:
        temp = line.replace(":", "")
        name, *rest = temp.split(" ")

        current_node = next(x for x in nodes if x.name == name)
        if len(rest) == 1:
            if current_node.name == "humn":
                current_node.value = None
            else:
                current_node.value = int(rest[0])

        else:
            left_child_node = next(x for x in nodes if x.name == rest[0])
            current_node.children.append(left_child_node)
            right_child_node = next(x for x in nodes if x.name == rest[2])
            current_node.children.append(right_child_node)

            if current_node.name == "root":
                current_node.operation = "="
            else:
                current_node.operation = rest[1]

    return nodes


def compute_node_value_part_2(parent_node: Node, humn_node: Node) -> int:
    root_left_node = parent_node.children[0]
    root_right_node = parent_node.children[1]

    root_left_node.get_value_part_2(humn_node)
    root_right_node.get_value_part_2(humn_node)

    if root_left_node.value is None:
        target_node = root_left_node
        known_node = root_right_node
    else:
        target_node = root_right_node
        known_node = root_left_node

    if parent_node.value is None or known_node.value is None:
        print(
            "parent_node.name:",
            parent_node.name,
            "parent_node.value:",
            parent_node.value,
        )
        print(
            "known_node.name:", known_node.name, "known_node.value:", known_node.value
        )
        print(
            "target_node.name:",
            target_node.name,
            "target_node.value:",
            target_node.value,
        )
        return -1

    if parent_node.operation == "+":
        target_node.value = parent_node.value - known_node.value
    elif parent_node.operation == "-":
        target_node.value = parent_node.value + known_node.value
    elif parent_node.operation == "*":
        target_node.value = parent_node.value // known_node.value
    else:
        target_node.value = parent_node.value * known_node.value

    if target_node.name == "humn":
        return target_node.value
    else:
        return compute_node_value_part_2(target_node, humn_node)


def part_2(data: list[str]) -> int:
    nodes = create_nodes_part_2(data)
    root = next(x for x in nodes if x.name == "root")
    humn = next(x for x in nodes if x.name == "humn")

    for child in root.children:
        child.get_value_part_2(humn)

    root_left_node = root.children[0]
    root_right_node = root.children[1]

    if root_left_node.value is None:
        root_left_node.value = root_right_node.value
        target_node = root_left_node
    else:
        root_right_node.value = root_left_node.value
        target_node = root_right_node

    ans = compute_node_value_part_2(target_node, humn)
    print("ans:", ans)
    print("humn.value:", humn.value)

    return ans


def run_testing():
    with open("test.txt", "r") as f:
        data = f.read().splitlines()

        if is_part_1:
            assert part_1(data) == test_part_1_answer
        else:
            assert part_2(data) == test_part_2_answer

        f.close()


def main():
    # * if next line changed, adjust the change in init.py
    with open("day21.txt", "r") as f:
        data = f.read().splitlines()

        part_1(data) if is_part_1 else part_2(data)

        f.close()


if __name__ == "__main__":
    run_testing() if is_testing else main()
