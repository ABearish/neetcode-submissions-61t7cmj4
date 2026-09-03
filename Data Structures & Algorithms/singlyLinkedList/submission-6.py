class LinkedList:

    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        curr_idx = 0
        while curr:
            if curr_idx == index:
                return curr['val']
            curr = curr['next']
            curr_idx += 1        
        return -1

    def insertHead(self, val: int) -> None:
        new_head = {'val': val, 'next': self.head}
        self.head = new_head

    def insertTail(self, val: int) -> None:
        new_tail = {'val': val, 'next': None}
        if not self.head:
            self.head = new_tail
            return

        curr = self.head
        while curr['next']:
            curr = curr['next']
        curr['next'] = new_tail

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head['next']
            return True
        
        curr = self.head
        prev = None
        curr_count = 0
        while curr:
            if curr_count == index:
                prev['next'] = curr['next']
                return True 
            prev = curr
            curr = curr['next']
            curr_count += 1
        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr['val'])
            curr = curr['next']
        return values
        
