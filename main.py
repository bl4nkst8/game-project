from character import Character
from window import Window

if __name__ == "__main__":
    window = Window()
    character = Character(window.screen)
    character.run()
    window.run()
