from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def extract_gps_info(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
        return exif_data
    except Exception as e:
        print(f"Error: {e}")
        return None


coords = extract_gps_info('./media/image.jpg')
print(coords)
