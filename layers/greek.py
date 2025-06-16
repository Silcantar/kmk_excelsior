from kmk.keys import KC
from features.alias import ________, XXXXXXXX

import features.alias as AL
import features.macros as MC
import features.unicode as UC

# Template for all-transparent layer.
greek = [
        # 5b              5a              4               3               2               1               0
                          ________      , AL.SGREEK     , AL.CLEAR      , ________      , ________      , ________      ,   # 00
                          ________      , XXXXXXXX      , UC.alpha      , UC.GQUES      , UC.IEXCL      , ________      ,   # 01
                          ________      , UC.zeta       , UC.sigma      , UC.fsigma     , UC.SECTION    , ________      ,   # 02
          ________                      , UC.chi        , UC.delta      , UC.epsilon    , UC.GBP        , ________      ,   # 03
                          XXXXXXXX      , UC.psi        , UC.phi        , UC.rho        , UC.CENT       , ________      ,   # 04
          AL.SGREEK                     , UC.omega      , UC.gamma      , UC.tau        , UC.PERMYR     , ________      ,   # 05
                          ________      , UC.beta       , UC.eta        , UC.upsilon    , UC.YEN        , ________      ,   # 06
          ________                      , UC.nu         , UC.xi         , UC.theta      , UC.EURO       , ________      ,   # 07
          ________                      , UC.mu         , UC.kappa      , UC.iota       , UC.MULT       , ________      ,   # 08
          ________                      , UC.LTE        , UC.lamda      , UC.omicron    , UC.DEG        , ________      ,   # 09
                          ________      , UC.GTE        , UC.DAGGER     , UC.pi         , MC.TRIPLE0    , ________      ,   # 10
                          ________      , UC.IQUES      , UC.DDAGGER    , UC.CHECK      , UC.NDASH      , ________      ,   # 11
                          ________      , AL.SGREEK     , ________      , UC.BALLOTX    , UC.MDASH      , ________      ,   # 12
                          ________      , XXXXXXXX      , ________      , ________      , ________      , ________      ,   # 13
                          ________      , ________      , ________      , ________      , ________      , ________      ,   # 14
                          ________      , ________      , ________      , ________      , ________      , ________      ,   # 15
                          ________      , ________      , ________      , ________      , ________      , ________      ,   # 16
                          ________      , ________      , ________      , ________      , ________      , ________      ,   # 17
                          ________      , ________      , ________      , ________      , ________      , ________      ,   # 18
                          ________      , AL.SGREEK     , ________      , ________      , ________      , ________      ,   # 19
                          ________      , UC.DDAGGER    , KC.LCBR       , KC.RCBR       , UC.ACUTE      , ________      ,   # 20
                          UC.SHEKEL     , UC.IEXCL      , UC.CENT       , UC.EURO       , UC.INTBANG    , ________      ,   # 21
                          UC.WON        , UC.SECTION    , UC.PERMYR     , UC.BITCOIN    , KC.BSLS       , ________      ,   # 22
                          UC.GTE        , UC.GBP        , UC.YEN        , UC.RUPEE      , UC.MULT       , ________      ,   # 23
                          UC.LTE        , ________      , UC.MDASH      , UC.APPEQL     , UC.NDASH      , ________      ,   # 24
                          ________      , AL.SGREEK     , ________      , ________      , ________      , ________      ,   # 25
    ]