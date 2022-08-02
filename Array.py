import ctypes


class Array(object):

    def __init__(self):
        self.item_count = 0
        self.array_capacity = 1
        self.primary_array = self._create_array(self.array_capacity)

    def _create_array(self, array_capacity):
        return (array_capacity * ctypes.py_object)()

    def list(self):
        return " ".join(str(self.primary_array[x]) for x in range(self.item_count))

    def __len__(self):
        return self.item_count

    def __getitem__(self, item_index):
        if not 0 <= item_index < self.item_count:
            return IndexError('index out of range!')
        return self.primary_array[item_index]

    def append(self, item):
        if self.item_count == self.array_capacity:
            self._extend_array(2*self.array_capacity)
        self.primary_array[self.item_count] = item
        self.item_count += 1

    def _extend_array(self, new_capacity):
        secondary_array=self._create_array(new_capacity)
        for i in range(self.array_capacity):
            secondary_array[i] = self.primary_array[i]
        self.primary_array = secondary_array
        self.array_capacity = new_capacity

    def delete(self,index):
        for i in range(index,self.item_count-1):
            self.primary_array[i]=self.primary_array[i+1]




array = Array()
for i in range(10):
    array.append(i)
array.delete(3)
print(array.list())