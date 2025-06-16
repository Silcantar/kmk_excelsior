from kmk.keys import KC
from kmk.modules.combos import Sequence
import unicode as UC

sequences = [
    Sequence((KC.LEADER, KC.N1, KC.SLSH, KC.N4), UC.ONE_FOURTH, fast_reset=False),
    Sequence((KC.LEADER, KC.N1, KC.SLSH, KC.N2), UC.ONE_HALF, fast_reset=False),
    Sequence((KC.LEADER, KC.N3, KC.SLSH, KC.N4), UC.THREE_FOURTHS, fast_reset=False),
    Sequence((KC.LEADER, KC.N1, KC.SLSH, KC.N7), UC.ONE_SEVENTH, fast_reset=False),
    Sequence((KC.LEADER, KC.N1, KC.SLSH, KC.N9), UC.ONE_NINTH, fast_reset=False),
    Sequence((KC.LEADER, KC.N1, KC.SLSH, KC.N1, KC.N0), UC.ONE_TENTH, fast_reset=False),
    Sequence((KC.LEADER, KC.N1, KC.SLSH, KC.N3), UC.ONE_THIRD, fast_reset=False),
    Sequence((KC.LEADER, KC.N2, KC.SLSH, KC.N3), UC.TWO_THIRDS, fast_reset=False),
    Sequence((KC.LEADER, KC.N1, KC.SLSH, KC.N5), UC.ONE_FIFTH, fast_reset=False),
    Sequence((KC.LEADER, KC.N2, KC.SLSH, KC.N5), UC.TWO_FIFTHS, fast_reset=False),
    Sequence((KC.LEADER, KC.N3, KC.SLSH, KC.N5), UC.THREE_FIFTHS, fast_reset=False),
    Sequence((KC.LEADER, KC.N4, KC.SLSH, KC.N5), UC.FOUR_FIFTHS, fast_reset=False),
    Sequence((KC.LEADER, KC.N1, KC.SLSH, KC.N6), UC.ONE_SIXTH, fast_reset=False),
    Sequence((KC.LEADER, KC.N5, KC.SLSH, KC.N6), UC.FIVE_SIXTHS, fast_reset=False),
    Sequence((KC.LEADER, KC.N1, KC.SLSH, KC.N8), UC.ONE_EIGHTH, fast_reset=False),
    Sequence((KC.LEADER, KC.N3, KC.SLSH, KC.N8), UC.THREE_EIGHTHS, fast_reset=False),
    Sequence((KC.LEADER, KC.N5, KC.SLSH, KC.N8), UC.FIVE_EIGHTHS, fast_reset=False),
    Sequence((KC.LEADER, KC.N7, KC.SLSH, KC.N8), UC.SEVEN_EIGHTHS, fast_reset=False),
    Sequence((KC.LEADER, KC.N0, KC.SLSH, KC.N3), UC.ZERO_THIRDS, fast_reset=False),
]