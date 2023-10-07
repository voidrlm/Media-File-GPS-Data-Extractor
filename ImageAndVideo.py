import exiftool
try:
    with exiftool.ExifToolHelper() as et:
        # Provide file path here (Can use both image and video files)
        filepath = "./media/image.jpg"
        gps_data = et.get_metadata(
            filepath, ['-gpslatitude', '-gpslongitude'])
        print(gps_data)
except exiftool.ExifToolError as e:
    print(f"ExifToolError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
