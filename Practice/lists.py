class List:
    def __init__(self):
        self.arr = [1,2,3]

    [1,2,3,4]
    [1,2,6,3,4]
    def insertAtIndex(self, num, arr, index):
        for i in range(index, arr.length()):
            arr[i + 1] = arr[i]
        num = arr[index]

        return arr