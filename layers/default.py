from kmk.keys import KC
from features.alias import ________, XXXXXXXX

import features.alias as AL
import features.macros as MC
import features.unicode as UC

# Template for all-transparent layer.
default = [
        # 5b              5a              4               3               2               1               0
                          KC.LALT       , AL.LM_LSFT    , AL.CAPS       , KC.TAB        , KC.ESC        , KC.F1         ,   # 00
                          KC.LWIN       , XXXXXXXX      , KC.A          , KC.Q          , KC.N1         , KC.F2         ,   # 01
                          KC.LCTL       , KC.Z          , KC.S          , KC.W          , KC.N2         , KC.F3         ,   # 02
          AL.GREEK                      , KC.X          , KC.D          , KC.E          , KC.N3         , KC.F4         ,   # 03
                          XXXXXXXX      , KC.C          , KC.F          , KC.R          , KC.N4         , KC.F5         ,   # 04
          AL.LM_LSFT                    , KC.V          , KC.G          , KC.T          , KC.N5         , KC.F6         ,   # 05
                          KC.SPC        , KC.B          , KC.H          , KC.Y          , KC.N6         , KC.F7         ,   # 06
          KC.TAB                        , KC.N          , KC.J          , KC.U          , KC.N7         , KC.F8         ,   # 07
          KC.ENT                        , KC.M          , KC.K          , KC.I          , KC.N8         , KC.F9         ,   # 08
          AL.GREEK                      , KC.COMM       , KC.L          , KC.O          , KC.N9         , KC.F10        ,   # 09
                          KC.RCTL       , KC.DOT        , KC.SCLN       , KC.P          , KC.N0         , KC.F11        ,   # 10
                          KC.RWIN       , KC.SLSH       , KC.QUOT       , KC.LBRC       , KC.MINS       , KC.F12        ,   # 11
                          KC.APPS       , AL.LM_RSFT    , KC.ENT        , KC.RBRC       , KC.EQL        , KC.F13        ,   # 12
                          KC.RALT       , XXXXXXXX      , KC.BSLS       , KC.BSPC       , KC.F15        , KC.F14        ,   # 13
                          AL.GREEK      , KC.PGDN       , AL.WRDL       , KC.PGUP       , KC.INS        , KC.F16        ,   # 14
                          AL.PASTE      , AL.UNDO       , KC.LEFT       , KC.HOME       , KC.PSCR       , KC.F17        ,   # 15
                          AL.COPY       , KC.F2         , KC.DOWN       , KC.UP         , AL.FRAC       , KC.F18        ,   # 16
                          AL.CUT        , AL.REDO       , KC.RIGHT      , KC.END        , AL.SUB        , KC.F19        ,   # 17
                          AL.FIND       , AL.BOT        , AL.WRDR       , AL.TOP        , AL.SUPER      , KC.F20        ,   # 18
                          KC.LALT       , AL.LM_LSFT    , KC.BSPC       , KC.LCTL       , KC.TAB        , KC.F21        ,   # 19
                          KC.SPC        , KC.QUOT       , KC.LPRN       , KC.RPRN       , KC.GRV        , KC.F22        ,   # 20
                          KC.P0         , KC.N1         , KC.N4         , KC.N7         , UC.RADICAL    , KC.F23        ,   # 21
                          MC.TRIPLE0    , KC.N2         , KC.N5         , KC.N8         , KC.PSLS       , KC.F24        ,   # 22
                          KC.DOT        , KC.N3         , KC.N6         , KC.N9         , KC.PAST       , KC.PSCR       ,   # 23
                          KC.COMM       , KC.PENT       , KC.PPLS       , KC.PEQL       , KC.MINS       , KC.SLCK       ,   # 24
                          KC.RALT       , AL.LM_RSFT    , KC.DEL        , KC.RCTL       , KC.TAB        , KC.PAUS       ,   # 25
    ]