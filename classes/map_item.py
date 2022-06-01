

class Map_item:
    '''
    (todo docs)
    classes for a garbage
    '''
    item_sprites = [] # предметы должны как-то отображаться в окошке, я предлагаю соответственно тэгу присваивать спрайт.
    # Каким бы он ни был todo разобраться с отображением спрайтов

    # initializing garbage
    def __init__(self, volume, tag):
        if tag == 0:
            self.tag = tag
            self.volume = 0
        else:
            self.tag = tag
            self.volume = volume


