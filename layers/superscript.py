from kmk.keys import KC
from features.alias import ________, XXXXXXXX

from features import alias as AL
from features import unicode as UC

# Template for all-transparent layer.
superscript = [
        # 5b              5a              4               3               2               1               0
                          ________      , AL.SSUPER     , AL.CLEAR      , ________      , ________      , ________      ,   # 00
                          ________      , XXXXXXXX      , UC.SUP_a      , ________      , UC.SUP_1      , ________      ,   # 01
                          ________      , UC.SUP_z      , UC.SUP_s      , UC.SUP_w      , UC.SUP_2      , ________      ,   # 02
          ________                      , UC.SUP_x      , UC.SUP_d      , UC.SUP_e      , UC.SUP_3      , ________      ,   # 03
                          XXXXXXXX      , UC.SUP_c      , UC.SUP_f      , UC.SUP_r      , UC.SUP_4      , ________      ,   # 04
          AL.SSUPER                     , UC.SUP_v      , UC.SUP_g      , UC.SUP_t      , UC.SUP_5      , ________      ,   # 05
                          ________      , UC.SUP_b      , UC.SUP_h      , UC.SUP_y      , UC.SUP_6      , ________      ,   # 06
          ________                      , UC.SUP_n      , UC.SUP_j      , UC.SUP_u      , UC.SUP_7      , ________      ,   # 07
          ________                      , UC.SUP_m      , UC.SUP_k      , UC.SUP_i      , UC.SUP_8      , ________      ,   # 08
          ________                      , ________      , UC.SUP_l      , UC.SUP_o      , UC.SUP_9      , ________      ,   # 09
                          ________      , ________      , ________      , UC.SUP_p      , UC.SUP_0      , ________      ,   # 10
                          ________      , ________      , ________      , ________      , UC.SUP_MIN    , ________      ,   # 11
                          ________      , AL.SSUPER     , ________      , ________      , UC.SUP_EQL    , ________      ,   # 12
                          ________      , XXXXXXXX      , ________      , ________      , ________      , ________      ,   # 13
                          ________      , ________      , ________      , ________      , ________      , ________      ,   # 14
                          ________      , ________      , ________      , ________      , ________      , ________      ,   # 15
                          ________      , ________      , ________      , ________      , ________      , ________      ,   # 16
                          ________      , ________      , ________      , ________      , ________      , ________      ,   # 17
                          ________      , ________      , ________      , ________      , ________      , ________      ,   # 18
                          ________      , AL.SSUPER     , ________      , ________      , ________      , ________      ,   # 19
                          ________      , UC.SUP_LPN    , UC.SUP_RPN    , ________      , ________      , ________      ,   # 20
                          UC.SUP_0      , UC.SUP_1      , UC.SUP_4      , UC.SUP_7      , ________      , ________      ,   # 21
                          ________      , UC.SUP_2      , UC.SUP_5      , UC.SUP_8      , ________      , ________      ,   # 22
                          ________      , UC.SUP_3      , UC.SUP_6      , UC.SUP_9      , ________      , ________      ,   # 23
                          ________      , ________      , UC.SUP_PLS    , UC.SUP_EQL    , UC.SUP_MIN    , ________      ,   # 24
                          ________      , AL.SSUPER     , ________      , ________      , ________      , ________      ,   # 25
    ]