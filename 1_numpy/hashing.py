class mapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class map:
    def __init__(self):
        self.bucketSize = 20
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0

    def getIndex(self, hashCode):
        return hashCode % 20

    def insert(self, key, value):
        hashCode = hash(key)
        index = self.getIndex(hashCode)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        head = self.buckets[index]
        newNode = mapNode(key, value)
        self.buckets[index] = newNode
        newNode.next = head
        self.count += 1