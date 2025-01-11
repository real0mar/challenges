import random


class RandomizedSet:

    def __init__(self):
        self.element_idx: dict[int, int] = {}
        self.vals: list[int] = []

    def insert(self, val: int) -> bool:
        if val in self.element_idx:
            return False
        self.vals.append(val)
        self.element_idx[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.element_idx:
            return False
        idx = self.element_idx[val]
        last_element = self.vals[-1]

        self.vals[idx] = last_element
        self.element_idx[last_element] = idx

        self.vals.pop()
        del self.element_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)  # ignore: S311


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
