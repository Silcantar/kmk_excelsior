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