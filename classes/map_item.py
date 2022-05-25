

class Map_item:
    '''
    (todo docs)
    class for a garbage
    '''

    # initializing garbage
    def __init__(self, volume, tag):
        if tag == 0:
            self.tag = tag
            self.volume = 0
        else:
            self.tag = tag
            self.volume = volume


