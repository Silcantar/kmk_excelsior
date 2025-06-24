#!/usr/bin/env bash

# Create lib folder if it doesn't exist already.
mkdir ./lib/

# Copy submodules to the locations required by CircuitPython.
rsync -av ./submodules/kmk_firmware/kmk/ ./kmk/
rsync -av ./submodules/Adafruit_CircuitPython_MCP230xx/adafruit_mcp230xx/ ./lib/adafruit_mcp230xx/
rsync -av ./submodules/Adafruit_CircuitPython_SSD1322/adafruit_ssd1322.py ./lib/adfruit_ssd1322.py

# Copy firmware files to the keyboard controller.
rsync -avm --delete --filter='merge install.rules' ./ /media/$USER/EXCELSIOR/