class Character:
    name = ""
    map = None

    def __init__(self, character_name):
        self.name = character_name if character_name != "" else "Cowboy Hank"

    def enter_map(self, m):
        self.map = m
