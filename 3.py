class Node:
    def __init__(self, num):
        self.right = None
        self.left = None
        self.num = num

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def calculateMaxDepth(self):
        factors = []
        divisor = 2
        while self.num > 1:
            if self.num % divisor == 0:
                factors.append(divisor)
                self.num = self.num // divisor
            else:
                divisor += 1
        while not self.is_prime(divisor):
                divisor += 1

        return len(factors) - 1


node_example = Node(60)
result = node_example.calculateMaxDepth()
print(result)