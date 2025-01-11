from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.time_map: defaultdict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        for i in range(len(self.time_map[key]) - 1, -1, -1):
            if self.time_map[key][i][0] <= timestamp:
                return self.time_map[key][i][1]

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
