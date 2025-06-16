from kmk.keys import KC, Key

class CustomModifiedKey(Key):
    def __init__(self, baseKey, modifiedKey, mods=(KC.LSFT, KC.RSFT)):
        self.baseKey = baseKey
        self.modifiedKey = modifiedKey
        self.mods = mods

    def on_press(self, keyboard, coord_int=None):
        if any(i in keyboard.keys_pressed for i in self.mods):
            keyboard.add_key(self.modifiedKey)
        else:
            keyboard.add_key(self.baseKey)
    
    def on_release(self, keyboard, coord_int = None):
        return super().on_release(keyboard, coord_int)