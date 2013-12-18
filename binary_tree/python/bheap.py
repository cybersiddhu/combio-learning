class BinHeap():
    def __init__(self):
        self.heap_list = [0]
        self.currsize = 0


def percolate_up(self, i):
    """percolate a new item up to the tree to maintain the heap structure"""
    while i // 2 > 0:  # as long the size is greater than 2
        if self.heap_list[i] < self.heap_list[i // 2]:
            # new item is less than parent( remember
            # access parent by dividing index by 2 )
            tmp_parent = self.heap_list[i // 2]
            # current item is the new parent
            self.heap_list[i // 2] = self.heap_list[i]
            self.heap_list[i] = tmp_parent
        i = i // 2


def insert(self, k):
    """insert a node in the heap"""
    self.heap_list.append(k)
    self.currsize = self.currsize + 1
    self.percolate_up(self.currsize)


def percolate_down(self, i):
    """percolate a new item down the  tree to maintain the heap structure"""
    while i * 2 >= self.currsize:
        mc = self.minchild(i)
        if self.heap_list[i] > self.heap_list[mc]:
            tmp = self.heap_list[i]
            self.heap_list[i] = self.heap_list[mc]
            self.heap_list[mc] = tmp
        i = mc


def minchild(self, i):
    """find the minimum child in tree"""
    if i * 2 + 1 > self.currsize:
        return i * 2
    else:
        if self.heap_list[i*2] < self.heap_list[i*2+1]:
            return i * 2
        else:
            return i * 2 + 1


def delmin(self):
    """delete the root and maintain the heap"""
    retval = self.heap_list[1]
    self.heap_list[1] = self.currsize
    self.currsize = self.currsize - 1
    self.heap_list.pop()
    self.percolate_down(1)
    return retval
