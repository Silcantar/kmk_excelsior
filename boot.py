# Copy this file to the root of the CIRCUITPY drive and disconnect/reconnect it to rename it to EXCELSIOR.

import storage

storage.remount("/", readonly=False)

m = storage.getmount("/")
m.label = "EXCELSIOR"

storage.remount("/", readonly=True)

storage.enable_usb_drive()