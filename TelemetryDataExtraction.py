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

try:
    # Initialize the telemetry parser with the video file path
    tp = telemetry_parser.Parser('./media/test.MP4')

    # ADJUST YOUR FREQUENCY HERE (low or high).This is used to adjust the total number of output values.High provides all the latitude and longitude of all the intervals recorded
    frequency = 'high'

    # Initialize an empty array to store latitude and longitude objects
    gps_data_array = []

    # Get the telemetry data
    telemetry = tp.telemetry()

    for obj in telemetry:
        if "GPS" in obj:
            if "Data" in obj['GPS']:
                gpsData = obj['GPS']['Data']
                if (frequency == "low"):
                    if len(gpsData) % 2 == 0:  # Array has an even number of elements
                        middle_element = gpsData[len(gpsData) // 2 - 1]
                        # conversion to decimal
                        latitude = middle_element[0] / 10000000
                        # conversion to decimal
                        longitude = middle_element[1] / 10000000
                        gps_data_array.append(
                            {"latitude": latitude, "longitude": longitude})
                    else:  # Array has an odd number of elements
                        middle_element = gpsData[len(gpsData) // 2]
                        # conversion to decimal
                        latitude = middle_element[0] / 10000000
                        # conversion to decimal
                        longitude = middle_element[1] / 10000000
                        gps_data_array.append(
                            {"latitude": latitude, "longitude": longitude})
                else:
                    for data in gpsData:
                        latitude = data[0] / 10000000  # conversion to decimal
                        longitude = data[1] / 10000000  # conversion to decimal
                        gps_data_array.append(
                            {"latitude": latitude, "longitude": longitude})

    # Now, gps_data_array contains an array of objects, each with 'latitude' and 'longitude' keys.
    print("GPS Data Array:", gps_data_array)
# file not found exception
except FileNotFoundError:
    print("File not found. Please check the file path.")
# unknown exception
except Exception as e:
    print(f"An error occurred: {str(e)}")
