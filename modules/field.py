class Field:
    def __init__(self, middle):
        self._middle = middle
        self._up = None
        self._down = None
        self._left = None
        self._right = None

    @property
    def middle(self):
        return self._middle

    @middle.setter
    def middle(self, value):
        self._middle = value

    @property
    def up(self):
        return self._up

    @up.setter
    def up(self, value):
        self._up = value

    @property
    def down(self):
        return self._down

    @down.setter
    def down(self, value):
        self._down = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value
