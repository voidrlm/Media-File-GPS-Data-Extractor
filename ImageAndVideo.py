import exiftool
with exiftool.ExifToolHelper() as et:
    # Provide file path here (Can use both image and video files)
    filepath = "./media/image.jpg"
    gps_data = et.get_metadata(
        filepath, ['-gpslatitude', '-gpslongitude'])
    print(gps_data)
