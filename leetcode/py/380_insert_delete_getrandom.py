import random


class RandomizedSet:

    def __init__(self):
        self.location_map: dict[int, int] = {}
        self.internal_list: list[int] = []

    def insert(self, val: int) -> bool:
        if val not in self.location_map:
            self.internal_list.append(val)
            self.location_map[val] = len(self.internal_list) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.location_map:
            return False
        else:
            idx = self.location_map[val]
            last_element = self.internal_list[-1]

            self.internal_list[idx] = last_element
            self.location_map[last_element] = idx

            self.internal_list.pop()
            del self.location_map[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.internal_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
