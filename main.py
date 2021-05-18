import random


class Node:
    def __init__(self, value, level):
        self.value = value
        self.next = [None]*(level+1)


class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.level = 1
        self.head = self.newNode(-1, self.max_level)

    def newNode(self, value, level):
        node = Node(value, level)
        return node

    def randomLevel(self):
        level = 1
        while level < self.max_level and random.random() < 0.5:
            level += 1
        return level

    def search(self, value):
        global o
        x = self.head
        for i in range(self.level, 0, -1):
            while x.next[i] != None and x.next[i].value < value:
                x = x.next[i]
        x = x.next[1]
        if x != None and x.value == value:
            o.write('1')
        else:
            o.write('0')
        o.write("\n")

    def insert(self, value):
        update = [None]*(self.max_level+1)
        x = self.head
        for i in range(self.level, 0, -1):
            while x.next[i] != None and x.next[i].value < value:
                x = x.next[i]
            update[i] = x
        x = x.next[1]
        if x == None or x.value != value:
            newLevel = self.randomLevel()
        if newLevel > self.level:
            for i in range(self.level+1, newLevel+1):
                update[i] = self.head
            self.level = newLevel
        node = self.newNode(value, newLevel)
        for i in range(1, newLevel+1):
            node.next[i] = update[i].next[i]
            update[i].next[i] = node

    def delete(self, value):
        update = [None]*(self.max_level+1)
        x = self.head
        for i in range(self.level, 0, -1):
            while x.next[i] != None and x.next[i].value < value:
                x = x.next[i]
            update[i] = x
        x = x.next[1]
        if x != None and x.value == value:
            for i in range(1, self.level+1):
                if update[i].next[i] != x:
                    break
                update[i].next[i] = x.next[i]
            while self.level > 1 and self.head.next[self.level] == None:
                self.level -= 1

    def successor(self, value):
        x = self.head
        for i in range(self.level, 0, -1):
            while x.next[i] != None and x.next[i].value < value:
                x = x.next[i]
        x = x.next[1]
        return x

    def predecessor(self, value):
        x = self.head
        for i in range(self.level, 0, -1):
            while x.next[i] != None and x.next[i].value < value:
                x = x.next[i]
        if x.next[1] != None and x.next[1].value == value:
            return x.next[1]
        else:
            return x

    def printInterval(self, value1, value2):
        global o
        x = self.successor(value1)
        y = self.predecessor(value2)
        while x != y:
            o.write(str(x.value))
            o.write(" ")
            x = x.next[1]
        if x == y:
            o.write(str(x.value))
        o.write("\n")

    def displaySkipList(self):
        print("\n*****Skip List******")
        for lvl in range(self.level, 0, -1):
            print("Level {}: ".format(lvl), end=" ")
            node = self.head.next[lvl]
            while node != None:
                print(node.value, end=" ")
                node = node.next[lvl]
            print("")


list = SkipList(15)
with open('abce.in', 'r') as f:
    with open('abce.out','w') as o:
        Q = int(f.readline())
        for line in f:
            x = [int(i) for i in line.split()]
            if x[0] == 1:
                list.insert(x[1])
            elif x[0] == 2:
                list.delete(x[1])
            elif x[0] == 3:
                list.search(x[1])
            elif x[0] == 4:
                o.write(str(list.predecessor(x[1]).value))
                o.write("\n")
            elif x[0] == 5:
                o.write(str(list.successor(x[1]).value))
                o.write("\n")
            else:
                list.printInterval(x[1], x[2])
