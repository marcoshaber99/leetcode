
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None


class BrowserHistory:
    def __init__(self, homepage: str):
         
        # Current page in the browser
        self.current = Node(homepage) 

        # Pointer to represent the future browsing history
        self.future = None  

    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node
        self.future = None


    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.future = self.current
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.future:
            self.current = self.future
            self.future = self.future.next
            steps -= 1
        return self.current.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)