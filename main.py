# Copy this file to the root of the EXCELSIOR drive.

print('Starting')

from excelsior import Excelsior

excelsior = Excelsior()

#******************************************************************************#
#                                                                              #
#                           Module & Extension Imports                         #
#                                                                              #
#******************************************************************************#

#-------------------------------- Hold/Tap ------------------------------------#
from kmk.modules.holdtap import HoldTap
excelsior.modules.append(HoldTap())

#--------------------------------- Macros -------------------------------------#
from kmk.modules.macros import Macros, UnicodeModeWinC
excelsior.modules.append(Macros(unicode_mode=UnicodeModeWinC)) # type: ignore

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
    timeout=60000,  # Maximum time to spend in record or config mode, milliseconds
    key_interval=10,  # Milliseconds between key events while playing
    use_recorded_speed=False  # Whether to play the sequence at the speed it was typed
)

excelsior.modules.append(dynamicSequences)

#-------------------------------- International -------------------------------#
from kmk.extensions.international import International
excelsior.extensions.append(International())

#--------------------------------- Media Keys ---------------------------------#
from kmk.extensions.media_keys import MediaKeys
excelsior.extensions.append(MediaKeys())


#******************************************************************************#
#                                                                              #
#                                   Keymap                                     #
#                                                                              #
#******************************************************************************#
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

if __name__ == '__main__':
    excelsior.go()