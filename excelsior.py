import board
import busio
from digitalio import Pull

from adafruit_mcp230xx.mcp23017 import MCP23017 # type: ignore

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.digitalio import MatrixScanner
from kmk.scanners import DiodeOrientation

# Imports for Displays
import displayio

from kmk.extensions.display import Display, TextEntry, ImageEntry

from lib.adafruit_ssd1322 import SSD1322

class Excelsior(KMKKeyboard):
    def __init__(self):
        super().__init__()

        i2c = busio.I2C(scl=board.GP5, sda=board.GP4, frequency=100000)
        mcp20 = MCP23017(i2c, address=0x20)
        mcp21 = MCP23017(i2c, address=0x21)
        
        # Create and register the scanner.
        # Columns and rows are 'reversed' from what they should be to make keymaps vertical rather than horizontal.
        self.matrix = [
            MatrixScanner(
                cols=(
                    board.GP10,
                    board.GP11,
                    board.GP12,
                    board.GP13,
                    board.GP14,
                    board.GP15,
                    board.GP16,
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
                ),
                
                diode_orientation=DiodeOrientation.ROW2COL,
                pull=Pull.UP,
            ),

            MatrixScanner(
                cols=(
                    mcp20.get_pin(1),
                    mcp20.get_pin(2),
                    mcp20.get_pin(3),
                    mcp20.get_pin(4),
                    mcp20.get_pin(5),
                    mcp20.get_pin(6),
                ),

                rows=(
                    mcp20.get_pin(9),
                    mcp20.get_pin(10),
                    mcp20.get_pin(11),
                    mcp20.get_pin(12),
                    mcp20.get_pin(13),
                    mcp20.get_pin(14),
                ),
                
                diode_orientation=DiodeOrientation.ROW2COL,
                pull=Pull.UP,
            ),

            MatrixScanner(
                cols=(
                    mcp21.get_pin(1),
                    mcp21.get_pin(2),
                    mcp21.get_pin(3),
                    mcp21.get_pin(4),
                    mcp21.get_pin(5),
                    mcp21.get_pin(6),
                ),

                rows=(
                    mcp21.get_pin(9),
                    mcp21.get_pin(10),
                    mcp21.get_pin(11),
                    mcp21.get_pin(12),
                    mcp21.get_pin(13),
                    mcp21.get_pin(14),
                ),
                
                diode_orientation=DiodeOrientation.ROW2COL,
                pull=Pull.UP,
            )
        ]

        # Initialize Displays

        spi = busio.SPI(board.GP2, board.GP3)

        left_display_bus = displayio.FourWire(spi, command=mcp20.get_pin(7), chip_select=mcp_20.get_pin(8), reset=mcp20.get_pin(15), baudrate=1000000)
        right_display_bus = displayio.FourWire(spi, command=mcp21.get_pin(7), chip_select=mcp_21.get_pin(8), reset=mcp21.get_pin(15), baudrate=1000000)

        time.sleep(1)

        left_display = SSD1322(left_display_bus, width=256, height=64, colstart=28)
        right_display = SSD1322(right_display_bus, width=256, height=64, colstart=28)