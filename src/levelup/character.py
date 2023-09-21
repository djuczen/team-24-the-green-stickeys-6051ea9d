from levelup.position import Position


class Character:
    name = ""
    map = None
    position = None

    def __init__(self, character_name):
        self.name = character_name if character_name != "" else "Cowboy Hank"
        self.position = Position(0,0)

    def enter_map(self, m):
        self.map = m

    def move(self,direction):
        return direction