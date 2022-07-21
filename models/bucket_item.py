class BucketItem:
    def __init__(self, traveller, destination, visited = False, id = None):
        self.traveller = traveller
        self.destination = destination
        self.visited = visited
        self.id = id
