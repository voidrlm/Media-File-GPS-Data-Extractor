# This Python script leverages Pillow for extracting GPS metadata from images
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def extract_gps_info(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == 'GPSInfo':
                    gps_info = {GPSTAGS.get(t, t): v for t, v in value.items()}
                    latitude = gps_info.get('GPSLatitude')
                    longitude = gps_info.get('GPSLongitude')

                    if latitude and longitude:
                        latitude = float(
                            latitude[0]) + float(latitude[1]) / 60 + float(latitude[2]) / 3600
                        longitude = float(
                            longitude[0]) + float(longitude[1]) / 60 + float(longitude[2]) / 3600
                        if gps_info.get('GPSLatitudeRef') == 'S':
                            latitude = -latitude
                        if gps_info.get('GPSLongitudeRef') == 'W':
                            longitude = -longitude

                        return latitude, longitude
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


coords = extract_gps_info('./media/image.jpg')  # ADD YOUR IMAGE PATH HERE
if coords:
    latitude, longitude = coords
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("GPS information not found in the image metadata.")
