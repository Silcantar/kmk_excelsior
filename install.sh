mkdir ./lib/

rsync -av ./submodules/kmk_firmware/kmk/ ./kmk/
rsync -av ./submodules/Adafruit_CircuitPython_MCP230xx/adafruit_mcp230xx/ ./lib/adafruit_mcp230xx/
rsync -av ./submodules/Adafruit_CircuitPython_SSD1322/adafruit_ssd1322.py ./lib/adfruit_ssd1322.py

rsync -avm --delete --filter='merge install.rules' ./ /media/$USER/EXCELSIOR/