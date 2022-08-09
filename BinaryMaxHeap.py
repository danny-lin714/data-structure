class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self._up(data)

    def _up(self,data):
        data_index = self.heap.index(data) + 1
        while data > self.heap[int(data_index / 2) - 1] and data_index > 1:
            smaller_index=int(data_index/2)
            self._swap(data_index, smaller_index)
            data_index = int(data_index / 2)

    def _swap(self,data_index,smaller_index):
        temp = self.heap[smaller_index-1]  # 將比較小的值記錄起來
        self.heap[smaller_index - 1] = self.heap[data_index - 1]  # 將資料換到較小的值的位置
        self.heap[data_index - 1] = temp  # 將較小資料換到原始資料的位置
    """
    def _down(self):
    """

a = BinaryHeap()

for i in range(1, 10):
    a.insert(i)
    print(a.heap)

