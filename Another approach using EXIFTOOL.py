

import subprocess
import json
import re


def formatGPSData(dms_string):
    dms_pattern = r'(\d+) deg (\d+)\' ([\d.]+)" ([NSEW])'
    match = re.match(dms_pattern, dms_string)
    if not match:
        raise ValueError("Invalid DMS format")
    degrees, minutes, seconds, direction = match.groups()
    degrees, minutes, seconds = map(float, (degrees, minutes, seconds))
    decimal_degrees = degrees + minutes/60 + seconds/3600

    if direction in ['S', 'W']:
        decimal_degrees = -decimal_degrees

    return round(decimal_degrees, 4)


# Define the command to run+
if __name__ == "__main__":
    command = "exiftool.exe -json ./media/iphone.mov"

    # Run the subprocess and capture the output
    completed_process = subprocess.run(
        command, stdout=subprocess.PIPE, shell=True, text=True)

    # Check for errors
    if completed_process.returncode == 0:
        json_output = completed_process.stdout
        data = json.loads(json_output)
        GPSLatitude = formatGPSData(data[0]['GPSLatitude'])
        GPSLongitude = formatGPSData(data[0]['GPSLongitude'])
        print(GPSLatitude)
        print(GPSLongitude)

    else:
        print("Subprocess returned an error:", completed_process.returncode)
