#  Supported video formats
#  GoPro (HERO 5 and later)
#  Sony (a1, a7c, a7r IV, a7 IV, a7s III, a9 II, FX3, FX6, FX9, RX0 II, RX100 VII, ZV1, ZV-E10)
#  Insta360 (OneR, OneRS, SMO 4k, Go, GO2, Caddx Peanut)
#  DJI (Avata, O3 Air Unit, Action 2)
#  Blackmagic RAW (*.braw)
#  RED RAW (V-Raptor, KOMODO) (*.r3d)
#  Betaflight blackbox (*.bfl, *.bbl, *.csv)
#  ArduPilot logs (*.bin, *.log)
#  Gyroflow .gcsv log
#  iOS apps: Sensor Logger, G-Field Recorder, Gyro, GyroCam
#  Android apps: Sensor Logger, Sensor Record, OpenCamera Sensors, MotionCam Pro
#  Runcam CSV (Runcam 5 Orange, iFlight GOCam GR, Runcam Thumb, Mobius Maxi 4K)
#  Hawkeye Firefly X Lite CSV
#  XTU (S2Pro, S3Pro)
#  WitMotion (WT901SDCL binary and *.txt)
#  Vuze (VuzeXR)
#  KanDao (Obisidian Pro)
#  CAMM format

import telemetry_parser
tp = telemetry_parser.Parser('./media/gopro.mp4')
telemetry = tp.telemetry()
print(telemetry)
