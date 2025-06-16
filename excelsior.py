import board
import busio
from digitalio import Pull

from adafruit.mcp23017 import MCP23017

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.digitalio import MatrixScanner
from kmk.scanners import DiodeOrientation

class Excelsior(KMKKeyboard):
    def __init__(self):
        super().__init__()

        i2c = busio.I2C(scl=board.GP5, sda=board.GP4, frequency=100000)
        mcp20 = MCP23017(i2c, address=0x20)
        mcp21 = MCP23017(i2c, address=0x21)
        
        # Create and register the scanner.
        # Columns and rows are reversed from what they should be to 
        self.matrix = MatrixScanner(
            cols=(
                board.GP10,
                board.GP11,
                board.GP12,
                board.GP13,
                board.GP14,
                board.GP15,
                board.GP16,
                mcp20.get_pin(1),
                mcp20.get_pin(2),
                mcp20.get_pin(3),
                mcp20.get_pin(4),
                mcp20.get_pin(5),
                mcp20.get_pin(6),
                mcp21.get_pin(1),
                mcp21.get_pin(2),
                mcp21.get_pin(3),
                mcp21.get_pin(4),
                mcp21.get_pin(5),
                mcp21.get_pin(6)
            ),

            rows=(
                board.GP17, 
                board.GP18, 
                board.GP19, 
                board.GP20, 
                board.GP21, 
                board.GP22, 
                board.GP23, 
                board.GP24, 
                board.GP25, 
                board.GP26,
                board.GP27,
                board.GP28,
                board.GP29,
                board.GP30,
                mcp20.get_pin(9),
                mcp20.get_pin(10),
                mcp20.get_pin(11),
                mcp20.get_pin(12),
                mcp20.get_pin(13),
                mcp20.get_pin(14),
                mcp21.get_pin(9),
                mcp21.get_pin(10),
                mcp21.get_pin(11),
                mcp21.get_pin(12),
                mcp21.get_pin(13),
                mcp21.get_pin(14)
            ),
            
            diode_orientation=DiodeOrientation.ROW2COL,
            pull=Pull.UP,
        )

excelsior = Excelsior()

#******************************************************************************#
#                                                                              #
#                               Module Imports                                 #
#                                                                              #
#******************************************************************************#

#--------------------------------- Macros -------------------------------------#
from kmk.modules.macros import Macros, UnicodeModeWinC
excelsior.modules.append(Macros(UnicodeMode=UnicodeModeWinC))

#---------------------------- Combos/Sequences --------------------------------#
from kmk.modules.combos import Combos
combos = Combos()
excelsior.modules.append(combos)

from features.combos import sequences
combos.combos = sequences

#----------------------------------- Layers -----------------------------------#
from kmk.modules.layers import Layers
layers = Layers()
layers.combo_layers = {
    (2, 8): 9,  # Greek + Macro Play = Macro Record
    (2, 9): 8,  # Greek + Macro Record = Macro Play - this probably doesn't work
}
excelsior.modules.append(layers)

#------------------------------ Dynamic Sequences -----------------------------#

from kmk.modules.dynamic_sequences import DynamicSequences

dynamicSequences = DynamicSequences(
    slots=27, # The number of sequence slots to use
    timeout=60000,  # Maximum time to spend in record or config mode before stopping automatically, milliseconds
    key_interval=10,  # Milliseconds between key events while playing
    use_recorded_speed=False  # Whether to play the sequence at the speed it was typed
)

excelsior.modules.append(dynamicSequences)


#***********************************************************************************************************************************************#
#                                                                                                                                               #
#                                                                    Keymap                                                                     #
#                                                                                                                                               #
#***********************************************************************************************************************************************#
from layers.default import default
from layers.custom_shift import custom_shift
from layers.greek import greek
from layers.greek_shifted import greek_shifted
from layers.superscript import superscript
from layers.superscript_shifted import superscript_shifted
from layers.subscript import subscript
from layers.subscript_shifted import subscript_shifted
from layers.macro_play import macro_play
from layers.macro_record import macro_record
from layers.layer_lock import layer_lock

excelsior.keymap = [

    # 0: Default keymap
    default,

    # 1: Custom Shift
    custom_shift,

    # 2: Greek/Symbol
    greek,

    # 3: Greek/Symbol Shifted
    greek_shifted,

    # 4: Superscript
    superscript,

    # 5: Superscript Shifted
    superscript_shifted,

    # 6: Subscript
    subscript,

    # 7: Subscript Shifted
    subscript_shifted,

    # 8: Macro Play
    macro_play,

    # 9: Macro Record
    macro_record,

    # 10: Layer Lock
    layer_lock,

]