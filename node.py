class Node:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
        self.next = None
        self.prev = None