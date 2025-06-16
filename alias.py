from kmk.keys import KC, LCTL, LSFT, RSFT
import unicode as UC
import macros as MC

________ = KC.TRNS
XXXXXXXX = KC.NO

# Layer Switches
CLEAR   = KC.TO(0)
GREEK   = KC.MO(2)
SGREEK  = KC.MO(3)
SSUPER  = KC.MO(5)
SSUB    = KC.MO(7)
MC_PLY  = KC.MO(8)
MC_REC  = KC.MO(9)

LM_LSFT = KC.LM(1, LSFT)
LM_RSFT = KC.LM(1, RSFT)

# Hold-Taps
FRAC    = KC.HT(UC.FRACTION_SLASH   , KC.LEADER)    # Tap: Fraction Slash               | Hold: Sequence Leader
CAPS    = KC.HT(KC.CAPS             , KC.MO(10))    # Tap: Caps Lock                    | Hold: Lock Layer
SUPER   = KC.HT(LCTL(LSFT(KC.EQL))  , KC.MO(4))     # Tap: C-S-= (MS Word Superscript)  | Hold: Superscript Layer
SUB     = KC.HT(LCTL(KC.EQL)        , KC.MO(6))     # Tap: C-= (MS Word Subscript)      | Hold: Subscript Layer

# Modified Keys
BOT     = LCTL(KC.END)
COPY    = LCTL(KC.C)
CUT     = LCTL(KC.X)
PASTE   = LCTL(KC.V)
REDO    = LCTL(KC.Y)
REPL    = LCTL(KC.H)
TOP     = LCTL(KC.HOME)
UNDO    = LCTL(KC.Z)
WRDL    = LCTL(KC.LEFT)
WRDR    = LCTL(KC.RGHT)